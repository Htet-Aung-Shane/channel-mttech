from odoo import models, fields, api
import datetime


class Service(models.Model):
    _name = "mt.service"
    _description = "Service Type"

    name = fields.Char("Name")
    contact_id = fields.Many2one("res.partner", string="Client Name")
    service_type_id = fields.Many2one("mt.service.type", string="Service Type")
    service_date = fields.Datetime(
        string="Service Date", default=fields.Datetime.now, required=True
    )
    service_charges = fields.Float('Service Charges')
    update_charges = fields.Float('Update Charges')
    update_date = fields.Datetime(string='Update Date', required=False)
    unit = fields.Integer('Unit')
    active = fields.Boolean(
        default=True,
        help="The active field allows you to hide the category without removing it.",
    )
