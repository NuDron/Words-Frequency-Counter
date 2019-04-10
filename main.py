"""
Finding common English words is this program main purpose.
This script will iterate through the user-supplied document (in .txt format only)
and will show 50 most common words sorted by decreasing frequency.

Program's Graphical User Interface (GUI) is made in the Tkinter library
as it is sufficiently robust and widely supported in Python.

Even though this script is heavily modified (GUI, different sorting algorithm,
new validation method) this work is based on the project from Open University (see [CREDITS] section).

Credits:
This code was initially my Open University Project and I had to do most of this myself,
but I need to mention that the whole idea of this app is thanks to Open University team
behind M269-18J module (Algorithms, data structures and computability),
which I wholeheartedly recommend to study.

Made By: Krzysztof Szumko (09 - April - 2019)
LinkedIn: https://www.linkedin.com/in/krzysztofszumko1989
"""
from tkinter import *
from tkinter import filedialog

"""
Class is used later as a main tool for storage of words and later sorting words.
"""
class Bag:

    def __init__(self):
        """Create a new empty bag."""
        self.items = []

    def add(self, item):
        """Add one copy of item to the bag. Multiple copies are allowed."""
        self.items.append(item)

    def count(self, item):
        """Return the number of copies of item in the bag.

        Return zero if the item doesn't occur in the bag.
        """
        counter = 0
        for an_item in self.items:
            if an_item == item:
                counter += 1
        return counter

    def clear(self, item):
        """Remove all copies of item from the bag.

        Do nothing if the item doesn't occur in the bag.
        """
        newList = []
        for eachElement in self.items:
            if eachElement != item:
                newList.append(eachElement)

        self.items = newList

    def size(self):
        """Return the total number of copies of all items in the bag."""
        return len(self.items)

    def ordered(self):
        """Return the items by decreasing number of copies.

        Return a list of (count, item) pairs.
        """
        result = set()
        for item in self.items:
            result.add((self.count(item), item))
        return sorted(result, reverse=True)
"""
Method adds words from text file where they are separated by ',' sign (this is used as list separator).
@return: a List of words to avoid from text file titled 'wordsToAvoid.txt' (in main folder)
! Script won't run without 'wordsToAvoid.txt'.
"""
def listOfValidWords():
    text_file = open('wordsToAvoid.txt', encoding="utf8", errors ='ignore')                                             #ToDo improve encoding - errors spotted
    lines = text_file.read().split(',')
    text_file.close()
    return lines

#Initialisation of list of valid words as same list will be used multiple times.
listOfValidWords = listOfValidWords()

"""
The main method for validating if a word should be labelled as occurring. 
This method makes sure that word which is printed later is "proper".
Method uses listOfValidWords().
"""
def valid(word):
    """Return True if word should be added to the bag, otherwise False.
    @return: Single word as String
    """
    if word not in listOfValidWords and word != '' and word not in range(100):
        return word


def bag_of_words(filename):
    """Return the words occurring in filename as a bag-of-words.
    filename is a string with the name of a text file
    """
    words = Bag()
    # open the file in read-only mode
    with open(filename, mode="r", encoding="utf8") as file:
        # go through the file line by line
        for line in file:
            # transform punctuation into space
            line = line.replace('(', ' ')
            line = line.replace('[', ' ')
            line = line.replace('{', ' ')
            line = line.replace(')', ' ')
            line = line.replace(']', ' ')
            line = line.replace('}', ' ')
            line = line.replace('.', ' ')
            line = line.replace(',', ' ')
            line = line.replace(';', ' ')
            line = line.replace(':', ' ')
            line = line.replace('_', ' ')
            line = line.replace('—', ' ')
            line = line.replace('1', ' ')
            line = line.replace('2', ' ')
            line = line.replace('3', ' ')
            line = line.replace('4', ' ')
            line = line.replace('5', ' ')
            line = line.replace('6', ' ')
            line = line.replace('7', ' ')
            line = line.replace('8', ' ')
            line = line.replace('9', ' ')
            line = line.replace('0', ' ')
            line = line.replace('-tm', ' ')
            # use space to separate the words in a line
            for word in line.split():
                # remove quote marks and other characters
                word = word.strip("'\"!?+-*/#")
                # put in lowercase
                word = word.lower()
                if valid(word):
                    words.add(word)
    return words

"""
The main function for counting words from a text user-supplied file and 
printing top 50 words sorted in decreasing order by frequency.
"""
def getWordCounted():
    #Start from cleaning the text Window (GUI) from previous activities
    textWindow.delete(1.0, END)
    textWindow.insert(INSERT, "Collecting words in selected text file...")

    #Pop-up window for choosing suitable file
    all_words = bag_of_words(filedialog.askopenfilename())
    textWindow.insert(INSERT, "Done" + '\n')

    textWindow.insert(INSERT, 'Sorting the words by decreasing frequency...')
    frequency = all_words.ordered()
    textWindow.insert(INSERT,"Done" + '\n')

    top = 50                                                                                                            #ToDo make variable changable by user
    textWindow.insert(INSERT, "The " + str(top) + " most frequent words are:")

    #Variable initialised for numeration
    counter = 1
    for (count, word) in frequency[:top]:
        textWindow.insert(INSERT, '\n' + str(counter) + ') the word occured ' + str(count) + ' times: ' + word)
        counter = counter + 1


def instructionsCreator():
    """
    Method is responsible for creating a text of instruction for How-To-Use the app.
    Text is displayed in Top Frame.
    :return:
    """
    instruction = ""
    instruction += "-- >  How to use an app  < --" + '\n'
    instruction += "1) Click on the [SELECT TEXT FILE] button below" + '\n'
    instruction += "2) Choose a suitable file in '.txt' format" + '\n'
    instruction += "3) Wait, it could take a while to process everything" + '\n'
    instruction += "" + '\n'
    instruction += "IMPORTANT *** File Should be in English" + '\n'
    instruction += "IMPORTANT *** Words will be lower-cased" + '\n'
    return instruction


"""
TkInter Graphical User Interface
"""
#Main tkinter window
root = Tk()
#tkinter method for assigning a custom title to window.
root.title("Frequency Word Counter")
#Main window 'Root' size is defined. Can be resized by user.
root.geometry('500x500')

#Creation of Frames inside Tkinter Root object, which will be populated with buttons.
topFrame = Frame(root)
middleFrame = Frame(root)
bottomFrame = Frame(root)

#Populating the Frames to root window. From now on it is visible.
topFrame.pack( side = TOP , anchor = N , expand = YES )
middleFrame.pack( fill = BOTH )
bottomFrame.pack( side = BOTTOM )

#Label with instruction text. Position is Top-Left.
a = Label(topFrame, text= instructionsCreator()).pack( side = LEFT)

"""
Button creation with 'command'(method) attached to it. 
! Remember not to use '()' with your method as it will call it immediately on runtime.
"""

ab = Button(middleFrame, text="Select Text File", command = getWordCounted)
ab.pack( fill = BOTH )

"""
Creation of text window for feedback and output. 
It is made scalable to Frame size populated by it (bottomFrame).
"""
textWindow = Text(bottomFrame)
textWindow.pack( fill = BOTH )


#This makes root window await for input.
#Always refreshed loop awaiting for input.
root.mainloop()
