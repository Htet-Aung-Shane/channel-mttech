from odoo import models, fields, api


class ContactExt(models.Model):
    _inherit = 'res.partner' 

    mt_company_id = fields.Many2one('mt.company')