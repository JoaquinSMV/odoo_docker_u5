from odoo import fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'

    es_estudiante = fields.Boolean(string='Es Estudiante', compute='_compute_es_estudiante', store=True)
    es_profesor = fields.Boolean(string='Es Profesor', compute='_compute_es_profesor', store=True)
    estudiante_id = fields.One2many('academia.estudiante', 'partner_id', string='Estudiante Relacionado')
    profesor_id = fields.One2many('academia.profesor', 'partner_id', string='Profesor Relacionado')

    def _compute_es_estudiante(self):
        for partner in self:
            partner.es_estudiante = bool(partner.estudiante_id)

    def _compute_es_profesor(self):
        for partner in self:
            partner.es_profesor = bool(partner.profesor_id)
