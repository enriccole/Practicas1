{
    'name': "Curso de programación Odoo 14",
    'summary':"""
        Curso de programación Odoo 14, funcionalidades
    """,
    'author':'Enric Lazaro',
    'category':'General',
    'version':'1.0.0',
    'depends':['mail','hr'],
    'data':[
        'security/libreria_security.xml',
        'views/libros_view.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/hr_employee_view.xml'
    ],
    'application': True,
    "installable": True,
}