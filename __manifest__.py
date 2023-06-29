
# -*- coding: utf-8 -*-
###############################################################################
#
#    INDE TRUCK S.L. <informatica@indetruck.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses
#    
#    Odoo and OpenERP is trademark of Odoo S.A.
#
###############################################################################
{
    'name': 'Inventario Mod',
    'summary': 'Inventario Mod ',
    'version': '1.0',

    'description': """
Inventario.
==============================================


    """,

    'author': 'Raúl Ramírez',

    'website': 'www.indetruck.com',

    'license': 'AGPL-3',
    'category': 'Uncategorized',

    'depends': [
        'base',
        'stock',
    ],
    'external_dependencies': {
        'python': [
        ],
    },
    'data': [
        'views/stock_picking.xml'
    ],
    'demo': [
    ],
    'js': [
    ],
    'css': [
    ],
    'qweb': [
    ],
    'images': [
    ],
    'test': [
    ],

    'installable': True
}
