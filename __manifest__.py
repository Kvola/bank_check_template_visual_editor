# -*- coding: utf-8 -*-
{
    'name': 'Bank Check Template - Éditeur Visuel',
    'version': '17.0.1.0.0',
    'category': 'Accounting/Accounting',
    'summary': 'Éditeur visuel pour positionner les éléments des chèques bancaires',
    'description': """
Éditeur Visuel de Positionnement pour Chèques Bancaires
========================================================

Ce module étend le module bank_check_template en ajoutant un éditeur visuel
interactif pour positionner les éléments des chèques.

Fonctionnalités principales:
-----------------------------
* 🎨 Éditeur visuel avec glisser-déposer
* 📊 Aperçu en temps réel du chèque
* 🖱️ Positionnement intuitif par drag & drop
* 📏 Grille d'alignement et magnétisme
* 💾 Sauvegarde automatique des positions
* 📤 Export/Import des configurations (JSON)
* 🔄 Copie de positions entre templates
* ✅ Validation des positions
* 🔍 Zoom et navigation
* 📐 Redimensionnement des zones

Utilisation:
-----------
1. Ouvrir un modèle de chèque
2. Cliquer sur l'onglet "🎨 Éditeur Visuel"
3. Glisser-déposer les éléments pour les positionner
4. Les positions sont automatiquement sauvegardées

Configuration:
-------------
Aucune configuration nécessaire. Le module s'intègre automatiquement
au module bank_check_template existant.

Notes techniques:
----------------
* Compatible Odoo 17.0+
* Utilise OWL (Odoo Web Library) pour le JavaScript
* Widget personnalisé : check_position_editor
* Responsive et optimisé pour tous les écrans
    """,
    'author': 'Votre Entreprise',
    'website': 'https://www.votresite.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'account',
        'web',
        'check_printing_generic',
        'payment_request_validation',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bank_check_template_visual_editor_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'bank_check_template_visual_editor/static/src/js/check_position_editor.js',
            'bank_check_template_visual_editor/static/src/xml/check_position_editor_template.xml',
            'bank_check_template_visual_editor/static/src/css/check_position_editor.css',
        ],
    },
    'images': [
        'static/description/icon.png',
        'static/description/banner.png',
        'static/description/screenshot_editor.png',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': 'post_init_hook',
}
