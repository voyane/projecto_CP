from odoo import http
from odoo.http import request
import base64
from odoo.http import request, _logger, Response
import requests
from odoo.tools.safe_eval import json


class BlogController(http.Controller):

    @http.route('/get-blog/', auth='public', type="json", methods=['POST'])
    def get_blog(self):
        registros = request.env['customblog.customblog'].sudo().search([])

        dados_blog = []

        for registro in registros:
            image_url = f"/api/blog_image/{registro.id}" if registro.featured_image else "https://via.placeholder.com/1920x1080.png?text=No+Image"
            dados_blog.append({
                'id': registro.id,
                'author': registro.author,
                'published_date': registro.published_date.strftime('%Y-%m-%d'),
                'category': registro.category,
                'tags': registro.tags,
                'post_title': registro.post_title,
                'content': registro.content,
                'comments': registro.comments,
                'image': image_url,
            })

        return dados_blog

    @http.route('/api/blog_image/<int:candidate_id>', type='http', auth='public', methods=['GET'], csrf=False)
    def get_candidate_image(self, candidate_id, **kwargs):
        candidate = request.env['customblog.customblog'].sudo().browse(candidate_id)

        default_image_url = 'https://img.freepik.com/free-vector/error-404-concept-landing-page_23-2148237748.jpg?w=740&t=st=1722329273~exp=1722329873~hmac=b5deb354d7059b35548596a91ddfcf6cf31f31690997b3b6ea7bacd648df46f6'

        if candidate.exists() and candidate.featured_image:
            image_data = base64.b64decode(candidate.featured_image)
            return Response(image_data, mimetype='image/png')
        else:
            try:
                response = requests.get(default_image_url)
                if response.status_code == 200:
                    return Response(response.content, mimetype='image/png')
                else:
                    return Response("Image not found", status=404)
            except requests.RequestException:
                return Response("Error fetching default image", status=500)

    @http.route('/bblog/<int:id>/', type='http', auth='public', website=True)
    def function_name(self, id):
        record = request.env['customblog.customblog'].sudo().search([('id', '=', id)], limit=1)

        image_url = "/web/image/customblog.customblog/{}/featured_image".format(
            record.id) if record.featured_image else "https://via.placeholder.com/1920x1080.png?text=No+Image"

        values = {
            'key_value': record,
            'image_url': image_url,
        }
        return request.render('ntizu.visualizacao', values)
