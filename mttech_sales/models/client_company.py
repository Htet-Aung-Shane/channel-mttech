from odoo import models, fields, api


class Company(models.Model):
    _name = "mt.company"
    _description = "Company"

    active = fields.Boolean(
        default=True,
        help="The active field allows you to hide the category without removing it.",
    )
    name = fields.Char("Company Name")
    image = fields.Binary()
    email = fields.Char("Email")
    phone_no = fields.Char("Phone No")