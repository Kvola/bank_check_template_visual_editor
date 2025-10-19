# 🎨 Présentation Visuelle - Éditeur de Positionnement de Chèques

## Interface de l'éditeur

```
┌─────────────────────────────────────────────────────────────────────────┐
│ 🎨 ÉDITEUR VISUEL DE POSITIONNEMENT                                      │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                           │
│  [Zoom +] [Zoom -]  [Grille ✓]  [Magnétisme ✓]   │
│                                                                           │
├──────────────────────────────────────┬──────────────────────────────────┤
│                                      │  📋 ÉLÉMENTS DU CHÈQUE           │
│  ┌────────────────────────────────┐ │                                   │
│  │                                │ │  ┌─────────────────────────────┐ │
│  │   ┌────────────┐   [Date]     │ │  │ 📅 Date                     │ │
│  │   │  Abidjan   │   12/01/2025 │ │  │ Position X: 120.0 mm        │ │
│  │   └────────────┘               │ │  │ Position Y: 15.0 mm         │ │
│  │                                │ │  │ [Réinitialiser]             │ │
│  │   [Bénéficiaire]               │ │  └─────────────────────────────┘ │
│  │   ENTREPRISE EXEMPLE SARL      │ │                                   │
│  │                                │ │  ┌─────────────────────────────┐ │
│  │                                │ │  │ 👤 Bénéficiaire             │ │
│  │   [Montant chiffres]           │ │  │ Position X: 15.0 mm         │ │
│  │   1 500 000 FCFA               │ │  │ Position Y: 30.0 mm         │ │
│  │                                │ │  │ Largeur: 140.0 mm           │ │
│  │   [Montant lettres]            │ │  │ [Réinitialiser]             │ │
│  │   Un million cinq cent...      │ │  └─────────────────────────────┘ │
│  │                                │ │                                   │
│  │                    [Signature] │ │  ┌─────────────────────────────┐ │
│  │                    ┌─────────┐ │ │  │ 💰 Montant (chiffres)       │ │
│  └────────────────────│─────────┘─┘ │  │ Position X: 120.0 mm        │ │
│         175 mm × 85 mm               │  │ Position Y: 45.0 mm         │ │
│                                      │  │ [Réinitialiser]             │ │
│                                      │  └─────────────────────────────┘ │
│                                      │                                   │
│                                      │  💡 AIDE                         │
│                                      │  • Cliquez et glissez           │
│                                      │  • Alignement automatique       │
│                                      │  • Sauvegarde automatique       │
│                                      │                                   │
└──────────────────────────────────────┴──────────────────────────────────┘
```

## Workflow d'utilisation

```
┌──────────────┐
│   DÉBUT      │
└──────┬───────┘
       │
       v
┌──────────────────────┐
│ Ouvrir un template   │
│ de chèque            │
└──────┬───────────────┘
       │
       v
┌──────────────────────┐
│ Cliquer sur onglet   │
│ "🎨 Éditeur Visuel"  │
└──────┬───────────────┘
       │
       v
┌──────────────────────┐
│ Activer grille et    │
│ magnétisme (optionel)│
└──────┬───────────────┘
       │
       v
┌──────────────────────┐
│ Sélectionner un      │
│ élément à positionner│
└──────┬───────────────┘
       │
       v
┌──────────────────────┐
│ Glisser l'élément    │
│ à la position voulue │
└──────┬───────────────┘
       │
       v
┌──────────────────────┐
│ Position sauvegardée │
│ automatiquement ✅   │
└──────┬───────────────┘
       │
       v
┌──────────────────────┐
│ Répéter pour chaque  │
│ élément              │
└──────┬───────────────┘
       │
       v
┌──────────────────────┐
│ Valider les positions│
└──────┬───────────────┘
       │
       v
┌──────────────┐
│   FIN        │
└──────────────┘
```

## États des éléments

### Élément normal
```
┌────────────────┐
│  Date          │ ← Label en haut
│                │
│  (120, 15) mm  │ ← Coordonnées
└────────────────┘
```

### Élément sélectionné
```
╔════════════════╗
║  Date          ║ ← Bordure plus épaisse
║                ║   + Ombre portée
║  (120, 15) mm  ║
╚════════════════╝
```

### Élément en cours de déplacement
```
┌ ─ ─ ─ ─ ─ ─ ─ ┐
│  Date          │ ← Semi-transparent
│                │   + Curseur "grabbing"
│  (125, 18) mm  │ ← Coordonnées en temps réel
└ ─ ─ ─ ─ ─ ─ ─ ┘
```

## Grille de positionnement

