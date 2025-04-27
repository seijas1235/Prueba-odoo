from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ResearchProject(models.Model):
    """Modelo para gestionar proyectos de investigación en Odoo.

    Este modelo permite crear y administrar proyectos de investigación, con campos como nombre,
    código, fechas, presupuesto, investigadores y estado. También incluye lógica para calcular
    la duración del proyecto y validar fechas.
    """
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
        """Calcula la duración del proyecto en días basado en las fechas de inicio y fin.

        Si las fechas están definidas, calcula los días entre `start_date` y `end_date`.
        Si no, establece la duración en 0.
        """
        for project in self:
            if project.start_date and project.end_date:
                project.duration = (project.end_date - project.start_date).days
            else:
                project.duration = 0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """Valida que la fecha de inicio sea anterior a la fecha de finalización.

        Si la fecha de inicio es mayor a la de finalización, lanza un error de validación.
        """
        for project in self:
            if project.start_date and project.end_date and project.start_date > project.end_date:
                raise ValidationError('La fecha de inicio debe ser anterior a la fecha de finalización.')

    @api.onchange('start_date')
    def _onchange_start_date(self):
        """Limpia la fecha de finalización si la fecha de inicio es posterior.

        Esto evita que el usuario tenga que corregir manualmente la fecha de fin si cambia
        la fecha de inicio a una fecha posterior.
        """
        if self.start_date and self.end_date and self.start_date > self.end_date:
            self.end_date = False

    def action_set_in_progress(self):
        """Cambia el estado del proyecto a 'En Progreso'.

        Este método se usa desde un botón en la vista de formulario para avanzar el estado.
        """
        self.write({'state': 'in_progress'})

    def action_set_review(self):
        """Cambia el estado del proyecto a 'En Revisión'.

        Este método se usa desde un botón en la vista de formulario para avanzar el estado.
        """
        self.write({'state': 'review'})

    def action_set_completed(self):
        """Cambia el estado del proyecto a 'Completado'.

        Este método se usa desde un botón en la vista de formulario para marcar el proyecto como finalizado.
        """
        self.write({'state': 'completed'})

    def action_set_cancelled(self):
        """Cambia el estado del proyecto a 'Cancelado'.

        Este método se usa desde un botón en la vista de formulario para cancelar el proyecto.
        """
        self.write({'state': 'cancelled'})

    def action_set_draft(self):
        """Cambia el estado del proyecto a 'Nuevo' (Borrador).

        Este método se usa desde un botón en la vista de formulario para reiniciar el estado.
        """
        self.write({'state': 'draft'})