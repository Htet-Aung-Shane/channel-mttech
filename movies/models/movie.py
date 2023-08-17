from odoo import models, fields, api

class Movie(models.Model):
    _name = 'mt.movie'
    _description = 'Movies'
    no = fields.Char (
        'Application Number', size=16, copy=False,
        readonly=True, store=True,
        default=lambda self:
        self.env['ir.sequence'].next_by_code('mt.movie'))
    name = fields.Char ('Name')
    review = fields.Text ('Review')
    image = fields.Binary()
    attachment = fields.Binary()

    partner_id = fields.Many2one('res.partner',string='Publisher', compute="compute_publisher", store=True)
    genre_ids = fields.Many2many('mt.genre', string='Genre') 
    category_ids = fields.Many2many('mt.category', string='Category') 
    country_id = fields.Many2many('res.country',string='Country')
    tag_id = fields.Many2one('mt.tag',string='Movie Type')
    cast_ids = fields.Many2many('mt.cast', string='Casts')
    link_ids = fields.One2many('mt.link','link_id',string='Movie Link')
    additional_ids = fields.One2many('mt.additional','additional_id',string='Additional Info')
    active = fields.Boolean(default=True)
    

    @api.depends('name')
    def compute_publisher(self):
        for rec in self:
            rec.partner_id = self.env.user.partner_id
            print(self.env.user.partner_id)

class Link(models.Model):
    _name = 'mt.link'
    _description = 'Links'
    name = fields.Char ('Name')
    link = fields.Char ('Link')
    link_id = fields.Many2one('mt.movie', string='Links To Movie')

class Additional(models.Model):
    _name = 'mt.additional'
    _description = 'Additional'
    name = fields.Char ('Name')
    description = fields.Char ('Description')
    additional_id = fields.Many2one('mt.movie', string='Additional To Movie')
