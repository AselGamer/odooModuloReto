# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class Venta(models.Model):
    _name = 'venta'


    cliente_id = fields.Many2one(comodel_name='res.partner', string='Cliente')
