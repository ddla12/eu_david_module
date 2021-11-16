# -*- coding: utf-8 -*-
from odoo import models, fields

class Pet(models.Model):
    _name           = "pets"
    _description    = "Pets"

    # Required fields
    name = fields.Char(
        required    = True,
        string      = "Pet name"
    )
    partner_id = fields.Many2one(
        "res.partner", 
        string="Owner", 
        required=True
    )
    species = fields.Many2one(
        "species",
        string = "Species",
        required = True
    )
    age = fields.Integer(
        required    = True,
        string      = "Pet age"
    )
    genre   = fields.Selection(
        selection = [
            ("male", "Male"),
            ("female", "Female")
        ],
        required = True,
        string = "Pet genre"
    ) 

    # Optional fields
    history = fields.Text(
        size = 120,
        string = "Something to tell about yout pet?"
    )
    found_place = fields.Selection(
        selection = [
            ("street", "On the street"),
            ("gift", "Was a gift"),
            ("store", "I bought it")
        ],
        string = "Where did you get your pet?"
    )
    color = fields.Char(
        string = "Color of your pet",
        size = 16
    )
    get_date = fields.Date(
        string = "When did you get your pet?"
    )