from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Estudiante(models.Model):
    _name = 'academia.estudiante'
    _description = 'Estudiante'

    name = fields.Char(string='Nombre Completo', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento')
    edad = fields.Integer(string='Edad', compute='_compute_edad', store=True)
    email = fields.Char(string='Email', required=True, unique=True)
    telefono = fields.Char(string='Teléfono')
    direccion = fields.Text(string='Dirección')
    profesor_ids = fields.Many2many('academia.profesor', string='Profesores Asignados')
    partner_id = fields.Many2one('res.partner', string='Contacto Relacionado', ondelete='restrict')

    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for rec in self:
            if rec.fecha_nacimiento:
                today = fields.Date.today()
                rec.edad = today.year - rec.fecha_nacimiento.year - \
                           ((today.month, today.day) < (rec.fecha_nacimiento.month, rec.fecha_nacimiento.day))
            else:
                rec.edad = 0

    @api.constrains('fecha_nacimiento')
    def _check_fecha_nacimiento(self):
        for rec in self:
            if rec.fecha_nacimiento and rec.fecha_nacimiento > fields.Date.today():
                raise ValidationError('La fecha de nacimiento no puede ser en el futuro.')

    @api.constrains('email')
    def _check_unique_email(self):
        for rec in self:
            if rec.email and self.search_count([('email', '=', rec.email), ('id', '!=', rec.id)]) > 0:
                raise ValidationError('El email ya existe. Por favor, introduce un email único.')

    @api.onchange('fecha_nacimiento')
    def _onchange_fecha_nacimiento(self):
        if self.fecha_nacimiento:
            self._compute_edad()
            if self.edad < 18:
                return {
                    'warning': {
                        'title': "Advertencia de Edad",
                        'message': "El estudiante es menor de 18 años.",
                    }
                }

