# -*- coding: utf-8 -*-

from . import models

def post_init_hook(env):
    """Hook exécuté après l'installation du module"""
    import logging
    _logger = logging.getLogger(__name__)
    
    try:
        # Activer l'éditeur visuel pour tous les templates existants
        templates = env['bank.check.template'].search([])
        if templates:
            templates.write({'enable_visual_editor': True})
            _logger.info("✅ Éditeur visuel activé pour %s templates", len(templates))
        else:
            _logger.info("ℹ️ Aucun template trouvé, l'éditeur sera activé lors de la création")
    except Exception as e:
        _logger.warning("⚠️ Impossible d'activer l'éditeur visuel : %s", str(e))
        # Ne pas bloquer l'installation si le modèle parent n'existe pas encore
