# -*- coding: utf-8 -*-
"""
Crear el modelo "match_user", que debe incluir los siguientes campos:
• name (Char, requerido): Nombre del usuario.
• email (Char, requerido): Dirección de correo electrónico del usuario.
• age:Integer
• gender: Selection  (opciones: "he", "she", "any")
• photo (Binary): Imagen .
• status (Selection, requerido, opciones: "active", "on_break", "banned"): Estado del usuario.
• num_appointments (Integer, calculado): Número de citas.
• match_ids (One2many a match_appointment, campo user_from_id): Lista de peticiones
• received_match_ids (One2many a match_appointment, campo user_to_id): Lista de solicitudes
"""
from odoo import models, fields, api

class user(models.Model):
    _name = 'love_match.match_user'
    _description = 'Solicitante'

    name = fields.Char(string="Nombre", required=True)
    email = fields.Char(string="Email",required=True)
    age = fields.Integer(string='Edad', default=0)

    gender = fields.Selection(
    selection=[
        ('he', 'He/El'),
        ('she', 'She/Ella'),
        ('any', 'Indistinto'),
    ],
    string='Genero',
    required=True,
    default='any'
    )   

    photo = fields.Binary(string="Fotografía")

    biography = fields.Text(
        string='Biografia'
    )

    status = fields.Selection(
        string='Estado',
        selection=[('active', 'Activo'), 
                   ('on-break', 'Descanso'), 
                   ('banned', 'Baneado')],
        default='active', readonly=True
    )
    
    num_appointments = fields.Integer(
        compute='_compute_num_appointments' )
    
    match_ids = fields.One2many(
        string='Matches',
        comodel_name='love_match.match_appointment',
        inverse_name='user_from_id',
    )

    received_match_ids = fields.One2many(
        string='Received Match',
        comodel_name='love_match.match_appointment',
        inverse_name='user_to_id',
    )
    
    @api.depends('match_ids')
    def _compute_num_appointments(self):
        for record in self:
            record.num_appointments = len(record.match_ids)
    
   # @api.constrains('match_ids')
   # def _check_status(self):
   #     for record in self:
   #         if record.status == 'on-break':
   #             raise models.ValidationError('No se puede citar esta en break ')
        