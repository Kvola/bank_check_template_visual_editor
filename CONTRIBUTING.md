# 🤝 Guide de Contribution

Merci de votre intérêt pour contribuer à ce projet ! Ce document vous guidera à travers le processus de contribution.

## 📋 Table des matières

- [Code de conduite](#code-de-conduite)
- [Comment contribuer](#comment-contribuer)
- [Signaler un bug](#signaler-un-bug)
- [Proposer une fonctionnalité](#proposer-une-fonctionnalité)
- [Soumettre des modifications](#soumettre-des-modifications)
- [Style de code](#style-de-code)
- [Tests](#tests)
- [Documentation](#documentation)

## 🤗 Code de conduite

Ce projet adhère à un code de conduite. En participant, vous vous engagez à respecter ce code.

### Principes de base

- Soyez respectueux et inclusif
- Acceptez les critiques constructives
- Concentrez-vous sur ce qui est meilleur pour la communauté
- Faites preuve d'empathie envers les autres membres

## 🎯 Comment contribuer

Il existe plusieurs façons de contribuer :

### 1. Signaler des bugs
Trouvé un bug ? Signalez-le !

### 2. Proposer des fonctionnalités
Vous avez une idée ? Partagez-la !

### 3. Améliorer la documentation
La documentation peut toujours être améliorée

### 4. Écrire du code
Soumettez des pull requests avec vos modifications

### 5. Aider les autres
Répondez aux questions sur les issues

## 🐛 Signaler un bug

Avant de signaler un bug :

1. **Vérifiez les issues existantes** - Peut-être que quelqu'un l'a déjà signalé
2. **Mettez à jour** - Assurez-vous d'utiliser la dernière version
3. **Vérifiez la documentation** - Le problème pourrait être documenté

### Template de rapport de bug

```markdown
**Description du bug**
Description claire et concise du bug.

**Étapes pour reproduire**
1. Allez à '...'
2. Cliquez sur '...'
3. Faites défiler jusqu'à '...'
4. Voir l'erreur

**Comportement attendu**
Description claire de ce qui devrait se passer.

**Comportement actuel**
Description de ce qui se passe actuellement.

**Captures d'écran**
Si applicable, ajoutez des captures d'écran.

**Environnement:**
- OS: [ex: Ubuntu 22.04]
- Odoo version: [ex: 17.0]
- Navigateur: [ex: Chrome 120]
- Module version: [ex: 1.0.0]

**Logs**
```
Coller ici les logs pertinents
```

**Contexte additionnel**
Ajoutez tout contexte supplémentaire ici.
```

## 💡 Proposer une fonctionnalité

Avant de proposer une fonctionnalité :

1. **Vérifiez les issues existantes** - Peut-être déjà proposée
2. **Réfléchissez à la portée** - Est-ce dans le scope du projet ?
3. **Préparez votre proposition** - Soyez aussi détaillé que possible

### Template de proposition

```markdown
**Fonctionnalité proposée**
Description claire et concise de la fonctionnalité.

**Problème résolu**
Quel problème cette fonctionnalité résout-elle ?

**Solution proposée**
Comment cette fonctionnalité pourrait-elle être implémentée ?

**Alternatives envisagées**
Quelles alternatives avez-vous considérées ?

**Exemples d'utilisation**
Comment cette fonctionnalité serait-elle utilisée ?

**Impact**
- Utilisateurs affectés: [ex: tous les utilisateurs]
- Complexité: [Faible / Moyenne / Élevée]
- Priorité: [Basse / Moyenne / Haute]

**Ressources**
Liens vers des exemples, mockups, etc.
```

## 🔧 Soumettre des modifications

### Workflow Git

1. **Fork** le projet
2. **Clone** votre fork
   ```bash
   git clone https://github.com/votre-username/bank_check_template_visual_editor.git
   ```
3. **Créez une branche** pour votre fonctionnalité
   ```bash
   git checkout -b feature/ma-nouvelle-fonctionnalite
   ```
4. **Committez** vos modifications
   ```bash
   git commit -m "Ajout de ma nouvelle fonctionnalité"
   ```
5. **Push** vers votre fork
   ```bash
   git push origin feature/ma-nouvelle-fonctionnalite
   ```
6. **Ouvrez une Pull Request**

### Conventions de commit

Utilisez des messages de commit clairs et descriptifs :

```
type(scope): description courte

Description plus détaillée si nécessaire.

- Point de détail 1
- Point de détail 2

Fixes #123
```

**Types de commit:**
- `feat`: Nouvelle fonctionnalité
- `fix`: Correction de bug
- `docs`: Documentation
- `style`: Formatage, point-virgules manquants, etc.
- `refactor`: Refactorisation du code
- `test`: Ajout de tests
- `chore`: Maintenance

**Exemples:**
```bash
feat(editor): ajout du zoom par molette de souris
fix(save): correction de la sauvegarde automatique
docs(readme): mise à jour du guide d'installation
```

## 📝 Style de code

### Python

Suivez [PEP 8](https://www.python.org/dev/peps/pep-0008/) :

```python
# Bon
def calculate_position(element, x, y):
    """Calculate the final position of an element."""
    return {
        'x': x,
        'y': y,
        'element_id': element.id
    }

# Mauvais
def calc_pos(e,x,y):
    return {'x':x,'y':y,'element_id':e.id}
```

### JavaScript

Suivez [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript) :

```javascript
// Bon
const getElementPosition = (element) => {
    const { x, y } = element;
    return { x, y };
};

// Mauvais
function get_pos(el) {
    return {x:el.x,y:el.y}
}
```

### XML

```xml
<!-- Bon -->
<field name="template_name" 
       placeholder="ex: BGFI Bank"
       help="Nom du template"/>

<!-- Mauvais -->
<field name="template_name" placeholder="ex: BGFI Bank" help="Nom du template"/>
```

## 🧪 Tests

### Tests Python

```python
from odoo.tests import TransactionCase

class TestCheckPositionEditor(TransactionCase):
    def setUp(self):
        super().setUp()
        self.template = self.env['bank.check.template'].create({
            'template_name': 'Test Template',
            'bank_name': 'Test Bank',
        })
    
    def test_position_validation(self):
        """Test que les positions sont validées correctement"""
        self.template.write({
            'date_x': 120.0,
            'date_y': 15.0,
        })
        result = self.template.action_validate_positions()
        self.assertEqual(result['params']['type'], 'success')
```

### Tests JavaScript

```javascript
QUnit.test('Position calculation', function(assert) {
    const editor = new CheckPositionEditor();
    const position = editor.calculatePosition(100, 50);
    
    assert.equal(position.x, 100, 'X position is correct');
    assert.equal(position.y, 50, 'Y position is correct');
});
```

### Lancer les tests

```bash
# Tests Python
./odoo-bin -c odoo.conf -u bank_check_template_visual_editor --test-enable

# Tests JavaScript
# Ouvrir dans le navigateur : http://localhost:8069/web/tests
```

## 📚 Documentation

### Documentation du code

```python
def action_sync_with_precise_config(self):
    """
    Synchronise les positions du template avec la configuration précise.
    
    Cette méthode récupère la configuration précise de la banque
    et met à jour tous les champs de position du template.
    
    :raises UserError: Si la configuration précise n'est pas disponible
    :return: Notification de succès
    :rtype: dict
    """
    self.ensure_one()
    # ...
```

### Documentation des fonctionnalités

Documentez les nouvelles fonctionnalités dans :
- README.md (vue d'ensemble)
- VISUAL_GUIDE.md (guide visuel)
- Code (docstrings)
- Commentaires inline (si nécessaire)

## ✅ Checklist avant soumission

Avant de soumettre une Pull Request, vérifiez :

- [ ] Le code suit le style guide
- [ ] Les tests passent
- [ ] La documentation est à jour
- [ ] Les commits sont bien formatés
- [ ] Aucun code mort ou commenté
- [ ] Aucune dépendance inutile
- [ ] Le code fonctionne en production
- [ ] Les conflits sont résolus

## 🎖️ Reconnaissance des contributions

Tous les contributeurs seront :
- Listés dans le fichier CONTRIBUTORS.md
- Mentionnés dans les release notes
- Remerciés publiquement

## 📞 Contact

Des questions ? Contactez-nous :
- 📧 Email : dev@votreentreprise.com
- 💬 Discord : [Lien vers Discord]
- 🐦 Twitter : [@VotreCompte]

## 📜 Licence

En contribuant, vous acceptez que vos contributions soient sous licence LGPL-3, comme le reste du projet.

---

**Merci de contribuer ! 🙏**

Chaque contribution, petite ou grande, fait une différence.
