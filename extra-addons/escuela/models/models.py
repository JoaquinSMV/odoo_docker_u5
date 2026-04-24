# -*- coding: utf-8 -*-

from odoo import models, fields, api


class profesor(models.Model):
    _name = 'escuela.profesor'
    _description = 'PROFESOR'

    name = fields.Char()
   