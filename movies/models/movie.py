from odoo import models, fields, api

class Movie(models.Model):
    _name = 'mt.movie'
    _description = 'Movies'
    name = fields.Char ('Name')
    review = fields.Text ('Review')
    image = fields.Binary()
    attachment = fields.Binary()

    genre_ids = fields.Many2many('mt.genre', string='Genre') 
    category_ids = fields.Many2many('mt.category', string='Category') 
    country_id = fields.Many2one('res.country',string='Country')
    active = fields.Boolean(default=True)