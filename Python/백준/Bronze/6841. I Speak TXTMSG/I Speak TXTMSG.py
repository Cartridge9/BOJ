dic = {"CU":"see you",
	   ":-)":"I’m happy",
	   ":-(":"I’m unhappy",
	   ";-)":"wink",
	   ":-P":"stick out my tongue",
	   "(~.~)":"sleepy",
	   "TA":"totally awesome",
	   "CCC":"Canadian Computing Competition",
	   "CUZ":"because",
	   "TY":"thank-you",
	   "YW":"you’re welcome",
	   "TTYL":"talk to you later"}
while 1:
	a = input()
	if a == "TTYL":
		print(dic[a])
		break
	if a not in dic:
		print(a)
	else:
		print(dic[a])