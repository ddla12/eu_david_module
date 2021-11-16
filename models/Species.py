# -*- coding: utf-8 -*-
from odoo import models, fields

class Species(models.Model):
    _name           = "species"
    _description    = "Species"

    # Required fields
    name = fields.Char(
        required    = True,
        string      = "Species"
    )