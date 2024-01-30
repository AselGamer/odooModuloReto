# -*- coding:utf-8 -*-

import logging
from odoo import fields, models, api
from odoo.exceptions import UserError

logger = logging.getLogger(__name__)


class Venta(models.Model):
    _name = 'venta'
    _inherit = ['image.mixin']

    usuario_id = fields.Many2one(comodel_name='usuario', string='Usuario')
    tipo = fields.Selection(
        selection=[('arma', 'Arma'),
                   ('armadura', 'Armadura'),
                   ('medicamento', 'Medicamento')],
    )
    fch_compra = fields.Datetime(string='Fecha compra', copy=False)
    arma_id = fields.Many2one(comodel_name='arma', string='Arma')
    armadura_id = fields.Many2one(comodel_name='armadura', string='Armadura')
    medicamento_id = fields.Many2one(comodel_name='medicamento', string='Medicamento')
    arma_imagen = fields.Binary(related='arma_id.imagen', string='Imagen articulo')
    armadura_imagen = fields.Binary(related='armadura_id.imagen', string='Imagen articulo')
    medicamento_imagen = fields.Binary(related='medicamento_id.imagen', string='Imagen articulo')
    total_arma = fields.Monetary(default=0, related='arma_id.precio', string='Total arma')
    total_armadura = fields.Monetary(default=0, related='armadura_id.precio',string='Total armadura')
    total_medicamento = fields.Monetary(default=0, related='medicamento_id.precio',string='Total medicamento')
    total_articulo = fields.Monetary(string='Total', compute='_compute_total', store=True)
    currency_id = fields.Many2one(
        comodel_name='res.currency',
        string='Moneda',
        default=lambda self: self.env.company.currency_id.id
    )

    state = fields.Selection(
        selection=[('presupuesto', 'Presupuesto'),
                   ('comprado', 'Comprado')],
        default='presupuesto', string='Estado', copy=False
    )

    @api.depends('total_arma', 'total_armadura', 'total_medicamento')
    def _compute_total(self):
        for record in self:
            record.total_articulo = record.total_arma + record.total_armadura + record.total_medicamento

    def realizar_compra(self):
        dinero_disponible = self.usuario_id.dinero
        total_articulo = self.total_articulo
        if(dinero_disponible < total_articulo):
            raise UserError('No tienes dinero suficiente')
        else:
            self.usuario_id.dinero = dinero_disponible - total_articulo
            self.state = 'comprado'
            self.fch_compra = fields.Datetime.now()