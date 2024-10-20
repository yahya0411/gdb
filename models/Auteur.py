from odoo import models, fields
class Auteur (models.Model) :
    _name = 'auteur'

    nom=fields.Char(string="Nom")

    prenom= fields.Char(string="Prénom")

    date_naissance= fields.Date(string="Date de naissance")

    nationalite= fields.Char(string="Nationalité")
    sexe = fields.Selection([
    ('homme', 'Homme'),
    ('femme',' Femme')
    ])