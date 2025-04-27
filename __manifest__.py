{
    'name': 'Research Project',
    'version': '1.0',
    'summary': 'Gestión de proyectos de investigación',
    'description': 'Un módulo para administrar proyectos de investigación en Odoo.',
    'author': 'Gustavo Seijas',
    'category': 'Project',
    'depends': ['base', 'mail', 'web'],
    'data': [
        'security/research_project_security.xml',
        'security/ir.model.access.csv',
        'data/research_project_sequence.xml',
        'views/research_project_views.xml',
        'report/report_research_project.xml',
    ],
    'installable': True,
    'application': True,
}