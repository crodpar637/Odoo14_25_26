from odoo import models, fields, api

class Classes(models.Model):
    _name = 'gym.classes'
    _description = 'Gym Classes'
    
    name = fields.Char(string="Nombre de la clase", required=True, help="Nombre de la clase")
    description = fields.Text(string="Descripción de la clase")
    start = fields.Datetime('Inicio',required=True, autodate = True)
    end = fields.Datetime('Fin',required=True, autodate = True)
    capacity = fields.Integer("Capacidad")
    activityType = fields.Selection([('dance','Baile'),
        ('aerobic','Aerobic'),
        ('anaerobic','Anaerobico'),
        ('relax','Relax'),],
        'Tipo de actividad')
    
    users_ids = fields.Many2many("gym.users",string="Usuarios apuntados")