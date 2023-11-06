{
    'name' : 'Movies',
    'description' : 'Movies Website Hosted By MT Tech',
    'depends' : ['base','contacts'],
    'category': 'Education',
    'author': 'Htet Aung Shane',
    'data': [
        'security/ir.model.access.csv',   
        'security/permission.xml', 
        'views/movie.xml',
        'views/movie_website.xml',
        'views/genre.xml',
        'views/category.xml',
        'views/tag.xml',
        'views/cast.xml',
        'views/movie_sequence.xml',
        'views/menu.xml',     
        ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets':{
        'web.assets_frontend': [
            '/movies/static/src/scss/movie_common.scss'
        ]
    }
}