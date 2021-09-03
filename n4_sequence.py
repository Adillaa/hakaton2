#to chto imeem

sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = (14,10,35,45,'60',70,90,0,105,150,'70')
sequence_2 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0)
sequence_3 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70')

#perevod v set
seq1=set(sequence_0)
seq2=set(sequence_1)
seq3=set(sequence_2)
seq4=set(sequence_3)

a=0

#sravnit
def srv(first, second,third,fourth):
	n=len(first)
	new=seq1.difference(second)
	new2=seq1.difference(third)
	new3=seq1.difference(fourth)
	n2=len(new)
	n3=len(new2)
	n4=len(new3)
	if n==n2 and n==n3 and n==n4:
		print("unikalno")
	else:
		print("ne unikalen")
#tech

srv(seq1,seq2,seq3,seq4)
srv(seq2,seq1,seq3,seq4)
srv(seq3,seq1,seq2,seq4)
srv(seq4,seq1,seq2,seq3)
