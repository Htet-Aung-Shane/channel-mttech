from odoo import models, fields, api
from random import randint

class ServiceType(models.Model):
    _name = 'mt.service.type'
    _description = 'Service Type'

    def _get_default_color(self):
        return randint(1, 11)
    name = fields.Char ('Name')
    color = fields.Integer(string='Color', default=_get_default_color)
    active = fields.Boolean(default=True, help="The active field allows you to hide the category without removing it.")



