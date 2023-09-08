import odoo.http as http
from odoo.http import request
from odoo.http import request, Response
import json
from odoo import models

class BookShow(http.Controller):
    @http.route(['/movies'], type='http',
                auth='public', website=True)
    def show(self, **get):
        country_ids = request.env['res.country'].sudo().search([])
        genre_ids = request.env['mt.genre'].sudo().search([])
        category_ids = request.env['mt.category'].sudo().search([])
        type_ids = request.env['mt.tag'].sudo().search([])
        cast_ids = request.env['mt.cast'].sudo().search([])
        print('countries>',country_ids,'genre',genre_ids,'category',category_ids,'type_ids',type_ids,'cast_ids',cast_ids)
        get.update({
                'countries': country_ids,
            })
        return http.request.render(
            "movies.movies_list",get
        )