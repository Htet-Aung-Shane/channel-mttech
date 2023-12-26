from odoo import models, fields, api
import datetime


class Service(models.Model):
    _name = "mt.service"
    _description = "Service Type"

    no = fields.Char (
        'Application Number', size=16, copy=False,
        readonly=True, store=True,
        default=lambda self:
        self.env['ir.sequence'].next_by_code('mt.sale'))
    contact_id = fields.Many2one("res.partner", string="Client Name")
    domain_name = fields.Char("Domain Name")
    service_type_id = fields.Many2one("mt.service.type", string="Service Type")
    service_date = fields.Date(
        string="Service Date", default=fields.Date.today(), required=True
    )
    service_charges = fields.Float('Service Charges')
    update_charges = fields.Float('Update Charges')
    update_date = fields.Date(string='Update Date', required=False)
    unit = fields.Integer('Unit')
    active = fields.Boolean(
        default=True,
        help="The active field allows you to hide the category without removing it.",
    )
