from odoo import models,fields
class Emprunteur(models.Model):
    _name = 'emprunteur'
    _rec_name = 'nom'
    nom = fields.Char(string='Nom')
    prenom = fields.Char(string='Prenom')
    date_naissance = fields.Datetime(string='Date de naissance')
    state = fields.Selection([('draft', 'Draft'), ('published', 'Published')],)
    sexe = fields.Selection([('homme', 'Homme'), ('femme', 'Femme')],)
    emprunt_id = fields.One2many('emprunt', 'emprunteur_id', string='Emprunteur')