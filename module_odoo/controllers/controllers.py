# -*- coding: utf-8 -*-
from odoo import http
from odoo import http
from odoo.http import request
import werkzeug
from urllib.parse import urlparse, parse_qs

class Ntizu(http.Controller):

    @http.route('/candidato/', type='http', auth='public', website=True)
    def index_page(self, **kw):
        return request.render('ntizu.candidato', {})

    @http.route(['/candidato/submit'], csrf=False, type='http', auth="public", website=True)
    def contact_form_submit(self, **post):
        candidato = request.env['candidato.candidato'].sudo().create({
            'nome': post.get('nome'),
            'apelido': post.get('apelido'),
            'profissao': post.get('profissao'),
            'email': post.get('email'),
            'telefone': post.get('telefone'),
        })
        return request.redirect('/candidato/verificar?candidato_id=%s' % candidato.id)

    @http.route(['/candidato/verificar'], type='http', auth="public", website=True)
    def verify_page(self, **kw):
        candidato_id = request.httprequest.args.get('candidato_id')
        if not candidato_id:
            return request.redirect('/candidato/submit')

        return request.render('ntizu.wrapper', {'candidato_id': candidato_id})

    @http.route('/my_route', type='http', auth='public', website=True)
    def my_method(self, **kwargs):
        return request.render('ntizu.wrapper', {})

    @http.route('/token/', type='http', auth='public', website=True)
    def index_page(self, **kw):
        return request.render('ntizu.wrapper', {})

    @http.route(['/token/submit'], csrf=False, type='http', auth="public", website=True)
    def token_submit(self, **post):
        candidato_id = post.get('candidato_id')
        print(f'candidato_id: {candidato_id}')

        if not candidato_id:
            return request.redirect('/candidato/verificar')

        submitted_token = ''.join([
            post.get('token1', ''),
            post.get('token2', ''),
            post.get('token3', ''),
            post.get('token4', ''),
            post.get('token5', ''),
            post.get('token6', ''),
        ])

        print(submitted_token)
        candidato = request.env['candidato.candidato'].sudo().browse(int(candidato_id))

        if candidato and candidato.token == submitted_token:
            return request.render('ntizu.thank_you', {'candidato': candidato})
        else:
            return request.render('ntizu.verificacao_falha', {'candidato': candidato})

