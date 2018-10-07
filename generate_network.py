### Generation of nodes 
from itertools import combinations
labels = ['label0', 'label1', 'label2','label3']
mainlabels = ['teacher','student','content','building' ]
cdata = []
for n in range(1,5):
	data = combinations(labels, n)
	cdata.extend(data)

for mlb in mainlabels: 
	for d in cdata:
		s = list(d)
		for x in range(30):
			f = s.copy()
			f.insert(0,mlb +str(x))
			print(f)


