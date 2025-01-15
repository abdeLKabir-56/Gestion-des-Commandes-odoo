from odoo import models, fields

class PartModel(models.Model):
    _name = 'part_model'
    _description = 'Part Model'

    name = fields.Char(string='Part Name', required=True)
