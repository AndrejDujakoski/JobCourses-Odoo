from odoo import models, fields, api


class Teacher(models.Model):
    _name = "model.teacher"
    _description = "Info about teachers"

    name = fields.Char(string="Name", required=True)

    surname = fields.Char(string="Surname", required=True)

    email = fields.Char('Email', required=True)

    courses = fields.One2many("model.courses", 'teacher', string="Courses Teaching")


