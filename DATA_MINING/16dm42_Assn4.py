#Danielle Mott, March 2017
#This program takes four text files (speeches) and analyzes them.
#It displays the number of characters, words, and unique words.
#It also displays the occurrences of the word "I" as a percent of the total words.
#It shows the user the longest word. It also shows the user what percent of the words are unique.
#It writes to four new text files with a list of the unique words and their respective occurences.
#The most used word over 5 letters that occurs in all four speeches is "people".
#This program assumes that a string has been provided to it for a filename. It also assumes the text files
#that are being opened are in the same folder as the program.

'''Takes the name of a text file as a string and returns the contents of the file as a string.'''

def openFile(filename) : 
    fileIn = open(filename)
    fileString = fileIn.read()
    fileIn.close()
    return fileString

'''Takes a string and returns a string with no hyphens.'''
    
def removeHyphens(fileString) :
    return fileString.replace("-", " ")

'''Takes a string and returns a string where all line termination characters have been removed.'''

def removeLineTermination(fileString) :
    return fileString.replace("\n", " ")

'''Takes a string and returns a string where all non-single spaces have been turned into a single spaces'''

def removeDoubleSpaces(fileString) :
    while fileString.count("  ") > 0 :
        fileString = fileString.replace("  ", " ")
    return fileString

'''Accepts a string and changes all uppercase letters to lowercase letters.'''

def toLowerCase(fileString) :
    return fileString.lower()
 
'''Accepts a string and counts the exclamation marks, periods, and question marks. Returns the sum of the three.'''

def countSentences(cleanFileString) :
    numPeriod = cleanFileString.count(".")
    numExcMark = cleanFileString.count("!")
    numQuestMark = cleanFileString.count("?")
    return numPeriod + numExcMark + numQuestMark

'''Accepts a string and returns the string with no punctuation.'''

def removePunct(cleanFileString) :
    clean = ""
    for i in cleanFileString :
        if i.isalpha() or i == " " :
            clean += i
    return clean

'''Accepts a list of words and returns the number of elements (words) in the list.'''

def countWords(noPunctStrSplit) :
    numCount = 0
    for i in noPunctStrSplit :
        if i.isalpha() :
            numCount += 1
    return numCount

'''Accepts a string and returns the number of unique words in the string.'''

def countUniqueWords(noPunctStr) :
    noPunct = noPunctStr.split()
    noPunctList = list(set(noPunct))
    numCount = 0
    for i in noPunctList :
        if i.isalpha() :
            numCount += 1
    return numCount

'''Accepts the speech as a string and returns the number of times "I" appears.'''

def countI(plainSpeech) :
    speechList = plainSpeech.split()
    numCount = 0
    for i in speechList :
        if i == 'I' :
            numCount += 1
    return numCount

'''Accepts a list of words and returns the longest word(s).'''

def determineLongWord(noPunctStrSplit) :
    lengthMax = 0
    wordMax = ""
    for i in noPunctStrSplit :
        if len(i) > lengthMax :
            lengthMax = len(i)
            wordMax = i
        elif len(i) == lengthMax :
            if i not in wordMax :
                wordMax = wordMax + " and " + i
    return wordMax

'''Forms a dictionary from a list of words where the key is the word and the value is the number of occurences of the word.'''

def countOccurenceUniqueWord(noPunctStrSplit) :
    newDict = {}
    for i in noPunctStrSplit :
        if i in newDict :
            newDict[i] += 1
        else :
            newDict[i] = 1
    return newDict

'''Sorts a dictionary alphabetically and returns the dictionary as a string.'''
 
def createString(newDict) :
    myStr = ""
    for i in sorted(newDict) :
        if i.isalpha() :
            myStr += i + " "
            myStr += str(newDict[i])
            myStr += '\n'
    return myStr

'''Accepts a string and a filename (as a string) and then writes the string to the file with that name.'''

def writeToFile(dictAsStr, fileToWriteTo) :
    fileIn = open(fileToWriteTo, 'w')
    fileIn.write(dictAsStr)
    fileIn.close()

'''Accepts a list of words in the speech and returns list of words over 5 letters.'''

def calcBigWord(noPunctStrSplit) :
    bigWords = []
    for i in noPunctStrSplit :
        if len(i) > 5 and i.isalpha() :
            bigWords += [i]
    return bigWords

