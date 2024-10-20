from odoo import models,fields
class Emprunt(models.Model):
    _name = 'emprunt'
    date_debut = fields.Datetime(string='Debut')
    date_fin = fields.Datetime(string='Fin')
    rendu = fields.Selection([
        ('oui','Oui'),
        ('non','Non')
    ])