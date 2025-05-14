# -*- coding: utf-8 -*-
{
    'name': "ntizu",
    'description': 'Default website theme',
    'category': 'Theme',
    'sequence': 30,
    'version': '1.0',
    'depends': ['base', 'hr', 'website'],
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/assets.xml',
        'views/templates/Home/Home.xml',
        'views/templates/Form/candidato.xml',
        'views/templates/Token/token.xml',
        'views/custom_layout.xml',
        'views/thanks.xml',
        'views/verificacao_falha.xml',
        'views/templates/Blogcards/blogcards.xml',
        'views/templates/Blogfilter/blogfilter.xml',
        'views/templates/Candidato/candi.xml',
        'views/templates/Banner/baneer.xml',
        'views/templates/Banner/Bannerwomen.xml',
        'views/templates/Banner/baneer.xml',
        'views/templates/Footer/Footer.xml',
        'views/templates/HomePage/Homepage.xml',
        'views/templates/Webform/formweb.xml',
        'views/templates/Empresa/Empresa.xml',
    ],

    'qweb': [
    ],

    'assets': {
        'web.assets_backend': [
            '/ntizu/static/src/js/blog.js',
        ],
        'web.assets_frontend': [
            '/ntizu/static/src/js/blog.js',

        ],
    },

    'images': [

    ],
    'snippet_lists': {
    },
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
