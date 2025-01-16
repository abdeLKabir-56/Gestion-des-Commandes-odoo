# -*- coding: utf-8 -*-

from odoo import models, fields, api

class GestionCommande(models.Model):
    _name = 'gestion.commande'
    _description = 'Gestion des Commandes'

    name = fields.Char(string='Référence', required=True, index=True, default=lambda self: self._default_name())
    date_commande = fields.Datetime(string='Date de Commande', default=fields.Datetime.now)
    client_id = fields.Many2one('res.partner', string='Client', required=True)
    ligne_commande_ids = fields.One2many('gestion.commande.ligne', 'commande_id', string='Lignes de Commande')
    montant_total = fields.Float(string='Montant Total', compute='_compute_montant_total', store=True)

    @api.model
    def _default_name(self):
        return self.env['ir.sequence'].next_by_code('gestion.commande.sequence')

    @api.depends('ligne_commande_ids.prix_total')
    def _compute_montant_total(self):
        for commande in self:
            commande.montant_total = sum(ligne.prix_total for ligne in commande.ligne_commande_ids)

class GestionCommandeLigne(models.Model):
    _name = 'gestion.commande.ligne'
    _description = 'Lignes de Commande'

    commande_id = fields.Many2one('gestion.commande', string='Commande', ondelete='cascade')
    produit_id = fields.Many2one('product.product', string='Produit', required=True)
    quantite = fields.Float(string='Quantité', default=1.0)
    prix_unitaire = fields.Float(string='Prix Unitaire', related='produit_id.list_price')
    prix_total = fields.Float(string='Prix Total', compute='_compute_prix_total', store=True)

    @api.depends('quantite', 'prix_unitaire')
    def _compute_prix_total(self):
        for ligne in self:
            ligne.prix_total = ligne.quantite * ligne.prix_unitaire