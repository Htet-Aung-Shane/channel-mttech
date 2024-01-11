from odoo import models, fields, api


class ContactExt(models.Model):
    _inherit = 'res.partner' 

    mt_company_id = fields.Many2one('mt.company')

    @api.onchange('mt_company_id')
    def _onchange_company(self):
        if self.mt_company_id.phone_no:
            self.phone = self.mt_company_id.phone_no
        if self.mt_company_id.email:
            self.email = self.mt_company_id.email
        if self.mt_company_id.country_id:
            self.country_id = self.mt_company_id.country_id
        if self.mt_company_id.city_id:
            self.city = self.mt_company_id.city_id.name
        print('onchange works>>>',self.mt_company_id.phone_no)