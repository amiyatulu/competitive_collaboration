### Generation of nodes 
from itertools import combinations
mainlabels = ['teacher','student','content','building' ]
## Generation of labels
all_labels = []
c = 0
for mlb in mainlabels:
	lb = []
	for x in range(4):
		lb.append('label' + str(c))
		c = c + 1
	all_labels.append(lb)



all_cdata = []
for labels in all_labels:
	cdata = []
	for n in range(1,5):
		data = combinations(labels, n)
		cdata.extend(data)
	all_cdata.append(cdata)


m = 0
for mlb in mainlabels: 
	y = 0
	for d in all_cdata[m]:
		s = list(d)
		for x in range(30):
			f = s.copy()
			f.insert(0,mlb +str(y))
			print(f)
			y = y + 1
	m = m + 1


