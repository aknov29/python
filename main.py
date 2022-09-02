import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]
grades = np.array(data)
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]
student_data = np.array([study_hours, grades])
avg_study = student_data[0].mean()
avg_grade = student_data[1].mean()

print('Average study hours: {:.2f}\nAverage grade: {:.2f}'.format(avg_study, avg_grade))
df_students = pd.DataFrame({'Name': ['Dan', 'Joann', 'Pedro', 'Rosie', 'Ethan', 'Vicky', 'Frederic', 'Jimmie', 
                                        'Rhonda', 'Giovanni', 'Francesca', 'Rajab', 'Naiyana', 'Kian', 'Jenny',
                                        'Jakeem','Helena','Ismat','Anila','Skye','Daniel','Aisha'],
                                'StudyHours':student_data[0],
                                'Grade':student_data[1]})

df_students
df_students.iloc[0,[1,2]]
df_students.loc[0,'Grade']
df_students.loc[df_students['Name']=='Aisha']
df_students = df_students.dropna(axis=0, how='any')
passes  = pd.Series(df_students['Grade'] >= 60)
df_students = pd.concat([df_students, passes.rename("Pass")], axis=1)
df_students 
fig = plt.figure(figsize=(8,3))

plt.bar(x=df_students.Name, height=df_students.Grade, color='orange')
plt.title('Student Grades')
plt.xlabel('Student')
plt.ylabel('Grade')
plt.grid(color='#95a5a6', linestyle='--', linewidth=2, axis='y', alpha=0.7)
plt.xticks(rotation=90)

plt.show()