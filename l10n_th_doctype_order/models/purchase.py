# -*- coding: utf-8 -*-
from openerp import models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def create(self, vals):
        # Find doctype_id
        refer_type = 'purchase_order'
        doctype = self.env['res.doctype'].get_doctype(refer_type)
        fiscalyear_id = self.env['account.fiscalyear'].find()
        # --
        self = self.with_context(doctype_id=doctype.id,
                                 fiscalyear_id=fiscalyear_id)
        vals['name'] = self.env['ir.sequence'].next_by_doctype()
        return super(PurchaseOrder, self).create(vals)
