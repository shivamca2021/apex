{
    'name': "Branch and Shop Master",
    'summary': """Branch and Shop Master.""",
    'description': """
        Branch and Shop Master
    """,
    'website': "",
    'author': "",
    'category': 'Tools',
    'version': '17.0.0.0',
    'depends': ['base', 'sale','sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'views/masters_view.xml',
        'views/inherit_sale_order_view.xml',
    ],
    'images': [],
    'license': "AGPL-3",
    'installable': True,
    'application': True,
}
