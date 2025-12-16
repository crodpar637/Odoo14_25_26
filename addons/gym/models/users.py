from odoo import models, fields, api

class Users(models.Model):
    _name = 'gym.users'
    _description = 'Gym Users'
    
    name = fields.Char(string="Nombre", size=60, required=True, help="Nombre del usuario")
    idcard = fields.Char('ID Card', size=9, required=True)
    photo=fields.Binary('Foto')
    
    classes_ids = fields.Many2many("gym.classes",string="Clases del usuario")