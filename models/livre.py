from odoo import models, fields

class Livre(models.Model):
    _name = 'livre'
    titre = models.Char(String = "Titre", required = True)
    langue_livre =models.Selection([
        ('francais','Francais'),
        ('arabe','Arabe'),
        ('anglais','Anglais'),
    ])
    isbn = fields.Char(String = "ISBN")
    nbre_page = fields.Integer(String = "NBR PAGE")
    image_libre = fields.Char(String = "Image Libre")