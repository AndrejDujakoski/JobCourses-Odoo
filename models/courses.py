
from odoo import models, fields, api, _


class Courses(models.Model):
    _name = "model.courses"
    _description = "Info about Courses"

    teacher = fields.Many2one("model.teacher", ondelete='cascade', string="Course teacher")

    name = fields.Char(string="Name", required=True)

    field_of_study = fields.Char(string="Field of study")

    semester = fields.Selection(
        string="Semester",
        selection=[('first', 'I'),
                   ('second', 'II'),
                   ('third', 'III'),
                   ('fourth', 'IV'),
                   ('fifth', 'V'),
                   ('sixth', 'VI'),
                   ('seventh', 'VII'),
                   ('eighth', 'VIII')],
        help="Used to define the semester the course is taken in")

    state = fields.Selection(
        string="State",
        selection=[("draft", "Draft"),
                   ('open', "Open"),
                   ("finished", "Finished")],
        help="State of the course",
        default='draft')

    description = fields.Text(string="Description")

    beginning_date = fields.Date()
    end_date = fields.Date()

    students = fields.Many2many('model.student', string="Students")

    document = fields.Binary(string="Document")

    document_name = fields.Char(string="File Name")
    # ir attachment

    def change_status_open(self):
        if self.state == 'draft' or self.state == 'finished':
            print("sega state e: ", self.state)
            self.state = 'open'
            print("posle promena state e: ", self.state)

    def change_status_draft(self):
        if self.state == 'open' or self.state == 'finished':
            print("sega state e: ", self.state)
            self.state = 'draft'
            print("posle promena state e: ", self.state)

    def change_status_finished(self):
        if self.state == 'open':
            print("sega state e: ", self.state)
            self.state = 'finished'
            print("posle promena state e: ", self.state)

    def copy_course_draft(self, default=None):
        for record in self:
            print(record)
            if record.state == "finished":
                default = dict(default or {})
                default.update({
                    'students': None,
                    'state': 'draft',
                })
                copy = super(Courses, record).copy(default)
                view_id = record.env.ref('jobcourses.courses_form_view').id

                return {
                    'name': 'Copied Course',
                    'view_type': 'form',
                    'view_mode': 'form',
                    'res_model': 'model.courses',
                    'view_id': view_id,
                    'type': 'ir.actions.act_window',
                    'res_id': copy.id,
                    'target': 'current'
                }

    #inser_grades funkcija od tuka da se povikuva namesto da bidi action button da bidi object button
#     deff da se napraj funk ovde za wizardo
    def insert_grades(self):
        for student in self.students:
            print("student e: ", student)
        view = self.env.ref('jobcourses.insert_grades_form')
        print(view)
        print(self.name)
        wiz = self.env['transmodel.insertgrades'].create({'courseName': self.id})
        print(wiz)
        for record in self:

            return {
                'name': _('Grades Form'),
                'type': 'ir.actions.act_window',
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'transmodel.insertgrades',
                'views': [(view.id, 'form')],
                'view_id': view.id,
                'target': 'new',
                'res_id': wiz.id,
                'context': self.env.context,
            }


