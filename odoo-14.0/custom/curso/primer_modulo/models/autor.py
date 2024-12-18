from odoo import models, fields


class Autor(models.Model):
    _name='autor'
    _res_name = 'last_name'

    name = fields.Char(string="Nombre")
    last_name = fields.Char(strings="Apellido")