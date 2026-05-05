# Manages a media database of Movies, Books, and TV Shows,loads data from data.txt file, allows listing,
# searching, deleting, and adding items, rewrites the file after changes, and displays statistics
# such as total items, average release year, and oldest/newest entries.

class Media:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def __str__(self):
        return self.title + "(" + str(self.year) + ")"

    def getAttributeString(self):
        return self.title + str(self.year)

class Movie(Media):
    def __init__(self, title, year, genre):
        super().__init__(title, year)
        self.genre = genre

    def __str__(self):
        return super().__str__() + "\nGenre: " + self.genre

    def getAttributeString(self):
        return self.title + str(self.year) + self.genre

class Book(Media):
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def __str__(self):
        return super().__str__() + "\nAuthor: " + self.author

    def getAttributeString(self):
        return self.title + str(self.year) + self.author

class TVShow(Media):
    def __init__(self, title, year, numSeasons):
        super().__init__(title, year)
        self.numSeasons = numSeasons

    def __str__(self):
        return super().__str__() + "\nSeasons: " + str(self.numSeasons)

    def getAttributeString(self):
        return self.title + str(self.year) + str(self.numSeasons)

def getData():
    '''
    #Writing to the file
    outFile = open("data.txt", "a")
    outFile.write("movie,Django Unchained,2011,Western Action\n")
    outFile.close()
    '''
    
    #Connect to the file
    inFile = open("data.txt", "r")
    #Read the data into a variable
    theData = inFile.readlines()
    #Close the file
    inFile.close()
    
    for pos in range(len(theData)):     #get numbers 0 -> len(list) - 1
        theData[pos] = theData[pos].replace("\n", "") #strip newline from theData[pos]
    #print('The List: ', theData)

    movies = []
    shows = []
    books = []

    DELIMITER = ","
    #for each line 
    for line in theData:
        #seperate each attribute
        curLine = line.split(DELIMITER)
        for x in range(len(curLine)):
            curLine[x] = curLine[x].replace("@", ",")
        #if pos 0 is "movie", 
        if curLine[0] == "movie":
            #create a movie object with attributes
            m = Movie(curLine[1], int(curLine[2]), curLine[3])
            #add movie object to movies list
            movies.append(m)     
        elif curLine[0] == "book":
            b = Book(curLine[1], int(curLine[2]), curLine[3])
            books.append(b)
        elif curLine[0] == "tv":
            t = TVShow(curLine[1], int(curLine[2]), int(curLine[3]))
            shows.append(t)
    db = [movies, books, shows]
    return db

#allows user to delete item, lists the items then takes input selection
def deleteItem(curList, mediaDB):
    print("\n== DELETE ITEM ==")

    for titleItem in range(len(curList)):#list of items with a num in front for user to pick
        print(str(titleItem+1) + ") " +curList[titleItem].title)

    choice = input("Enter number to delete: ")#user chooses
    while not choice.isdigit() or int(choice) < 1 or int(choice) > len(curList):
        choice = input("Enter valid number: ")#validating the choice is num &  in list 

    index = int(choice) - 1
    removed = curList.pop(index)
    print("Deleted: " + removed.title)#rewrite data to not have that item no more

    rewriteFile(mediaDB)

#allows uuser toadd item, based on what type wanted
def addItem(curList, mediaType, mediaDB):
    print("\n== ADD ITEM ==")

    title = input("Title: ")
    title = title.replace(",", "@")#converts @ and ,
    year = int(input("Year: "))

    if mediaType == "movie":#if movie type make the object genre
        genre = input("Genre: ")
        newItem = Movie(title, year, genre)
        mediaDB[0].append(newItem)

    elif mediaType == "book":#if book type make author object
        author = input("Author: ")
        newItem = Book(title, year, author)
        mediaDB[1].append(newItem)

    elif mediaType == "tv":#if tv type make seasons num obect
        seasons = int(input("Number of seasons: "))
        newItem = TVShow(title, year, seasons)
        mediaDB[2].append(newItem)

    print("Item added!")
    rewriteFile(mediaDB)
    

