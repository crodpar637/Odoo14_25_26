# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class auto_repair(models.Model):
#     _name = 'auto_repair.auto_repair'
#     _description = 'auto_repair.auto_repair'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
