querries=int(input())
i=0
s1=list()
s2=[]
for i in range(querries):
	choice=list(input().split())
	if int(choice[0])==1:
		if not s1:
			s1.append(int(choice[1]))
			s2.append(int(choice[1]))
		else:
			s1.append(int(choice[1]))
			if s2[-1]<=int(choice[1]):
				s2.append(int(choice[1]))
	if int(choice[0])==2:
		if s1[-1]==s2[-1]:
			s1.pop()
			s2.pop()
		else:
			s1.pop()
	if int(choice[0])==3:
		print(s2[-1])