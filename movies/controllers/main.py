import odoo.http as http
from odoo.http import request
from odoo.http import request, Response
import json
from odoo import models

class BookShow(http.Controller):
    @http.route(['/movies'], type='http',
                auth='public', website=True)
    def show(self, **get):
        return http.request.render(
            "movies.movies_list",get
        )