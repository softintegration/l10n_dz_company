# -*- coding: utf-8 -*- 


from odoo import models,fields,api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = "res.partner"

    accounting_if = fields.Char(string="IF")
    accounting_nis = fields.Char(string="NIS")
    accounting_rc = fields.Char(string="RC")
    accounting_ai = fields.Char(string="AI")
    accounting_rc_issue_date = fields.Date(string='RC issue date')
    accounting_legal_status_id = fields.Many2one("res.company.legal.status", string="Legal status")
    accounting_ident_number = fields.Char(string='ID number')
    accounting_ident_issue_date = fields.Date(string='ID card issue date')