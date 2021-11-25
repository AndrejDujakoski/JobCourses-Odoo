from odoo import models, fields, api, _


class InsertGrades(models.Model):
    _name = 'model.grades'
    _description = "Info about the grades FROM MODEL.GRADES"

    # student = fields.Many2one("model.student", string="Students", readonly=True)
    #
    # course_name = fields.Char(string="Name of Course", default="test")
    #
    # grade_value = fields.Char(string="Grade for the course", readonly=True, default="10")

    course_name = fields.Many2one("model.courses", ondelete="cascade",
                                  string="Course TEST")

    grade_value = fields.Selection(string="Grade TEST",
                             selection=[
                                 ("5", "5"),
                                 ("6", "6"),
                                 ("7", "7"),
                                 ("8", "8"),
                                 ("9", "9"),
                                 ("10", "10")],
                             help="Grades of the students")

    student = fields.Many2one("model.student", string="Student")


