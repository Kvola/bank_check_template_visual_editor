/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component, useState, useRef, onMounted, onWillUnmount } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

/**
 * Éditeur visuel de positionnement des éléments du chèque
 * Permet de positionner par glisser-déposer les différents éléments
 */
class CheckPositionEditor extends Component {
    setup() {
        this.orm = useService("orm");
        this.notification = useService("notification");
        
        this.checkRef = useRef("checkCanvas");
        this.state = useState({
            elements: [],
            selectedElement: null,
            isDragging: false,
            zoom: 1.0,
            showGrid: true,
            snapToGrid: true,
            gridSize: 5, // mm
        });

        onMounted(() => {
            this.loadPositions();
            this.setupInteractions();
        });

        onWillUnmount(() => {
            this.cleanupInteractions();
        });
    }

    /**
     * Charge les positions actuelles depuis les champs du modèle
     */
    async loadPositions() {
        const record = this.props.record;
        
        // Charger l'image du chèque si disponible
        this.checkImageUrl = null;
        if (record.data.check_image) {
            this.checkImageUrl = `/web/image?model=bank.check.template&id=${record.resId}&field=check_image`;
        }
        
        this.state.elements = [
            {
                id: 'date',
                label: 'Date',
                x: record.data.date_x || 120,
                y: record.data.date_y || 15,
                width: 40,
                height: 8,
                color: '#3498db',
                fields: ['date_x', 'date_y']
            },
            {
                id: 'beneficiary',
                label: 'Bénéficiaire',
                x: record.data.beneficiary_x || 15,
                y: record.data.beneficiary_y || 30,
                width: record.data.beneficiary_width || 140,
                height: 10,
                color: '#2ecc71',
                fields: ['beneficiary_x', 'beneficiary_y', 'beneficiary_width']
            },
            {
                id: 'amount_digits',
                label: 'Montant (chiffres)',
                x: record.data.amount_digits_x || 120,
                y: record.data.amount_digits_y || 45,
                width: 40,
                height: 10,
                color: '#e74c3c',
                fields: ['amount_digits_x', 'amount_digits_y']
            },
            {
                id: 'amount_words',
                label: 'Montant (lettres)',
                x: record.data.amount_words_x || 15,
                y: record.data.amount_words_y || 50,
                width: record.data.amount_words_width || 140,
                height: 8,
                color: '#f39c12',
                fields: ['amount_words_x', 'amount_words_y', 'amount_words_width']
            },
            {
                id: 'location',
                label: 'Lieu',
                x: record.data.location_x || 15,
                y: record.data.location_y || 15,
                width: 50,
                height: 8,
                color: '#9b59b6',
                fields: ['location_x', 'location_y']
            },
            {
                id: 'signature',
                label: 'Signature',
                x: record.data.signature_x || 130,
                y: record.data.signature_y || 65,
                width: 30,
                height: 15,
                color: '#1abc9c',
                fields: ['signature_x', 'signature_y']
            }
        ];
    }

    /**
     * Configure les interactions (drag & drop)
     */
    setupInteractions() {
        if (!this.checkRef.el) return;

        this.checkRef.el.addEventListener('mousedown', this.onMouseDown.bind(this));
        document.addEventListener('mousemove', this.onMouseMove.bind(this));
        document.addEventListener('mouseup', this.onMouseUp.bind(this));
    }

    /**
     * Nettoie les écouteurs d'événements
     */
    cleanupInteractions() {
        document.removeEventListener('mousemove', this.onMouseMove.bind(this));
        document.removeEventListener('mouseup', this.onMouseUp.bind(this));
    }

    /**
     * Début du glisser
     */
    onMouseDown(event) {
        const rect = this.checkRef.el.getBoundingClientRect();
        const scale = this.getScale();
        const x = (event.clientX - rect.left) / scale;
        const y = (event.clientY - rect.top) / scale;

        // Trouver l'élément cliqué
        const element = this.findElementAt(x, y);
        
        if (element) {
            this.state.selectedElement = element;
            this.state.isDragging = true;
            this.dragOffset = {
                x: x - element.x,
                y: y - element.y
            };
            event.preventDefault();
        }
    }

    /**
     * Déplacement de la souris
     */
    onMouseMove(event) {
        if (!this.state.isDragging || !this.state.selectedElement) return;

        const rect = this.checkRef.el.getBoundingClientRect();
        const scale = this.getScale();
        let x = (event.clientX - rect.left) / scale - this.dragOffset.x;
        let y = (event.clientY - rect.top) / scale - this.dragOffset.y;

        // Snap to grid si activé
        if (this.state.snapToGrid) {
            x = Math.round(x / this.state.gridSize) * this.state.gridSize;
            y = Math.round(y / this.state.gridSize) * this.state.gridSize;
        }

        // Contraintes de position
        const checkWidth = this.props.record.data.check_width || 175;
        const checkHeight = this.props.record.data.check_height || 85;

        x = Math.max(0, Math.min(x, checkWidth - this.state.selectedElement.width));
        y = Math.max(0, Math.min(y, checkHeight - this.state.selectedElement.height));

        this.state.selectedElement.x = x;
        this.state.selectedElement.y = y;

        event.preventDefault();
    }

    /**
     * Fin du glisser - sauvegarde
     */
    async onMouseUp(event) {
        if (this.state.isDragging && this.state.selectedElement) {
            await this.savePosition(this.state.selectedElement);
            this.state.isDragging = false;
            
            this.notification.add(
                `Position de "${this.state.selectedElement.label}" mise à jour`,
                { type: 'success' }
            );
        }
    }

