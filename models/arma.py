# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


# Cuando le damos a Crear
class Arma(models.Model):
    _name = 'arma'
    _inherit = ['image.mixin']

    name = fields.Char(string='Nombre')
    descripcion = fields.Text(string='Descripción')
    danyo = fields.Integer(string='Daño')
    velocidad = fields.Integer(string='Velocidad de disparo')
    precio = fields.Monetary(string='Precio')
    currency_id = fields.Many2one(
        comodel_name="res.currency", string='Moneda',
        default=lambda self: self.env.company.currency_id.id
    )
    imagen = fields.Binary(string='Imagen')
