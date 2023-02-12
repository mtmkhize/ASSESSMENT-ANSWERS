Part A
import pandas as pd
import numpy as np

df_teacher = pd.DataFrame({
"name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
"married": [True, True, False, True],
"school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
"teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
"name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino","Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
"age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
"height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m', '2.1m']
})

teachers_list = []
for index, row in df_teacher.iterrows():
    teacher = {}
    teacher['name'] = row['name']
    teacher['married'] = row['married']
    teacher['school'] = row['school']
    teacher['students'] = []
    for student_index, student_row in df_student[df_student['teacher'] == row['name']].iterrows():
        student = {}
        student['name'] = student_row['name']
        student['age'] = student_row['age']
        student['height'] = student_row['height']
        teacher['students'].append(student)
    teachers_list.append(teacher)
print(teachers_list)

Part B

import pandas as pd
import numpy as np

df_teacher = pd.DataFrame({
"name": ["Pep Guardiola", "Jurgen Klopp", "Mikel Arteta", "Zinadine Zidane"],
"married": [True, True, False, True],
"school": ["Manchester High School", "Liverpool High School", "Arsenal High", np.nan]
})

df_student = pd.DataFrame({
"teacher": ["Mikel Arteta", "Mikel Arteta", "Pep Guardiola", "Jurgen Klopp", "Jurgen Klopp", "Jurgen Klopp", "Pep Guardiola","Pep Guardiola","Mikel Arteta"],
"name": ["Bukayo Saka", "Gabriel Martinelli", "Jack Grealish", "Roberto Firmino","Andrew Robertson", "Darwin Nunez", "Ederson Moraes", "Manuel Akanji", "Thomas Partey"],
"age": [21, 21, 27, 31, 28, 23, 29, 27, 29],
"height": ['2.1m','2.1m', '2.1m', '2.1m', '2.1m
