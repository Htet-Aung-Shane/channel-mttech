import odoo.http as http
from odoo.http import request
from odoo.http import request, Response
import json
from odoo import models

class ContactShow(http.Controller):
    @http.route(["/api/contacts"], type="http", auth="user", methods=["GET"], website=True, cors="*" )
    def show(self, **post):

        token = request.httprequest.headers.get('Authorization')
        contact_ids = request.env["res.partner"].sudo().search([])
        contact_data = []

        for contact in contact_ids:
            contact_data.append({
                'id': contact.id,
                'name': contact.name,
            })
        response = {
            'status': 'success',
            'data': contact_data
        }
        return http.Response(json.dumps(response), content_type='application/json')