    /**
     * Trouve l'élément à une position donnée
     */
    findElementAt(x, y) {
        // Parcourir en ordre inverse pour avoir le dernier élément dessiné
        for (let i = this.state.elements.length - 1; i >= 0; i--) {
            const el = this.state.elements[i];
            if (x >= el.x && x <= el.x + el.width &&
                y >= el.y && y <= el.y + el.height) {
                return el;
            }
        }
        return null;
    }

    /**
     * Sauvegarde la position d'un élément
     */
    async savePosition(element) {
        const updates = {};
        
        // Mettre à jour les champs correspondants
        if (element.fields.includes('date_x')) updates.date_x = element.x;
        if (element.fields.includes('date_y')) updates.date_y = element.y;
        if (element.fields.includes('beneficiary_x')) updates.beneficiary_x = element.x;
        if (element.fields.includes('beneficiary_y')) updates.beneficiary_y = element.y;
        if (element.fields.includes('beneficiary_width')) updates.beneficiary_width = element.width;
        if (element.fields.includes('amount_digits_x')) updates.amount_digits_x = element.x;
        if (element.fields.includes('amount_digits_y')) updates.amount_digits_y = element.y;
        if (element.fields.includes('amount_words_x')) updates.amount_words_x = element.x;
        if (element.fields.includes('amount_words_y')) updates.amount_words_y = element.y;
        if (element.fields.includes('amount_words_width')) updates.amount_words_width = element.width;
        if (element.fields.includes('location_x')) updates.location_x = element.x;
        if (element.fields.includes('location_y')) updates.location_y = element.y;
        if (element.fields.includes('signature_x')) updates.signature_x = element.x;
        if (element.fields.includes('signature_y')) updates.signature_y = element.y;

        // Mettre à jour le record
        await this.props.record.update(updates);
    }

    /**
     * Calcule le facteur d'échelle pour l'affichage
     */
    getScale() {
        const checkWidth = this.props.record.data.check_width || 175;
        const checkHeight = this.props.record.data.check_height || 85;
        return this.state.zoom * 3; // 3 pixels par mm
    }

    /**
     * Change le niveau de zoom
     */
    changeZoom(delta) {
        this.state.zoom = Math.max(0.5, Math.min(2.0, this.state.zoom + delta));
    }

    /**
     * Réinitialise une position
     */
    async resetPosition(element) {
        // Valeurs par défaut
        const defaults = {
            'date': { x: 120, y: 15 },
            'beneficiary': { x: 15, y: 30 },
            'amount_digits': { x: 120, y: 45 },
            'amount_words': { x: 15, y: 50 },
            'location': { x: 15, y: 15 },
            'signature': { x: 130, y: 65 }
        };

        if (defaults[element.id]) {
            element.x = defaults[element.id].x;
            element.y = defaults[element.id].y;
            await this.savePosition(element);
            
            this.notification.add(
                `Position de "${element.label}" réinitialisée`,
                { type: 'info' }
            );
        }
    }

    /**
     * Bascule la grille
     */
    toggleGrid() {
        this.state.showGrid = !this.state.showGrid;
    }

    /**
     * Bascule le snap to grid
     */
    toggleSnap() {
        this.state.snapToGrid = !this.state.snapToGrid;
    }
    
    /**
     * Change l'opacité de l'image de fond
     */
    async changeImageOpacity(delta) {
        const record = this.props.record;
        let newOpacity = (record.data.check_image_opacity || 0.5) + delta;
        newOpacity = Math.max(0, Math.min(1, newOpacity));
        
        await record.update({ check_image_opacity: newOpacity });
        
        this.notification.add(
            `Opacité : ${Math.round(newOpacity * 100)}%`,
            { type: 'info' }
        );
    }
    
    /**
     * Upload une nouvelle image de chèque
     */
    async uploadCheckImage(event) {
        const file = event.target.files[0];
        if (!file) return;
        
        // Vérifier que c'est une image
        if (!file.type.startsWith('image/')) {
            this.notification.add(
                'Veuillez sélectionner un fichier image',
                { type: 'warning' }
            );
            return;
        }
        
        // Vérifier la taille (max 5 MB)
        if (file.size > 5 * 1024 * 1024) {
            this.notification.add(
                'L\'image est trop volumineuse (max 5 MB)',
                { type: 'warning' }
            );
            return;
        }
        
        // Lire le fichier
        const reader = new FileReader();
        reader.onload = async (e) => {
            const base64 = e.target.result.split(',')[1];
            await this.props.record.update({
                check_image: base64,
                check_image_filename: file.name
            });
            
            // Recharger l'image
            await this.loadPositions();
            
            this.notification.add(
                `Image "${file.name}" chargée avec succès`,
                { type: 'success' }
            );
        };
        reader.readAsDataURL(file);
    }
    
    /**
     * Supprimer l'image du chèque
     */
    async removeCheckImage() {
        await this.props.record.update({
            check_image: false,
            check_image_filename: false
        });
        
        this.checkImageUrl = null;
        
        this.notification.add(
            'Image supprimée',
            { type: 'info' }
        );
    }

    /**
     * Charge une configuration précise si disponible
     */
    async loadPreciseConfig() {
        const resId = this.props.record.resId;
        if (!resId) return;

        try {
            const result = await this.orm.call(
                'bank.check.template',
                'action_sync_with_precise_config',
                [resId]
            );
            
            await this.loadPositions();
            
            this.notification.add(
                'Configuration précise chargée avec succès',
                { type: 'success' }
            );
        } catch (error) {
            this.notification.add(
                'Aucune configuration précise disponible',
                { type: 'warning' }
            );
        }
    }
}

CheckPositionEditor.template = "bank_check_template.CheckPositionEditor";

// Enregistrer le widget
registry.category("fields").add("check_position_editor", {
    component: CheckPositionEditor,
});

export default CheckPositionEditor;
