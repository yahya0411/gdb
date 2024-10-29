from odoo import models,fields
class Emprunt(models.Model):
    _name = 'emprunt'
    date_debut = fields.Datetime(string='Debut')
    date_fin = fields.Datetime(string='Fin')
    rendu = fields.Selection([
        ('oui','Oui'),
        ('non','Non')
    ])
    emprunteur_id = fields.Many2one('emprunteur', string="Emprunteur")
    auteur_id = fields.Many2one('auteur', string="Auteur")
    livre_id = fields.One2many('livre', 'emprunt_id', string='Emprunt')