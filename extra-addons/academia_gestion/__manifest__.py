{
    "name": "Gestión de Academia",
    "version": "18.0.1.0.0",
    "category": "Education",
    "summary": "Módulo para la gestión de estudiantes y profesores.",
    "author": "",
    "website": "",
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "report/estudiante_report_templates.xml",
        "report/estudiante_report.xml",
        "views/estudiante_views.xml",
        "views/profesor_views.xml",
        "views/res_partner_views.xml",
        "views/academia_menu.xml",
    ],
    "demo": [
        "demo/academia_demo.xml",
    ],
    "installable": True,
    "application": True,
}
