# -*- coding: utf-8 -*-
from odoo import models, fields

SPECIES = [
    "dog",
    "cat",
    "turtle",
    "hamster",
    "canary",
    "snake",
    "butterfly"
]

class Pet(models.Model):
    _name           = "pets"
    _description    = "Pets"
    _sql_constraints = [
        ("CHK_AGE", "CHECK (age < CURRENT_DATE)", "Your Pet must've been born on a valid date")
    ]

    # Required fields
    name = fields.Char(
        required    = True,
        string      = "Pet name"
    )
    species = fields.Selection(
        selection   = list(map(lambda s: (s, s.upper())), SPECIES),
        required    = True,
        string = "Species"
    )
    age = fields.Integer(
        required    = True,
        string      = "Pet age"
    )
    genre   = fields.Selection(
        selection = [
            ("male", "Male")
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
            ("street", "On the street")
            ("gift", "Was a gift")
            ("store", "I bought it")
        ],
        string = "Where did you get your pet?"
    )
    color = fields.Char(
        string = "Color of your pet"
    )
    get_date = fields.Date(
        string = "When did you get your pet?"
    )