'''Accepts a list of words over 5 letters and returns a dictionary of "word : number" pairs.'''
    
def makeDict(bigWordList) :
    bigWordDict = {}
    for i in bigWordList :
        if i in bigWordDict :
            bigWordDict[i] += 1
        else :
            bigWordDict[i] = 1
    return bigWordDict

'''Takes a dictionary of "word : number" pairs and sorts the dictionary by key value. It iterates through it backwards and
   displays the ten words that occur the most often.'''

def generate10Word(bigWordDict) :
    j = 0
    myStr = ""
    for i in reversed(sorted(bigWordDict, key=bigWordDict.get)) :#sorts the dictionary by key value and iterates through it backwards
        if j < 10 :
            myStr += str(i) +": " + str(bigWordDict[i]) + " times" + "\n"
        j += 1
    return myStr

 '''Stores the information returned by the functions that needs to be displayed.'''

def invokeFcn(filename) :
    displayFileName = filename.replace(".txt", "")
    length = len(openFile(filename))
    print(f"Number of characters: {length}")
    noHyphens = removeHyphens(openFile(filename))
    noLineTerm = removeLineTermination(noHyphens)
    noUpperCase = toLowerCase(noLineTerm)
    cleanSpeech = removeDoubleSpaces(noUpperCase) #string with no hyphens, line termination characters, or double spaces
    numSentences = countSentences(cleanSpeech)
    print("Number of sentences:", numSentences)
    stringNoPunct = removePunct(cleanSpeech)
    stringNoPunctSplit = stringNoPunct.split()
    numWords = countWords(stringNoPunctSplit)
    print("Number of words:", numWords)
    numUniqueWords = countUniqueWords(stringNoPunct)
    print("Number of unique words:", numUniqueWords)
    print(f"{(100 * (numUniqueWords / numWords)):.1f}% of the words are unique.")
    speech = openFile(filename)
    numIs = countI(speech)
    print(f'{(100 * (numIs / numWords)):.2f}% of the words are "I".')
    longestWord = determineLongWord(stringNoPunctSplit)
    print(f'Longest word(s): {longestWord}')
    newDictionary = countOccurenceUniqueWord(stringNoPunctSplit)
    newDictAsStr = createString(newDictionary)
    fileToWriteTo = filename.replace(".txt", "Occurences.txt") #The file written to is called filenameOccurences
    writeToFile(newDictAsStr, fileToWriteTo)
    print(f"There has been a text file created called '{displayFileName}Occurences' that includes each unique word in the speech and its number of occurences.")
    #For bonus part
    myListBigWord = calcBigWord(stringNoPunctSplit)
    myDictionaryBigWord = makeDict(myListBigWord)
    listOfFrequentWords = generate10Word(myDictionaryBigWord)
    print("Here are the 10 words over the length of 5 letters that occur the most often:")
    print(listOfFrequentWords)

def main() :
    fileName = "PMHarperBerlinWall.txt"
    print("This is the analysis for Prime Minister Harper's 2009 speech about the fall of the Berlin Wall: ")
    try :
        invokeFcn(fileName)
    except OSError :
        print("There has been a problem opening or reading your file.")
    except ValueError :
        print("There has been a problem opening or reading your file.")
    SecondFile =  "PresObamaBerlinSpeech.txt"
    print("This is the analysis for Senator Obama's 2008 speech in Berlin.")
    try :
        invokeFcn(SecondFile)
    except OSError :
        print("There has been a problem opening or reading your file.")
    except ValueError :
        print("There has been a problem opening or reading your file.")
    ThirdFile = "PresObamaInauguralAddress.txt"
    print("This is the analysis for President 2009 Obama's inaugural address.")
    try :
        invokeFcn(ThirdFile)
    except OSError :
        print("There has been a problem opening or reading your file.")
    except ValueError :
        print("There has been a problem opening or reading your file.")
    FourthFile = "Trump.txt"
    print("This is the analysis for Trump's 2017 speech to the CIA.")
    try :
        invokeFcn(FourthFile)
    except OSError :
        print("There has been a problem opening or reading your file.")
    except ValueError :
        print("There has been a problem opening or reading your file.")
main()
