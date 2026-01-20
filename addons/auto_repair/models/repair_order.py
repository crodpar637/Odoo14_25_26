# -*- coding: utf-8 -*-
"""
c) Modelo "repair_order" (0,75 puntos)
Crear el modelo "repair_order", que debe incluir los siguientes campos:
• name (Char, requerido): Identificador de la orden de reparación.
• vehicle_plate (Char, requerido): Matrícula del vehículo a reparar.
• client_name (Char, requerido): Nombre del cliente.
• repair_date (Datetime, requerido): Fecha y hora de la reparación.
• cost (Float): Coste estimado de la reparación.
• mechanic_id (Many2one a mechanic, requerido): Mecánico asignado a la reparación
"""

from odoo import models, fields, api

class repair_order(models.Model):
    _name = 'auto_repair.repair_order'
    _description = 'Orden de reparación'

    name = fields.Char(string="ID orden reparación", required=True)
    vehicle_plate = fields.Char(string="Matricula",required=True)
    client_name = fields.Char(string="Nombre del cliente",required=True)
    repair_date = fields.Datetime(
        string='Fecha de la reparación',
        default=fields.Datetime.now,
        required=True
    )
    cost = fields.Float(string="Coste estimado")
    
    mechanic_id = fields.Many2one(
        string='Mecánico',
        comodel_name='auto_repair.mechanic',
        ondelete='restrict',
    )
    