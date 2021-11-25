from odoo import models, fields, api


class Student(models.Model):
    _name = "model.student"
    _description = "Info about students"

    name = fields.Char(string="Name", required=True)

    surname = fields.Char(string="Surname", required=True)

    email = fields.Char(string="Email", required=True)

    enrolled_year = fields.Char(required=True)

    birth_date = fields.Date()

    index_number = fields.Char(string='Index number', readonly=True, default='Index')

    field_of_study = fields.Char('Field of Study')

    grades = fields.One2many("model.grades", 'student',
                             string="Student Grades", readonly=True)

    @api.model
    def create(self, vals):
        if vals.get('index_number', 'Index') == 'Index':
            vals['index_number'] = self.env['ir.sequence'].next_by_code('index.model.sequence') or '000/0000'
            enrolled = vals.get('enrolled_year')
            student_index = vals['index_number'].strip()
            vals['index_number'] = student_index
            vals['index_number'] += "/"
            vals['index_number'] += enrolled
        result = super(Student, self).create(vals)
        return result


