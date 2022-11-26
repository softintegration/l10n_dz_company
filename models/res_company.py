# -*- coding: utf-8 -*- 

from odoo import models,fields,api
from odoo.exceptions import UserError


class ResCompany(models.Model):
    _inherit = "res.company"

    accounting_if = fields.Char(string="IF")
    accounting_nis = fields.Char(string="NIS")
    accounting_rc = fields.Char(string="RC")
    accounting_ai = fields.Char(string="AI")
    accounting_rc_issue_date = fields.Date(string='RC issue date')
    accounting_legal_status_id = fields.Many2one("res.company.legal.status", string="Legal status")
    accounting_share_capital = fields.Char(string="Share capital")

class LegalStatus(models.Model):
    _name = 'res.company.legal.status'

    name = fields.Char(string="Name", required=True)
    code = fields.Char(string="Code",required=True)
    description = fields.Text(string="Description")