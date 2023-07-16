from odoo import models, fields, api

class Student(models.Model):
    _name = 'mt.cast'
    _description = 'Cast' 

    name = fields.Char('Name')
    dob = fields.Date('Birth Date')    
    image = fields.Binary()
    country_id = fields.Many2one('res.country',string='Country')
    active = fields.Boolean(default=True)
    gender = fields.Selection(
        selection=[
            ('default', 'Default'), ('male', 'Male'), ('female', 'Female'), ('LGBTQ', 'LGBTQ'), ('rather not to say', 'Rather Not To Say')], default='default')
