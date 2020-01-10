import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random



params_sort = [0, 5, 10, 5, 7, 10, 7, 10, 10]

print(params_sort)

j = 2
grade = []
subjects = ["Disciplina 1", "Disciplina 2", "Disciplina 3", "Disciplina 4", "Disciplina 5"]


while(j<len(params_sort)):
	a = 0
	while(a < params_sort[j]):
		b = 0
		newgradeline = []
		grade.append(newgradeline)
		while(b < len(subjects)):
			gen_grade = round(random.uniform(params_sort[j-2],params_sort[j-1]),2)
			newgradeline.append(gen_grade)
			b = b +1
		a = a +1
	print("saiu")
	j = j + 3

print(grade)




# In[3]:


#below averagge students
while (a < bast_qtd):
    b = 0
    newgradeline = []
    grade.append(newgradeline)
    while (b<len(subjects)):
        gen_grade = round(random.uniform(bast_param[0],bast_param[1]),2)
        newgradeline.append(gen_grade)
        b = b+1
    a = a +1
a = 0

#average students
while (a < avst_qtd):
    b = 0
    newgradeline = []
    grade.append(newgradeline)
    while (b<len(subjects)):
        gen_grade = round(random.uniform(avst_param[0],avst_param[1]),2)
        newgradeline.append(gen_grade)
        b = b+1
    a = a +1
a = 0

#above average students
while (a < aast_qtd):
    b = 0
    newgradeline = []
    grade.append(newgradeline)
    while (b<len(subjects)):
        gen_grade = round(random.uniform(aast_param[0],aast_param[1]),2)
        newgradeline.append(gen_grade)
        b = b+1
    a = a +1
