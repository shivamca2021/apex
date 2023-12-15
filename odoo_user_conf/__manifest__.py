# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Additional Odoo Conf',
    'version' : '17.0.0.0',
    'description': """'version' : '1.2',
    """,
    'depends': ['base', 'branch_shop_master'],
    'data': [
        'views/res_user.xml'
    ],
    'auto_install': True,
    'uninstall_hook': 'uninstall_hook',
    'license': 'LGPL-3',
}
