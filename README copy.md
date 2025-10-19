# 🎨 Éditeur Visuel pour Chèques Bancaires Odoo

Module Odoo pour positionner visuellement les éléments des chèques bancaires par glisser-déposer.

![Version](https://img.shields.io/badge/version-17.0.1.0.0-blue.svg)
![Odoo](https://img.shields.io/badge/Odoo-17.0-purple.svg)
![License](https://img.shields.io/badge/license-LGPL--3-green.svg)

## 📋 Présentation

Ce module étend le module `bank_check_template` en ajoutant un éditeur visuel interactif qui permet de positionner les éléments du chèque (date, bénéficiaire, montant, etc.) par simple glisser-déposer au lieu de saisir manuellement les coordonnées X/Y.

## ✨ Fonctionnalités

### 🎯 Positionnement Visuel
- **Glisser-déposer** : Déplacez les éléments directement sur le canvas du chèque
- **Aperçu en temps réel** : Voyez immédiatement où seront positionnés les éléments
- **Coordonnées automatiques** : Les positions X/Y sont calculées automatiquement
- **Sauvegarde automatique** : Chaque déplacement est sauvegardé instantanément

### 📏 Outils d'Alignement
- **Grille de positionnement** : Grille visuelle pour un alignement précis
- **Magnétisme** : Les éléments s'alignent automatiquement sur la grille
- **Zoom** : Zoom avant/arrière pour un positionnement précis
- **Règles visuelles** : Affichage des dimensions du chèque

### 🔧 Fonctionnalités Avancées
- **Export/Import JSON** : Sauvegardez et partagez vos configurations
- **Copie de positions** : Copiez les positions d'un template à un autre
- **Validation** : Vérification automatique que les éléments sont dans les limites
- **Réinitialisation** : Retour aux positions par défaut en un clic
- **Configuration précise** : Intégration avec les configs bancaires précises

## 📦 Installation

### Prérequis
- Odoo 17.0 ou supérieur
- Module `account` (comptabilité de base)
- Module `bank_check_template` (si applicable)

### Étapes d'installation

1. **Télécharger le module**
   ```bash
   cd /path/to/odoo/addons
   git clone [url_du_repo] bank_check_template_visual_editor
   ```

2. **Installer les dépendances** (si nécessaire)
   ```bash
   pip install -r requirements.txt
   ```

3. **Redémarrer le serveur Odoo**
   ```bash
   sudo systemctl restart odoo
   # ou
   ./odoo-bin -c odoo.conf --stop-after-init -u all
   ```

4. **Activer le mode développeur**
   - Paramètres → Activer le mode développeur

5. **Mettre à jour la liste des apps**
   - Apps → Mettre à jour la liste des apps

6. **Installer le module**
   - Recherchez "Bank Check Template - Éditeur Visuel"
   - Cliquez sur Installer

## 🚀 Utilisation

### Ouvrir l'éditeur visuel

#### Méthode 1 : Depuis un template existant
1. Allez dans **Comptabilité → Configuration → Modèles de chèques**
2. Ouvrez un template
3. Cliquez sur l'onglet **🎨 Éditeur Visuel**

#### Méthode 2 : Depuis la vue Kanban
1. Allez dans **Comptabilité → Configuration → Modèles de chèques**
2. Cliquez sur le bouton **Éditeur** sur une carte

#### Méthode 3 : Bouton dans le header
1. Ouvrez un template
2. Cliquez sur **Éditeur Visuel** dans le header

### Positionner les éléments

1. **Sélectionner un élément**
   - Cliquez sur l'élément dans le canvas
   - L'élément sélectionné s'affiche avec une bordure plus épaisse

2. **Déplacer un élément**
   - Cliquez et maintenez sur l'élément
   - Glissez-le à la position souhaitée
   - Relâchez pour sauvegarder

3. **Utiliser la grille**
   - Activez **Grille** pour voir la grille d'alignement
   - Activez **Magnétisme** pour aligner automatiquement sur la grille

4. **Zoomer**
   - Cliquez sur **Zoom +** / **Zoom -**
   - Ou utilisez la molette de la souris

### Panneau latéral

Le panneau latéral affiche :
- **Liste des éléments** avec leurs coordonnées actuelles
- **Bouton Réinitialiser** pour chaque élément
- **Aide** avec les instructions rapides

### Actions rapides

- **Réinitialiser toutes les positions** : Retour aux valeurs par défaut
- **Copier depuis un autre template** : Importer les positions d'un autre template
- **Exporter les positions** : Télécharger la configuration en JSON
- **Valider** : Vérifier que les positions sont correctes
- **Aperçu** : Voir un aperçu du chèque

## 🎨 Éléments positionnables

| Élément | Description | Couleur |
|---------|-------------|---------|
| 📅 Date | Position de la date | Bleu |
| 👤 Bénéficiaire | Nom du bénéficiaire | Vert |
| 💰 Montant (chiffres) | Montant en chiffres | Rouge |
| 📝 Montant (lettres) | Montant en toutes lettres | Orange |
| 📍 Lieu | Lieu d'émission | Violet |
| ✍️ Signature | Zone de signature | Turquoise |

## 🔧 Configuration

### Dimensions du chèque

Par défaut, les dimensions sont :
- **Largeur** : 175 mm (standard France/CI)
- **Hauteur** : 85 mm

Vous pouvez les modifier dans l'onglet **Dimensions**.

### Grille

Paramètres de la grille (modifiable dans le code) :
- **Taille de la grille** : 5 mm
- **Couleur** : Gris clair (#e0e0e0)

### Positions par défaut

| Élément | X (mm) | Y (mm) |
|---------|--------|--------|
| Date | 120 | 15 |
| Bénéficiaire | 15 | 30 |
| Montant (chiffres) | 120 | 45 |
| Montant (lettres) | 15 | 50 |
| Lieu | 15 | 15 |
| Signature | 130 | 65 |

## 📤 Export/Import

### Exporter une configuration

1. Ouvrez un template
2. Allez dans l'onglet **Éditeur Visuel**
3. Cliquez sur **Exporter les positions (JSON)**
4. Le fichier JSON est téléchargé

### Importer une configuration

Utilisez la méthode `action_import_positions` depuis le code Python :

```python
self.env['bank.check.template'].action_import_positions(json_data)
```

## 🛠️ Développement

### Structure du module

```
bank_check_template_visual_editor/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   └── bank_check_template_visual_editor.py
├── views/
│   └── bank_check_template_visual_editor_views.xml
├── security/
│   └── ir.model.access.csv
├── static/
│   ├── src/
│   │   ├── js/
│   │   │   └── check_position_editor.js
│   │   ├── css/
│   │   │   └── check_position_editor.css
│   │   └── xml/
│   │       └── check_position_editor_template.xml
│   └── description/
│       ├── icon.png
│       └── banner.png
└── README.md
```

### Technologies utilisées

- **Backend** : Python, Odoo ORM
- **Frontend** : OWL (Odoo Web Library), JavaScript ES6
- **Styles** : CSS3, Bootstrap
- **Format de données** : JSON

### Widget personnalisé

Le widget `check_position_editor` est enregistré dans le registre Odoo :

```javascript
registry.category("fields").add("check_position_editor", {
    component: CheckPositionEditor,
});
```

## 🐛 Dépannage

### Le widget ne s'affiche pas

1. Vérifiez que les assets sont bien chargés :
   - Inspectez la console du navigateur
   - Vérifiez dans Network → JS/CSS

2. Videz le cache :
   ```bash
   ./odoo-bin -c odoo.conf --update=bank_check_template_visual_editor
   ```

3. Régénérez les assets :
   - Mode développeur → Assets → Régénérer

### Les positions ne se sauvegardent pas

1. Vérifiez les droits d'accès :
   - L'utilisateur doit avoir les droits `account.group_account_user`

2. Vérifiez les logs Odoo :
   ```bash
   tail -f /var/log/odoo/odoo-server.log
   ```

### L'éditeur est lent

1. Réduisez le zoom
2. Désactivez temporairement la grille
3. Vérifiez les performances du navigateur

## 📝 Changelog

### Version 1.0.0 (2025-01-XX)
- ✨ Première version
- 🎨 Éditeur visuel complet
- 📏 Grille et magnétisme
- 💾 Sauvegarde automatique
- 📤 Export/Import JSON

## 🤝 Support

Pour toute question ou problème :
- 📧 Email : support@votreentreprise.com
- 🐛 Issues : [GitHub Issues]
- 📚 Documentation : [Wiki]

## 📄 Licence

Ce module est sous licence LGPL-3.

## 👨‍💻 Auteur

**Votre Entreprise**
- Website : https://www.votresite.com
- Email : contact@votreentreprise.com

## 🙏 Remerciements

- Communauté Odoo
- Contributeurs du module bank_check_template

---

**Fait avec ❤️ pour la communauté Odoo**
