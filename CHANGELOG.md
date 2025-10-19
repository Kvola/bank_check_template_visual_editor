# Changelog

Toutes les modifications notables de ce projet seront documentées dans ce fichier.

Le format est basé sur [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/),
et ce projet adhère au [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Non publié]

### À venir
- Raccourcis clavier (Ctrl+Z, Ctrl+Y, etc.)
- Historique des modifications avec annuler/rétablir
- Templates prédéfinis pour les banques populaires
- Mode sombre
- Guide interactif pour nouveaux utilisateurs
- Aperçu 3D du chèque
- Support multi-langues (EN, FR, ES)

## [1.0.0] - 2025-01-XX

### ✨ Ajouté
- Éditeur visuel complet avec glisser-déposer
- Positionnement interactif de tous les éléments du chèque :
  - Date
  - Bénéficiaire
  - Montant en chiffres
  - Montant en lettres
  - Lieu
  - Signature
- Grille de positionnement avec activation/désactivation
- Magnétisme automatique sur la grille (5mm)
- Zoom avant/arrière (50% à 200%)
- Panneau latéral avec liste des éléments
- Affichage des coordonnées en temps réel
- Sauvegarde automatique des positions
- Validation des positions (vérification des limites)
- Export des configurations au format JSON
- Import de configurations JSON
- Copie de positions entre templates
- Réinitialisation des positions (par élément ou globale)
- Intégration avec configurations précises existantes
- Aperçu du chèque avec positions actuelles
- Code couleur pour chaque type d'élément
- Responsive design (Desktop, Tablet, Mobile)
- Messages de notification pour feedback utilisateur
- Assistant de copie de positions (wizard)

### 🎨 Design
- Interface moderne et intuitive
- Palette de couleurs cohérente
- Animations fluides
- Éléments draggables stylisés
- Indicateurs visuels de sélection
- Grille semi-transparente

### 🔧 Technique
- Widget OWL personnalisé : `check_position_editor`
- Modèle Python étendu : `BankCheckTemplateVisualEditor`
- Vue XML enrichie avec nouvel onglet
- CSS optimisé avec animations
- Support complet Odoo 17.0
- Code modulaire et maintenable

### 📚 Documentation
- README complet en français
- Guide d'installation rapide
- Guide visuel avec diagrammes ASCII
- Fichier de sécurité et droits d'accès
- Exemples de code et d'utilisation

### 🔒 Sécurité
- Droits d'accès configurés (account.group_account_user)
- Validation des positions avant sauvegarde
- Vérification des limites du chèque
- Protection contre les positions invalides

### 🐛 Corrections
- Aucune (première version)

### ⚠️ Obsolète
- Aucun

### 🗑️ Supprimé
- Aucun

### 🔐 Sécurité
- Aucun problème de sécurité connu

---

## Format des versions

- **MAJOR** : Changements incompatibles avec l'API
- **MINOR** : Ajout de fonctionnalités rétrocompatibles
- **PATCH** : Corrections de bugs rétrocompatibles

## Types de changements

- `✨ Ajouté` : Nouvelles fonctionnalités
- `🔧 Modifié` : Changements de fonctionnalités existantes
- `⚠️ Obsolète` : Fonctionnalités bientôt supprimées
- `🗑️ Supprimé` : Fonctionnalités supprimées
- `🐛 Corrigé` : Corrections de bugs
- `🔐 Sécurité` : Corrections de vulnérabilités

---

**Mainteneur** : Votre Entreprise  
**Contact** : support@votreentreprise.com  
**Date de création** : Janvier 2025
