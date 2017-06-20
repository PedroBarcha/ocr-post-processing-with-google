import spellchecker
import queryenhancer
import wrapper

###TODO####
#put this variable in config
words_per_query=5 #text will be chopped with this value

#wrapper turns file text into queries for google
queries,queries_strings=wrapper.textWrap("texts/a041.txt",words_per_query)

corrected_queries=[]
#checks every query online and substitutes google's suggestions for the former phrases
for i in range (0,len(queries_strings)):
	queries_strings[i]=queryenhancer.enhanceQuery(queries_strings[i]) #makes query ready for Google's search
	print (queries_strings[i])
	corrected_queries.append(spellchecker.spellCheck(queries_strings[i]))
	print (corrected_queries[i])

	#TODO
	#if (corrected_queries[i]==-1)
		#no correction to be done
	#else #replace the corrected_query for the query
		#replace()