```
  0    5   10   15   20   25   30 ... 170  175 (mm)
  ┌────┬────┬────┬────┬────┬────┬────────┬────┐
0 │    │    │    │    │    │    │        │    │
  ├────┼────┼────┼────┼────┼────┼────────┼────┤
5 │    │    │ L  │    │    │    │        │ D  │
  ├────┼────┼────┼────┼────┼────┼────────┼────┤
10│    │    │    │    │    │    │        │    │
  ├────┼────┼────┼────┼────┼────┼────────┼────┤
15│    │    │    │    │    │    │        │    │
  ├────┼────┼────┼────┼────┼────┼────────┼────┤
20│    │    │    │    │    │    │        │    │
  └────┴────┴────┴────┴────┴────┴────────┴────┘

L = Lieu
D = Date
B = Bénéficiaire
MC = Montant Chiffres
ML = Montant Lettres
S = Signature
```

## Codes couleur des éléments

| Élément              | Couleur  | Code Hex |
|---------------------|----------|----------|
| 📅 Date             | Bleu     | #3498db  |
| 👤 Bénéficiaire     | Vert     | #2ecc71  |
| 💰 Montant chiffres | Rouge    | #e74c3c  |
| 📝 Montant lettres  | Orange   | #f39c12  |
| 📍 Lieu             | Violet   | #9b59b6  |
| ✍️ Signature        | Turquoise| #1abc9c  |

## Exemple de chèque positionné

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Abidjan, le                               12 janvier 2025         │ ← Date
│                                                                     │
│                                                                     │
│  Payez contre ce chèque                                            │
│                                                                     │
│  À    ENTREPRISE EXEMPLE SARL                                      │ ← Bénéficiaire
│  ───────────────────────────────────────────────────────────────   │
│                                                                     │
│  La somme de : Un million cinq cent mille francs CFA              │ ← Montant lettres
│  ────────────────────────────────────────────────────────────────  │
│                                                                     │
│                                               1 500 000 FCFA       │ ← Montant chiffres
│                                                                     │
│                                                                     │
│                                                     ┌─────────┐     │
│                                                     │         │     │ ← Signature
│                                                     └─────────┘     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
     175 mm
```

## Actions disponibles

### Barre d'outils
```
[🔍 Zoom +] [🔍 Zoom -]  |  [📐 Grille] [🧲 Magnétisme]
```

### Menu contextuel (clic droit)
```
┌─────────────────────┐
│ Copier position     │
│ Coller position     │
├─────────────────────┤
│ Réinitialiser       │
│ Supprimer           │
├─────────────────────┤
│ Propriétés...       │
└─────────────────────┘
```

### Panneau d'actions
```
┌──────────────────────────────┐
│  ACTIONS RAPIDES             │
├──────────────────────────────┤
│  [🔄] Réinitialiser tout     │
│  [📋] Copier depuis...       │
│  [📤] Exporter JSON          │
│  [📥] Importer JSON          │
│  [✅] Valider positions      │
│  [👁️] Aperçu                 │
└──────────────────────────────┘
```

## Format d'export JSON

```json
{
  "template_name": "BGFI Bank - Standard",
  "bank_name": "BGFI Bank",
  "bank_code": "BGFI_BARRE",
  "check_width": 175.0,
  "check_height": 85.0,
  "positions": {
    "date": {
      "x": 120.0,
      "y": 15.0
    },
    "beneficiary": {
      "x": 15.0,
      "y": 30.0,
      "width": 140.0
    },
    "amount_digits": {
      "x": 120.0,
      "y": 45.0
    },
    "amount_words": {
      "x": 15.0,
      "y": 50.0,
      "width": 140.0
    },
    "location": {
      "x": 15.0,
      "y": 15.0
    },
    "signature": {
      "x": 130.0,
      "y": 65.0
    }
  },
  "formatting": {
    "font_name": "Helvetica",
    "font_size": 10,
    "currency_symbol": "FCFA"
  }
}
```

## Notifications système

### Succès
```
┌────────────────────────────────┐
│ ✅ Position sauvegardée        │
│ La date a été déplacée à       │
│ (125, 18) mm                   │
└────────────────────────────────┘
```

### Avertissement
```
┌────────────────────────────────┐
│ ⚠️ Position hors limites       │
│ L'élément dépasse les bords    │
│ du chèque. Ajustez la position.│
└────────────────────────────────┘
```

### Information
```
┌────────────────────────────────┐
│ ℹ️ Grille activée              │
│ Taille de grille: 5 mm         │
│ Magnétisme actif               │
└────────────────────────────────┘
```

## Responsive Design

### Desktop (>1200px)
```
┌────────────────────────────────────────────┐
│  Éditeur principal   │  Panneau latéral    │
│  (Canvas large)      │  (300px fixe)       │
└────────────────────────────────────────────┘
```

### Tablet (768-1200px)
```
┌──────────────────────────┐
│  Éditeur principal       │
│  (Canvas adapté)         │
├──────────────────────────┤
│  Panneau latéral         │
│  (Pleine largeur)        │
└──────────────────────────┘
```

### Mobile (<768px)
```
┌────────────────┐
│  Barre outils  │
├────────────────┤
│  Canvas        │
│  (Scrollable)  │
├────────────────┤
│  Liste         │
│  éléments      │
└────────────────┘
```

---

**Créé avec ❤️ pour faciliter le positionnement des chèques**
