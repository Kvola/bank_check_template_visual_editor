from odoo import models, fields, api, _
from odoo.exceptions import UserError

class BankCheckTemplateVisualEditor(models.Model):
    """Extension pour l'éditeur visuel de positionnement"""
    
    _inherit = 'bank.check.template'
    
    # Champ pour l'éditeur visuel (widget personnalisé)
    visual_editor_data = fields.Text(
        'Données éditeur visuel',
        help="Données JSON pour l'éditeur visuel de positionnement",
        default='{}',
    )
    
    # Champ calculé pour activer l'éditeur visuel
    enable_visual_editor = fields.Boolean(
        'Activer éditeur visuel',
        default=True,
        help="Active l'éditeur visuel de positionnement des éléments"
    )
    
    # Image du chèque pour positionnement visuel
    check_image = fields.Binary(
        'Image du chèque',
        help="Uploadez une image d'un chèque vierge pour positionner visuellement les éléments",
        attachment=True
    )
    
    check_image_filename = fields.Char(
        'Nom du fichier image',
        help="Nom du fichier de l'image du chèque"
    )
    
    check_image_opacity = fields.Float(
        'Opacité de l\'image',
        default=0.5,
        help="Opacité de l'image de fond (0.0 = transparente, 1.0 = opaque)"
    )
    
    def action_open_visual_editor(self):
        """
        Ouvre l'éditeur visuel dans une vue formulaire dédiée
        """
        self.ensure_one()
        
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'bank.check.template',
            'res_id': self.id,
            'view_mode': 'form',
            'view_id': self.env.ref('bank_check_template_visual_editor.view_bank_check_template_visual_editor').id,
            'target': 'current',
            'context': {
                'form_view_initial_mode': 'edit',
            }
        }
    
    def action_preview_check(self):
        """
        Génère un aperçu PDF du chèque avec les positions actuelles
        """
        self.ensure_one()
        
        # Créer un chèque temporaire pour l'aperçu avec des données réalistes
        preview_check = self.env['check.printing'].create({
            'check_number': f'PREVIEW-{self.id}',
            'date': fields.Date.today(),
            'beneficiary': 'SOCIÉTÉ EXEMPLE SARL',
            'amount': 1500000.00,
            'memo': f'Aperçu du modèle {self.template_name}',
            'bank_template_id': self.id,
            'number_generation_method': 'manual',
            'state': 'draft',
        })
        
        try:
            # Générer le PDF du chèque d'aperçu
            pdf_data = preview_check._generate_check_pdf()
            preview_check.write({
                'pdf_file': pdf_data,
                'pdf_filename': f'Apercu_{self.template_name}.pdf',
                'state': 'ready'
            })
            
            # Retourner l'action pour télécharger/visualiser le PDF
            return {
                'type': 'ir.actions.act_window',
                'name': _('Aperçu du chèque - %s') % self.template_name,
                'res_model': 'check.printing',
                'res_id': preview_check.id,
                'view_mode': 'form',
                'target': 'new',
                'context': {
                    'is_preview': True,
                    'form_view_initial_mode': 'readonly',
                },
                'flags': {
                    'mode': 'readonly',
                }
            }
            
        except Exception as e:
            # En cas d'erreur, supprimer le chèque temporaire et afficher l'erreur
            preview_check.unlink()
            raise UserError(_(
                'Erreur lors de la génération de l\'aperçu:\n\n%s\n\n'
                'Vérifiez que toutes les positions sont correctement configurées.'
            ) % str(e))
    
    def action_copy_positions_from(self):
        """
        Copie les positions depuis un autre template
        """
        self.ensure_one()
        
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'bank.check.template.copy.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_target_template_id': self.id,
            }
        }
    
    def action_export_positions(self):
        """
        Exporte les positions au format JSON
        """
        self.ensure_one()
        
        positions = {
            'template_name': self.template_name,
            'bank_name': self.bank_name,
            'bank_code': self.bank_code,
            'check_width': self.check_width,
            'check_height': self.check_height,
            'positions': {
                'date': {'x': self.date_x, 'y': self.date_y},
                'beneficiary': {
                    'x': self.beneficiary_x,
                    'y': self.beneficiary_y,
                    'width': self.beneficiary_width
                },
                'amount_digits': {
                    'x': self.amount_digits_x,
                    'y': self.amount_digits_y
                },
                'amount_words': {
                    'x': self.amount_words_x,
                    'y': self.amount_words_y,
                    'width': self.amount_words_width
                },
                'location': {'x': self.location_x, 'y': self.location_y},
                'signature': {'x': self.signature_x, 'y': self.signature_y},
            },
            'formatting': {
                'font_name': self.font_name,
                'font_size': self.font_size,
                'currency_symbol': self.currency_symbol,
            }
        }
        
        import json
        json_data = json.dumps(positions, indent=2, ensure_ascii=False)
        
        # Créer un attachement temporaire
        attachment = self.env['ir.attachment'].create({
            'name': f'{self.template_name}_positions.json',
            'datas': json_data.encode('utf-8'),
            'mimetype': 'application/json',
            'res_model': self._name,
            'res_id': self.id,
        })
        
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{attachment.id}?download=true',
            'target': 'self',
        }
    
    @api.model
    def action_import_positions(self, json_data):
        """
        Importe les positions depuis un fichier JSON
        """
        import json
        
        try:
            data = json.loads(json_data)
            
            positions = data.get('positions', {})
            formatting = data.get('formatting', {})
            
            # Créer ou mettre à jour le template
            values = {
                'template_name': data.get('template_name'),
                'bank_name': data.get('bank_name'),
                'bank_code': data.get('bank_code'),
                'check_width': data.get('check_width', 175.0),
                'check_height': data.get('check_height', 85.0),
            }
            
            # Positions
            if 'date' in positions:
                values['date_x'] = positions['date']['x']
                values['date_y'] = positions['date']['y']
            
            if 'beneficiary' in positions:
                values['beneficiary_x'] = positions['beneficiary']['x']
                values['beneficiary_y'] = positions['beneficiary']['y']
                values['beneficiary_width'] = positions['beneficiary'].get('width', 140.0)
            
            if 'amount_digits' in positions:
                values['amount_digits_x'] = positions['amount_digits']['x']
                values['amount_digits_y'] = positions['amount_digits']['y']
            
            if 'amount_words' in positions:
                values['amount_words_x'] = positions['amount_words']['x']
                values['amount_words_y'] = positions['amount_words']['y']
                values['amount_words_width'] = positions['amount_words'].get('width', 140.0)
            
            if 'location' in positions:
                values['location_x'] = positions['location']['x']
                values['location_y'] = positions['location']['y']
            
            if 'signature' in positions:
                values['signature_x'] = positions['signature']['x']
                values['signature_y'] = positions['signature']['y']
            
            # Formatage
            values.update({
                'font_name': formatting.get('font_name', 'Helvetica'),
                'font_size': formatting.get('font_size', 10),
                'currency_symbol': formatting.get('currency_symbol', 'FCFA'),
            })
            
            template = self.create(values)
            
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('Import réussi'),
                    'message': _('Template "%s" créé avec succès') % template.template_name,
                    'type': 'success',
                }
            }
            
        except Exception as e:
            raise UserError(_('Erreur lors de l\'import: %s') % str(e))
    
    def action_reset_all_positions(self):
        """
        Réinitialise toutes les positions aux valeurs par défaut
        """
        self.ensure_one()
        
        default_values = {
            'date_x': 120.0,
            'date_y': 15.0,
            'beneficiary_x': 15.0,
            'beneficiary_y': 30.0,
            'beneficiary_width': 140.0,
            'amount_digits_x': 120.0,
            'amount_digits_y': 45.0,
            'amount_words_x': 15.0,
            'amount_words_y': 50.0,
            'amount_words_width': 140.0,
            'location_x': 15.0,
            'location_y': 15.0,
            'signature_x': 130.0,
            'signature_y': 65.0,
        }
        
        self.write(default_values)
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Réinitialisation'),
                'message': _('Toutes les positions ont été réinitialisées'),
                'type': 'info',
            }
        }
    
    def action_validate_positions(self):
        """
        Valide que les positions sont dans les limites du chèque
        """
        self.ensure_one()
        
        errors = []
        
        # Vérifier que les éléments ne dépassent pas
        if self.date_x > self.check_width or self.date_y > self.check_height:
            errors.append(_('La position de la date dépasse les limites du chèque'))
        
        if self.beneficiary_x + self.beneficiary_width > self.check_width:
            errors.append(_('Le bénéficiaire dépasse la largeur du chèque'))
        
        if self.beneficiary_y > self.check_height:
            errors.append(_('Le bénéficiaire dépasse la hauteur du chèque'))
        
        if self.amount_digits_x > self.check_width or self.amount_digits_y > self.check_height:
            errors.append(_('La position du montant en chiffres dépasse les limites'))
        
        if self.amount_words_x + self.amount_words_width > self.check_width:
            errors.append(_('Le montant en lettres dépasse la largeur du chèque'))
        
        if errors:
            message = '\n'.join(['• ' + e for e in errors])
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('⚠️ Erreurs de validation'),
                    'message': message,
                    'type': 'warning',
                    'sticky': True,
                }
            }
        else:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': _('✅ Validation réussie'),
                    'message': _('Toutes les positions sont correctes'),
                    'type': 'success',
                }
            }

