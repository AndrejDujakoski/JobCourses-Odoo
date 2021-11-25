from odoo import models, fields, api, _


class InsertGrades(models.TransientModel):
    _name = 'transmodel.insertgrades'
    _description = "Info about the grades"

    courseName = fields.Many2one("model.courses", ondelete="cascade",
                                  string="Course")

    grade = fields.Selection(string="Grade",
                             selection=[
                                 ("5", "5"),
                                 ("6", "6"),
                                 ("7", "7"),
                                 ("8", "8"),
                                 ("9", "9"),
                                 ("10", "10")],
                             help="Grades of the students")

    student = fields.Many2one("model.student", string="Student")

    def insert_grades_btn(self):

        # grades = self.env['model.grades'].browse(self._context.get('active_ids'))

        # grades = self.env['model.grades'].create(
        #     {'course_name': self.courseName,
        #      'grade_value': self.grade,
        #      'student': self.student
        #      })

        grades = self.env['model.grades'].create({})

        print("novata promenliva grades e: ", grades)

        grades.write({
            'grade_value': self.grade,
            'course_name': self.courseName,
            'student': self.student,
        })



        # for grade in self.student.grades:
        #     if grade.course_name.id == self.course_name.id:
        #         grade.grade = self.grade
        # active id
        # domain


