'''
Laba 3
'''
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

def extract_year(row):
    '''
    Количество курсов по годома
    '''
    year = datetime.fromisoformat(row['published_timestamp'].replace('Z', '').replace('T',' ')).year
    row['published_timestamp'] = year
    return row
df = pd.read_csv('udemy_courses.csv')
df = df.apply(extract_year,axis=1)
task1 = df.groupby('published_timestamp')['course_id'].count()
task2 = df.groupby('level')['course_id'].count()
print(task1,task2)
task1 = list(dict(task1).items())
task2 = list(dict(task2).items())
task1_x = list(dict(task1).keys())
task1_h = [dict(task1)[x] for x in task1_x]
task2_x = list(dict(task2).keys())
task2_h = [dict(task2)[x] for x in task2_x]
fig, ax = plt.subplots(2)
ax[0].bar(task1_x,height=task1_h)
ax[1].bar(task2_x,height=task2_h)
plt.show()
