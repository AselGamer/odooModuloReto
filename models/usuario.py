# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)

class Usuario(models.Model):
    _name = 'usuario'
    _inherit = ['image.mixin']

    name = fields.Char(string='Nombre')
    password = fields.Char(string='Contraseña')
    email = fields.Char(string='Email')
    apellido = fields.Char(string='Apellido')
    dinero = fields.Integer(string='Dinero')
    foto_perfil = fields.Binary(string='Foto de perfil')
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Moneda',
        default=lambda self: self.env.company.currency_id.id
    )


