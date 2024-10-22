#-*-coding:utf-8 -*-
{
'name': 'gdb',
'version': '1.0',
'category': 'bibliothèque',
'author': 'Mekki Yahia',
'depends' : ['project'],
'description':"""ce module est destiné pour gérer des LA bibliothèque""",
'data' : ['security/ir.model.access.csv','views/auteur.xml','views/livre.xml','views/emprunt.xml','views/emprunteur.xml',],
'installable': True,
'application': True,
'auto_install': False,
}