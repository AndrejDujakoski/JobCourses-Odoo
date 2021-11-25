# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = "student.model"
    _description = "Info about students"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    enrolled_year = fields.Char(required=True)
    birth_date = fields.Date()
    index_number = fields.Char(string='Index number', readonly=True, default='Index')
    field_of_study = fields.Char('Field of Study')

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


class Courses(models.Model):
    _name = "courses.model"
    _description = "Info about Courses"

    name = fields.Char(string="Name", required=True)
    teacher = fields.Many2one("teacher.model")
    field_of_study = fields.Char(string="Field of study")
    semester = fields.Selection(string="Semester", selection=[('first', 'I'), ('second', 'II'), ('third', 'III'),
                                ('fourth', 'IV'), ('fifth', 'V'), ('sixth', 'VI'), ('seventh', 'VII'),
                                ('eighth', 'VIII')],
                                help="Used to define the semester the course is taken in")

    state = fields.Selection(string="State", selection=[('open', "Open"), ("finished", "Finished"), ("draft", "Draft")]
                             , help="State of the course", default='draft')

    description = fields.Text(string="Description")
    beginning_date = fields.Date()
    end_date = fields.Date()
    students = fields.Many2many('student.model', string="Students")

    document = fields.Binary(string="Document")
    document_name = fields.Char(string="File Name")
    # ir attachment

    def change_status_open(self):
        self.state = 'open'

    def change_status_draft(self):
        self.state = 'draft'
        # self.teacher.readonly = True

    def change_status_finished(self):
        self.state = 'finished'

    def insert_grades(self):
        return {
            'name': 'Insert Grades',
            'domain': [],
            # ovde res model da se zameni so nov model so ce gi dava sutentite na kurso
            # i samo za niv da mozi da se menuva grades, to znaci deka ce treba da ima
            # relacii so koj so ce se znaj koj studenti se zapisani
            'res_model': 'insertgrades.model',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'context': {},
            'target': 'new',
        }

# create a view for this and a tree form se ko so treba
# On click on Insert Grades a pop up should be shown
# where you can insert the grades for every student that
# was in the course.
class InsertGrades(models.Model):
    _name = "insertgrades.model"
    _inherit = Courses
    # prajme _inherit za da mozi da se zema studentite nekako od kurso
    students = Courses.students



class Teacher(models.Model):
    _name = "teacher.model"
    _description = "Info about teachers"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    email = fields.Char('Email', required=True)

    courses = fields.Many2many("courses.model", string="Courses Teaching")
    # one to many
