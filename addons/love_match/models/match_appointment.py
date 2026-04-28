# -*- coding: utf-8 -*-

from odoo import models, fields, api

class match_appointment(models.Model):
    _name = 'love_match.match_appointment'
    _description = 'Solicitud de cita'

    user_from_id = fields.Many2one(
        string='Solicitud recibida',
        comodel_name='love_match.match_user',
        ondelete='restrict', required=True
    )
    
    user_to_id = fields.Many2one(
        string='Solicitud enviada',
        comodel_name='love_match.match_user',
        ondelete='restrict', required=True
    )
    
    scheduled_datetime = fields.Datetime(
        string='Fecha de cita',
        default=fields.Datetime.now,
        required=True
    )

    location = fields.Char(string="Lugar o direccion", required=True)

    status = fields.Selection(
    selection=[
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('cancelled', 'Cancelada'),
    ],
    string='Estado de su solicitud',
    required=True,
    default='pending'
    )
    
    notes = fields.Text(
        string='Notas'
    )
    
    