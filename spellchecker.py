#correctedQuery = Google's "did you mean?"
####TODO######
#Move cx and apy_key to global configs

import urllib2
import queryenhancer

API_key=""

cx="017534179585087163853:5lebqajxk1c" #The identifier of google's Custom Search Engine.

#with the index of the "correctedQuery", we can find the "did you mean" suggestion (located at the following indexes).
#the words yielded by "did you mean" are put into corrected_query. The last world is indicated by a comma at its end.
def getCorrectedQuery(list_of_words,index):
	i=0
	corrected_query=[]
	while True:
		corrected_query.append(list_of_words[index+i+1])
		if ((list_of_words[index+i+1].endswith(','))==False): #while there are still words
			i=i+1
		else:
			break

	#enhance the string
	enhanced_corrected_query=' '.join(corrected_query) #turn everything into a single string
	enhanced_corrected_query=queryenhancer.punctuationTrim(enhanced_corrected_query)

	return enhanced_corrected_query


def spellCheck(query):
	#search the query online
	search_result=urllib2.urlopen("https://www.googleapis.com/customsearch/v1?key="+API_key+"&cx="+cx+"&q="+query).read()

	#breaks text in words in order to search for the "correctedQuery" field, which indicates spell mistake
	list_of_words=search_result.split()

	#if there is a spell mistake, takes "correctedQuery" index among the words
	try:
		index=list_of_words.index('"correctedQuery":')
	except ValueError:
		return -1 #no spell mistake

	#if there is a spell mistake, the "did you mean" suggestion must be find after "correctedQuery" field
	return getCorrectedQuery(list_of_words,index)