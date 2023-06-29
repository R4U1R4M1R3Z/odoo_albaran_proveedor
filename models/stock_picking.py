# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class StockPickingMod(models.Model):
    _inherit = 'stock.picking'

    albaranProveedor = fields.Char(
        string='Albarán del proveedor',
    )



class StockMoveMod(models.Model):
    _inherit = 'stock.move'



    @api.onchange('price_unit')
    def _onchange_price_unit(self):
        for record in self:
            if record.product_id:
                record.product_id.standard_price = record.price_unit
                supplier_info = self.env['product.supplierinfo'].search([('product_tmpl_id', '=', record.product_id.id), ('name', '=', record.partner_id.id)], limit=1)
                if supplier_info:
                    supplier_info.price = record.price_unit