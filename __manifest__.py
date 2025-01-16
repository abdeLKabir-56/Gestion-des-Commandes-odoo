{
    'name': 'Gestion des Commandes',
    'version': '1.0',
    'summary': 'Module de gestion des commandes client',
    'category': 'Sales',
    'author': 'abdelkabir elhamoussi',
    'website': 'http://votresite.com',
    'depends': ['base', 'sale', 'stock'],  # Check dependencies
    'data': [
        'views/views.xml',
         'security/ir.model.access.csv' # Add security access rules if needed
    ],
    'installable': True,
    'application': True,
}
