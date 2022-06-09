'''
Name: George Liu


#Use sets to check for repetition, lists to change/mutate, and dictionaries to sort.
wordList=list()
allWords=set()
currentWords=set()
currentDigit=0
indexReal=dict()
valueList=list()

f='editorsNotes.txt' #replace editorsNotes with whatever file is being read.
source=file(f)

for line in source:
    data=line.split()
    
    if data[0].isdigit()==True: #if we are reading a line with the page number
        try: #add contents of all inputs/words below last digit to a list. use try since this won't work on first iteration.
            if wordList[currentDigit-1]==0: #If no previous entry to the page number, replace the value(s)
                wordList[currentDigit-1]=addList 
                allWords=allWords.union(currentWords) #Keep track of all used inputs to ensure no repeats
                currentWords=set() #Reset the list of words for the next page number
                
                
            else: #If there is a previous input to the page number, append the value(s)
                wordList[currentDigit-1]=wordList[currentDigit-1]+addList
                allWords=allWords.union(currentWords) #Keep track of all used inputs to ensure no repeats
                currentWords=set() #Reset the list of words for the next page number
                
                          
        except IndexError: #Wlil show an error on the first time through, so we ignore it.
            pass
        
        currentDigit=int(data[0]) # This is a counter that keeps track of the page number
        for i in range(int(data[0])): #Creates a list of 0's that will always be larger than the total # of pages.
            currentDigit=int(data[0]) #List values correspond to page number (index[0]->page1, index[1]->page2, etc.)
            wordList.append(0)#0's indicate no entry for that particular page number.
    else:
    #if we are reading a line with an entry/word.
        wordEntry=line.strip('\n') 
        currentWords.add(wordEntry.lower()) 
        addSet=currentWords
        #.difference(allWords) #If you wanted to create a list of list with no repeats then use this set method
        addList=sorted(addSet)
        
#The last group of inputs will not be added since there is no next page number. Therefore, we add these inputs manually. 
if wordList[currentDigit-1]==0:
    wordList[currentDigit-1]=addList
    currentWords=set()
    allWords=allWords.union(currentWords)
else:
    wordList[currentDigit-1]=wordList[currentDigit-1]+addList
    allWords=allWords.union(currentWords)
    currentWords=set()
    
# print wordList  check to see if the wordList matches up with page number/inputs.

allWords=sorted(allWords)
allWordsList=list(allWords)
# print allWordsList use to check

# Create a dictionary that lines up word inputs with their respective page number(s)
for i in allWordsList: # Iterate through a list of lists using two for loops
    for j in range(len(wordList)):
        if wordList[j]==0: #If there is no input, ignore
            pass
        else:
            if i in wordList[j]:
                valueList.append(j+1)
    indexReal[i]=tuple(valueList) #We convert to a tuple since dictionaries with list values must be tuples
    valueList=[]

source.close()

#Double-check to see if our results are correct.
pageNum=indexReal.keys()
pageNum.sort()
for value in pageNum:
    print value,str(indexReal[value]).strip("()").strip(',')

# Create a file with our results in it.
Index=file('Index.txt','w')
pageNum=indexReal.keys()
pageNum.sort()
for value in pageNum:
    writeString=(str(value)+' '+str(indexReal[value]).strip("()").strip(',')) #clean up the formatting
    Index.write(writeString)
    Index.write('\n')
Index.close()


