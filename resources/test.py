#Defining Subjects
subjects = ["EB101", "SI100", "SI120", "SI201", "SI250"]

turmas = [1,2,1,2,3]

subjects_with_turmas = []

sub = 0
turm = 0

while(sub < len(subjects)):
    if turmas[sub] == 1:
        subjects_with_turmas.append(subjects[sub])
    else:
        turm = 0
        strturma = 65
        while (turm < turmas[sub]):
            subjects_with_turmas.append(subjects[sub] + ' '+chr(strturma))
            strturma = strturma + 1
            turm = turm + 1
    sub = sub+1    

students = []

prereqs = ['EB101', 'SI100', 'SI120', 'SI201', 'SI250', 'SI100', 'SI100', 'SI120','SI201', 'SI100']

new_prereqs = []

newer_prereqs = []

#['EB101 A', 'SI100', 'EB101 B', 'SI100', 'SI120 A', 'SI201', 'SI120 B', 'SI201', 'SI250 A', 'SI100', 'SI250 B', 'SI100', 'SI100', 'SI120', 'SI201 A', 'SI100', 'SI201 B', 'SI100']
laco = 1

while (laco < len(prereqs)):
	subject_to_have_new_prereq = prereqs[laco]
	index_holder_to_match_turmas = subjects.index(subject_to_have_new_prereq)
	if turmas[index_holder_to_match_turmas] == 1:
		new_prereqs.append(prereqs[laco-1])
		new_prereqs.append(prereqs[laco])
	else:
		x = 0
		turm = 65
		while (x < turmas[index_holder_to_match_turmas]):
			new_prereqs.append(prereqs[laco-1] + ' '+chr(turm))
			new_prereqs.append(prereqs[laco])
			turm = turm+1
			x = x +1
	laco = laco + 2

laco2 = 1

while(laco2 < len(new_prereqs)):
	sub_with_prereq = new_prereqs[laco]
	index_holder_to_match_turmas = subjects.index(subject_to_have_new_prereq)
	if turmas[index_holder_to_match_turmas] == 1:
		newer_prereqs.append(new_prereqs[laco2-1])
		newer_prereqs.append(new_prereqs[laco2])
	else:
		x = 0
		turm = 65
		while (x < turmas[index_holder_to_match_turmas]):
			newer_prereqs.append(new_prereqs[laco2-1])
			newer_prereqs.append(new_prereqs[laco2]  + ' ' + chr(turm))
			turm = turm+1
			x = x+1
	laco2 = laco2 + 2








print(newer_prereqs)