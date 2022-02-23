import sqlite3
import random

from PyQt5.QtWidgets import QMainWindow, QFileDialog
from PyQt5 import uic
from error import Error
from unfaithful import Unfaithful
from docx import Document


class task_generator(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('tasks.ui', self)
        self.con = sqlite3.connect('Tesks.db')
        self.cur = self.con.cursor()

        self.Run.clicked.connect(self.run)
        self.save.clicked.connect(self.Save)
        self.back.clicked.connect(self.Back)
        self.file.clicked.connect(self.File)

        self.list_first = [self.label_3, self.label_4, self.first_min, self.first_max,
                           self.first_whole, self.first_material]
        for i in self.list_first:
            i.hide()
        self.save.hide()
        self.file.hide()

    def run(self):
        task_text = self.tasks_text.text()
        if task_text.count('&') % 2 != 0:
            self.Error()
        elif task_text.count('&') // 2 > 1:
            self.Error()
        else:
            self.lst_text_task = task_text.split()
            task_text = list(task_text)
            self.lst_variables = []
            for i in range(task_text.count('&') // 2):
                a1 = task_text.index('&')
                del task_text[a1]
                a2 = task_text.index('&')
                del task_text[a2]
                self.lst_variables.append(''.join(task_text[a1:a2]))
            for i in self.lst_variables:
                if len(i) == 0:
                    self.Error()
            for i in range(len(self.lst_variables)):
                if i == 0:
                    for j in self.list_first:
                        j.show()
                    self.first_variable.setText(self.lst_variables[i])
            for i in range(len(self.lst_text_task)):
                if self.lst_text_task[i].count('&') == 2:
                    a = list(self.lst_text_task[i])
                    del a[0]
                    del a[-1]
                    self.lst_text_task[i] = ''.join(a)
            self.change = self.lst_text_task.copy()
            self.save.show()

    def Save(self):
        self.RadioButten()
        self.Formula()
        self.MinMax()



    def Formula(self):
        a = self.formula.text()
        if a == '':
            self.Error()
        self.lst_formula = list(a.split())
        self.check = ['*', '/', '-', '+']
        for i in self.lst_variables:
            self.check.append(i)
            if i not in self.lst_formula:
                self.Unfaithful()
        for i in self.lst_formula:
            if i not in self.check:
                if not i.isdigit():
                    self.Unfaithful()
                else:
                    self.check.append(i)
        self.change_formula = self.lst_formula.copy()

    def RadioButten(self):
        count = 0
        lst_buttengroup = [[self.first_whole, self.first_material]]
        for i in range(len(self.lst_variables)):
            a = lst_buttengroup[i]
            for j in a:
                if j.isChecked():
                    count += 1
            if count != 1:
                self.Unfaithful()
            else:
                count = 0
        self.sign = []
        if len(self.lst_variables) == 0:
            self.Unfaithful()
        for i in range(len(self.lst_variables)):
            a = lst_buttengroup[i]
            if a[0].isChecked():
                self.sign.append(True)
            else:
                self.sign.append(False)

    def MinMax(self):
        self.variables = []
        lst_spinbox = [[self.first_min, self.first_max]]

        for i in range(len(self.lst_variables)):
            a = lst_spinbox[i]
            a1 = float(a[0].text().replace(',', '.'))
            a2 = float(a[1].text().replace(',', '.'))
            if a1 == a2 or a1 > a2:
                self.Error()
            elif len(self.lst_formula) == 0:
                self.Error()
            elif len(set(self.check) & set(self.lst_formula)) != len(self.lst_formula):
                self.Error()
            else:
                self.cur.execute("""DELETE from tacks""")
                self.variables.append([a1, a2])
                self.a = int(self.spinBox.text())

                for i in range(self.a):
                    for j in range(len(self.lst_variables)):
                        self.Formula()
                        if not self.variables:
                            self.Error()
                        else:
                            b = self.variables[j][0]
                            c = self.variables[j][1]
                            if j == 0:
                                if self.sign:
                                    self.num1 = random.randint(int(b), int(c))
                                else:
                                    self.num1 = round(random.uniform(b, c), 3)
                                self.lst_text_task[self.lst_text_task.index(self.lst_variables[0])] = str(self.num1)
                                self.lst_formula[self.lst_formula.index(self.lst_variables[0])] = self.num1

                        self.lst_text_task = list(map(str, self.lst_text_task))
                        self.lst_formula = list(map(str, self.lst_formula))
                        lst = [(' '.join(self.lst_text_task), str(eval(' '.join(self.lst_formula))))]

                        self.cur.executemany("INSERT INTO tacks VALUES (?, ?)", lst)
                        self.con.commit()
                        self.lst_text_task = self.change.copy()
                        self.lst_formula = self.change_formula.copy()
                        self.file.show()

    def File(self):
        a = self.cur.execute("""SELECT text FROM tacks""").fetchall()
        b = self.cur.execute("""SELECT ans FROM tacks""").fetchall()
        fname = QFileDialog.getSaveFileName()
        fname = fname[0]
        for i in range(self.a + 1):
            if i == 0:
                for j in range(self.a):
                    if j == 0:
                        self.document = Document()
                        self.document.add_heading(f'Ответы', level=1)
                        self.document.add_paragraph(f'{j + 1} - {b[j]}')
                        self.document.save(fname)
                    else:
                        self.document = Document(fname)
                        self.document.add_paragraph(f'{j + 1} - {b[j]}')
                        self.document.save(fname)
            else:
                self.document = Document(fname)
                self.document.add_paragraph()
                self.document.add_page_break()
                self.document.add_heading(f'Вариант {i}', level=1)
                self.document.add_paragraph(a[i - 1])
                self.document.save(fname)


    def Unfaithful(self):
        self.fourth = Unfaithful()
        self.fourth.show()

    def Error(self):
        self.fourth = Error()
        self.fourth.show()

    def Back(self):
        self.hide()