class BankCheckTemplateCopyWizard(models.TransientModel):
    """Assistant pour copier les positions d'un template à un autre"""
    
    _name = 'bank.check.template.copy.wizard'
    _description = 'Assistant de copie de positions'

    source_template_id = fields.Many2one(
        'bank.check.template',
        string='Template source',
        required=True,
        help="Template depuis lequel copier les positions"
    )
    
    target_template_id = fields.Many2one(
        'bank.check.template',
        string='Template cible',
        required=True,
        help="Template vers lequel copier les positions"
    )
    
    def action_copy_positions(self):
        """Copie les positions du template source vers la cible"""
        self.ensure_one()
        
        if not self.source_template_id or not self.target_template_id:
            raise UserError(_('Veuillez sélectionner les templates source et cible'))
        
        # Copier toutes les positions
        self.target_template_id.write({
            'date_x': self.source_template_id.date_x,
            'date_y': self.source_template_id.date_y,
            'beneficiary_x': self.source_template_id.beneficiary_x,
            'beneficiary_y': self.source_template_id.beneficiary_y,
            'beneficiary_width': self.source_template_id.beneficiary_width,
            'amount_digits_x': self.source_template_id.amount_digits_x,
            'amount_digits_y': self.source_template_id.amount_digits_y,
            'amount_words_x': self.source_template_id.amount_words_x,
            'amount_words_y': self.source_template_id.amount_words_y,
            'amount_words_width': self.source_template_id.amount_words_width,
            'location_x': self.source_template_id.location_x,
            'location_y': self.source_template_id.location_y,
            'signature_x': self.source_template_id.signature_x,
            'signature_y': self.source_template_id.signature_y,
        })
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('✅ Copie réussie'),
                'message': _('Les positions ont été copiées vers %s') % self.target_template_id.template_name,
                'type': 'success',
            }
        }