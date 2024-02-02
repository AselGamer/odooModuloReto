# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class Armadura(models.Model):
    _name = 'armadura'
    _inherit = ['image.mixin']

    name = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')
    defensa = fields.Integer(string='Defensa')
    precio = fields.Monetary(string='Precio')
    currency_id = fields.Many2one(
        comodel_name="res.currency", string='Moneda',
        default=lambda self: self.env.company.currency_id.id
    )
    imagen = fields.Binary(string='Imagen')
    ventas = fields.Integer(string='Ventas', default=0)

    priority = fields.Selection([
        ('0', 'Nulo'),
        ('1', 'Favorito')
    ], string='Prioridad', default='0')

    state = fields.Selection([
        ('comprado', 'Comprado'),
        ('no_comprado', 'No comprado')
    ], string='Estado', default='no_comprado')