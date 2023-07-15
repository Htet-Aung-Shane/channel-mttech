{
    'name' : 'Movies',
    'description' : 'Movies Website Hosted By MT Tech',
    'depends' : ['base','contacts'],
    'category': 'Education',
    'author': 'Htet Aung Shane',
    'data': [
        'security/ir.model.access.csv',   
        'views/movie.xml',
        'views/genre.xml',
        'views/category.xml',
        'views/menu.xml',     
        ],
    'installable': True,
    'auto_install': False,
    'application': True,
}