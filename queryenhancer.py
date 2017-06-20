import re

def punctuationTrim (word):
	word = re.sub('["]', '', word)
	word = re.sub('[,]', ' ', word)
	word = re.sub('  ', ' ', word)
	return word

#enhance the query in order to search online for it
def enhanceQuery(query):
	query=punctuationTrim(query)
	query=query.replace(" ","%20") #adequate the query to put it in the url
	return query