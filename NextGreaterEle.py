

def NextGreaterElement(array):
	NGElist=[]
	element=0
	next=0
	
	length=len(array)
	NGElist.append(array[0])
	
	for i in range(1,length,1):
		next=array[i]
		if len(NGElist):
			element = NGElist.pop()
			while element < next :
				print (str(element)+"----"+str(next))
				if len(NGElist)==0:
					break
				element = NGElist.pop()
			if element > next:
				NGElist.append(element)
		NGElist.append(next)

	while len(NGElist):
		element = NGElist.pop()
		next = -1
		print(str(element) + "---- " + str(next))




input_array=raw_input("Enter your input array elements separated by \",\" \n")
array=map(int,input_array.split(","))
NextGreaterElement(array)
			
