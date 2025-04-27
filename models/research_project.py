from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResearchProject(models.Model):
    _name = 'research.project'
    _description = 'Research Project'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nombre del Proyecto', required=True, tracking=True)
    code = fields.Char(string='Código', readonly=True, copy=False, default=lambda self: self.env['ir.sequence'].next_by_code('research.project'))
    description = fields.Text(string='Descripción', tracking=True)
    start_date = fields.Date(string='Fecha de Inicio', tracking=True)
    end_date = fields.Date(string='Fecha de Finalización', tracking=True)
    budget = fields.Float(string='Presupuesto', tracking=True)
    leader_id = fields.Many2one('res.partner', string='Investigador Principal', tracking=True)
    investigator_ids = fields.Many2many('res.partner', string='Investigadores', tracking=True)
    priority = fields.Selection([
        ('0', 'Baja'),
        ('1', 'Media'),
        ('2', 'Alta'),
    ], string='Prioridad', default='1', tracking=True)
    state = fields.Selection([
        ('draft', 'Nuevo'),
        ('in_progress', 'En Progreso'),
        ('review', 'En Revisión'),
        ('completed', 'Completado'),
        ('cancelled', 'Cancelado'),
    ], string='Estado', default='draft', tracking=True)
    duration = fields.Integer(string='Duración (días)', compute='_compute_duration', store=True)

    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for project in self:
            if project.start_date and project.end_date:
                project.duration = (project.end_date - project.start_date).days
            else:
                project.duration = 0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for project in self:
            if project.start_date and project.end_date and project.start_date > project.end_date:
                raise ValidationError('La fecha de inicio debe ser anterior a la fecha de finalización.')

    @api.onchange('start_date')
    def _onchange_start_date(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            self.end_date = False

    def action_set_in_progress(self):
        self.write({'state': 'in_progress'})

    def action_set_review(self):
        self.write({'state': 'review'})

    def action_set_completed(self):
        self.write({'state': 'completed'})

    def action_set_cancelled(self):
        self.write({'state': 'cancelled'})

    def action_set_draft(self):
        self.write({'state': 'draft'})