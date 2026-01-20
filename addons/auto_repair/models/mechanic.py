# -*- coding: utf-8 -*-
"""
Crear el modelo "mechanic", que debe incluir los siguientes campos:
• name (Char, requerido): Nombre del mecánico.
• email (Char, requerido): Dirección de correo electrónico del mecánico.
• employee_id (Char, requerido): Número de identificación del mecánico en el taller.
• phone (Char): Número de teléfono del mecánico.
• photo (Binary): Imagen del mecánico.
• status (Selection, requerido, opciones: "active", "inactive", "on_break"): Estado del mecánico.
• num_repairs (Integer, calculado): Número de reparaciones asignadas al mecánico.
• repair_ids (One2many a repair_order, campo mechanic_id): Lista de reparaciones asignadas al
mecánico
"""
from odoo import models, fields, api

class mechanic(models.Model):
    _name = 'auto_repair.mechanic'
    _description = 'Mecanico del taller'

    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email",required=True)
    employee_id = fields.Char(string="Número de empleado",required=True)
    phone = fields.Char(string="Teléfono")
    photo = fields.Binary(string="Fotografía")
    
    status = fields.Selection(
        string='Estado',
        selection=[('active', 'Activo'), ('inactive', 'Inactivo'), ('on-break', 'Descanso')]
    )
    
    num_repairs = fields.Integer(
        compute='_compute_num_repairs' )
    
    repair_ids = fields.One2many(
        string='Reparaciones',
        comodel_name='auto_repair.repair_order',
        inverse_name='mechanic_id',
    )
    
    @api.depends('repair_ids')
    def _compute_num_repairs(self):
        for record in self:
            record.num_repairs = len(record.repair_ids)
    