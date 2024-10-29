from odoo import models, fields
class Auteur (models.Model) :
    _name = 'auteur'
    _rec_name = 'nom'
    nom=fields.Char(string="Nom")

    prenom= fields.Char(string="Prénom")

    date_naissance= fields.Date(string="Date de naissance")

    nationalite= fields.Char(string="Nationalité",default="algerienne")
    sexe = fields.Selection([
    ('homme', 'Homme'),
    ('femme',' Femme')
    ])
    livre_ids = fields.One2many('livre', 'auteur_id',string="Livre")