{
    'name' : 'MT Sales',
    'description' : 'Sales And Invoice customization for MT Tech',
    'depends' : ['base','contacts', 'account_accountant'],
    'category': 'Manufacturing',
    'author': 'Htet Aung Shane',
    'installable': True,
    'auto_install': False,
    'application': True,
    'data': [
        'security/ir.model.access.csv',  
        'views/menu.xml', 
        'views/service.xml', 
        'views/service_type.xml', 
        'views/company.xml', 
        'views/city.xml', 
    ]
}