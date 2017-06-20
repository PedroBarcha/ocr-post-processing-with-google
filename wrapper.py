import string

#Chops the given file into phrases with "chop_size", that will later be sent as queries to google,
#returning: (first parameter=words matrix, second=list of phrases(strings)).
#Attention: chop is done between spaces, so "would , you come, son?", yields:
#[would],[,],[you],[come,],[son?].
#For this reason, chopps like the [,] don't count to the chop_size

def textWrap(file,chop_size):
	chops_list=[]
	chops_list_joint=[]
	chop_aux=[]
	words_count=0

	with open (file) as document:
		for line in document:
			for word in line.split(): #for every word
				chop_aux.append(word)
				if (word not in string.punctuation):
					words_count=words_count+1
				if (words_count == chop_size): #phrase complete
					chops_list.append(chop_aux)
					chop_aux=' '.join(chop_aux)
					chops_list_joint.append(chop_aux)
					del chop_aux
					chop_aux=[]
					words_count=0

	#add last chopped phrase to the chops list
	chops_list.append(chop_aux)
	chop_aux=' '.join(chop_aux)
	chops_list_joint.append(chop_aux)
	
	return (chops_list,chops_list_joint)

