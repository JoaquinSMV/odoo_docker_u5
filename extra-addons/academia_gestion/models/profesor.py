from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Profesor(models.Model):
    _name = 'academia.profesor'
    _description = 'Profesor'

    name = fields.Char(string='Nombre Completo', required=True)
    email = fields.Char(string='Email', required=True, unique=True)
    telefono = fields.Char(string='Teléfono')
    especialidad = fields.Char(string='Especialidad')
    estudiante_ids = fields.Many2many('academia.estudiante', string='Estudiantes Asignados')
    partner_id = fields.Many2one('res.partner', string='Contacto Relacionado', ondelete='restrict')

    @api.constrains('email')
    def _check_unique_email(self):
        for rec in self:
            if rec.email and self.search_count([('email', '=', rec.email), ('id', '!=', rec.id)]) > 0:
                raise ValidationError('El email ya existe. Por favor, introduce un email único para el profesor.')
