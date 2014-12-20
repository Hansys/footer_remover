# -*- coding: utf-8 -*-

# from openerp import models, fields, api

# class footer_remover(models.Model):
#     _name = 'footer_remover.footer_remover'

#     name = fields.Char()

from openerp import models, api

class FooterlessNotification(models.Model):
    _inherit = 'mail.notification'

    @api.model
    def get_signature_footer(self, user_id, res_model=None, res_id=None, context=None, user_signature=True):
        return ""
