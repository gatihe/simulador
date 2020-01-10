```python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
```


```python
#defining parameters
bast_param = [0,5] #ba prefix for below average student
avst_param = [5,7] #av prefix for average student
aast_param = [7,10] #aa prefix for above average student


#students quantities per parameter
bast_qtd = 5
avst_qtd = 3
aast_qtd = 8
st_total = bast_qtd + avst_qtd + aast_qtd

#Defining Subjects
subjects = ["Disciplina 1", "Disciplina 2", "Disciplina 3", "Disciplina 4", "Disciplina 5"]

students = []

#counter for students ids creation
i = 0

#counters and variable for grades creation
a = 0
b = 0
newgradeline = []

grade = []

#creating students and grades
while(i < st_total):
    newstudent = random.randint(100000,199999)
    #excluding duplicates
    if newstudent not in students:
        students.append(newstudent)
        i = i+1    

```


```python
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
```


```python
#generating table
simulation = pd.DataFrame (grade,index=students, columns=subjects)

simulation
```




<div>
<table class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Disciplina 1</th>
      <th>Disciplina 2</th>
      <th>Disciplina 3</th>
      <th>Disciplina 4</th>
      <th>Disciplina 5</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>129328</td>
      <td>3.41</td>
      <td>2.45</td>
      <td>3.04</td>
      <td>0.17</td>
      <td>1.87</td>
    </tr>
    <tr>
      <td>133024</td>
      <td>3.52</td>
      <td>1.00</td>
      <td>1.93</td>
      <td>0.89</td>
      <td>2.82</td>
    </tr>
    <tr>
      <td>185185</td>
      <td>2.58</td>
      <td>1.77</td>
      <td>2.42</td>
      <td>3.81</td>
      <td>1.34</td>
    </tr>
    <tr>
      <td>121082</td>
      <td>4.37</td>
      <td>3.04</td>
      <td>4.08</td>
      <td>2.89</td>
      <td>2.27</td>
    </tr>
    <tr>
      <td>174883</td>
      <td>0.32</td>
      <td>4.98</td>
      <td>1.16</td>
      <td>3.95</td>
      <td>1.78</td>
    </tr>
    <tr>
      <td>155360</td>
      <td>5.77</td>
      <td>5.93</td>
      <td>5.35</td>
      <td>6.22</td>
      <td>5.88</td>
    </tr>
    <tr>
      <td>163326</td>
      <td>6.17</td>
      <td>6.49</td>
      <td>5.71</td>
      <td>6.83</td>
      <td>5.49</td>
    </tr>
    <tr>
      <td>132134</td>
      <td>6.64</td>
      <td>6.56</td>
      <td>6.86</td>
      <td>5.18</td>
      <td>5.04</td>
    </tr>
    <tr>
      <td>190200</td>
      <td>8.38</td>
      <td>7.62</td>
      <td>7.14</td>
      <td>7.94</td>
      <td>9.80</td>
    </tr>
    <tr>
      <td>134368</td>
      <td>8.51</td>
      <td>7.33</td>
      <td>8.79</td>
      <td>9.37</td>
      <td>7.03</td>
    </tr>
    <tr>
      <td>138307</td>
      <td>9.94</td>
      <td>8.89</td>
      <td>9.77</td>
      <td>8.78</td>
      <td>9.74</td>
    </tr>
    <tr>
      <td>159817</td>
      <td>9.31</td>
      <td>7.44</td>
      <td>9.50</td>
      <td>9.81</td>
      <td>8.16</td>
    </tr>
    <tr>
      <td>110245</td>
      <td>9.45</td>
      <td>7.63</td>
      <td>9.97</td>
      <td>8.02</td>
      <td>9.57</td>
    </tr>
    <tr>
      <td>178953</td>
      <td>7.51</td>
      <td>9.68</td>
      <td>8.95</td>
      <td>8.89</td>
      <td>9.79</td>
    </tr>
    <tr>
      <td>130701</td>
      <td>9.78</td>
      <td>8.22</td>
      <td>7.35</td>
      <td>7.84</td>
      <td>7.08</td>
    </tr>
    <tr>
      <td>106483</td>
      <td>8.65</td>
      <td>7.49</td>
      <td>9.81</td>
      <td>7.31</td>
      <td>8.00</td>
    </tr>
  </tbody>
</table>
</div>