def rewriteFile(mediaDB):

    out = open("data.txt", "w")

    #for movies adds whatever option add/delete to the new version of data file rewrtiten
    for m in mediaDB[0]:
        convertMovieTitle = m.title.replace(",", "@")
        out.write("movie," + convertMovieTitle + "," + str(m.year) + "," + m.genre + "\n")

    for b in mediaDB[1]:
        convertBookTitle = b.title.replace(",", "@")
        out.write("book," + convertBookTitle + "," + str(b.year) + "," + b.author + "\n")

    for t in mediaDB[2]:
        convertTVTitle = t.title.replace(",", "@")
        out.write("tv," + convertTVTitle + "," + str(t.year) + "," + str(t.numSeasons) + "\n")

    out.close()

#lists total DB item num and average year released and old/newest item sorted yearly
def displayStats(curList):
    print("\n== STATS ==")

    if len(curList) == 0:
        print("No items.")
        return

    total = len(curList)
    sumYears = 0
    for item in curList:
        sumYears += item.year

    avgYear = sumYears / total

    oldest = curList[0]
    newest = curList[0]

    for item in curList:
        if item.year < oldest.year:
            oldest = item
        if item.year > newest.year:
            newest = item

    print("Total items: " + str(total))
    print("Average year: " + str(round(avgYear, 2)))
    print("Oldest item: " + str(oldest))
    print("Newest item: " + str(newest))




def main():
    MOVIES = 0
    BOOKS = 1
    TV = 2
    
    mediaDB = getData()
    logo = '''
___  ___         _ _      ___  ___                                  
|  \/  |        | (_)     |  \/  |                                  
| .  . | ___  __| |_  __ _| .  . | __ _ _ __   __ _  __ _  ___ _ __ 
| |\/| |/ _ \/ _` | |/ _` | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '__|
| |  | |  __/ (_| | | (_| | |  | | (_| | | | | (_| | (_| |  __/ |   
\_|  |_/\___|\__,_|_|\__,_\_|  |_/\__,_|_| |_|\__,_|\__, |\___|_|   
                                                     __/ |          
                                                    |___/           '''
    print("Welcome to...", end = "")
    print(logo)
    userMenu = '''
== SELECT MEDIA TYPE ==
A) Movies
B) Books
C) TV Shows'''
    actionMenu = '''
== SELECT ACTION ==
A) List all
B) Search
C) Delete items
D) Add items
E) Display Stats
'''
    statsMenu = '''
== DISPLAY STATS ==
'''
    #Choose Media Type
    print(userMenu)
    curList = [] #holds current media list
    choice = input(">>").lower()
    while choice not in ["a","b","c"]:
        choice = input(">>").lower()
    if choice == "a":
        curList = mediaDB[MOVIES]
    elif choice == "b":
        curList = mediaDB[BOOKS]
    elif choice == "c":
        curList = mediaDB[TV]
    else:
        print("How did we get here?", choice)

    #Choose action
    print(actionMenu)
    choice = input(">>").lower()
    while choice not in ["a","b","c","d","e"]:
        choice = input(">>").lower()

    if choice == "a":
        for item in curList:
            print(item)
            print()

    elif choice == "b":
        term = input("Enter search term: ").lower()
        print("FOUND:")
        for item in curList:
            if term in item.getAttributeString().lower():
                print(item)
                print()

    elif choice == "c":#deletes item
        deleteItem(curList, mediaDB)

    elif choice == "d":
        if curList == mediaDB[0]:
            addItem(curList, "movie", mediaDB)
        elif curList == mediaDB[1]:
            addItem(curList, "book", mediaDB)
        elif curList == mediaDB[2]:
            addItem(curList, "tv", mediaDB)

    elif choice == "e":#displays stats
        print(statsMenu)
        displayStats(curList)

        

main()
