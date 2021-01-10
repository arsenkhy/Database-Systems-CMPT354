import sqlite3

def queryBook(tableName, attribute, keyword, conn, colID):
    with conn:
        cur = conn.cursor()

        #myQuery = "SELECT * FROM albums NATURAL JOIN artists WHERE Name=:myArtist"
        myQuery = "SELECT * FROM " + tableName + " WHERE  " + attribute + " =:myKeyword"
        #cur.execute(myQuery,{"myArtist":myFavArtist})
        #"myTable":tableName, "myattribute":attribute,
        cur.execute(myQuery,{ "myKeyword":keyword})
        rows=cur.fetchall()
        if rows:
            print("the book ID you should look for is")
        else:
            print("Unfortunately, we do not have any result related " + "!\n")

        for row in rows:
            for i in row:
                print(i , end=' ')
            print("\n")
        print("\n")

def queryBorrow(bookID, conn):
    with conn:
        cur = conn.cursor()
        #bookNumber = int(bookID)
        #myQuery = "SELECT * FROM albums NATURAL JOIN artists WHERE Name=:myArtist"
        myQuery = "SELECT itemID FROM Inventory WHERE bookID =:myKeyword EXCEPT SELECT I.itemID FROM Inventory I, Borrow B WHERE I.itemID = B.itemID AND status = 'NOT RETURNED'"
        #cur.execute(myQuery,{"myArtist":myFavArtist})
        #"myTable":tableName, "myattribute":attribute,
        cur.execute(myQuery,{ "myKeyword":bookID})
        rows=cur.fetchall()
        if rows:
            print("the item ID you should look for is")
            for row in rows:
                for i in row:
                    print(i , end=' ')
                print("\n")
            print("\n")

        else:
            print("Unfortunately, we do not have any result related " + "!\n")

def finish():
    if conn:
        conn.close()
        print("Thank you for coming! Enjoy your day")

# program start here
conn = sqlite3.connect('library.db')
print("Welcome to use Group 44 Library \n")
print("What do you want to do today\n")

print("Looking for a book please type 1 \n")
print("Borrowing book with bookID please type 2 \n")
print("Returning book please type 3 \n")
print("Donating please type 4 \n")
print("Find an event please type 5 \n")
print("Register for an event please type 6 \n")
print("Volunteer for the library please type 7 \n")
print("Ask for help from a librarian please type 8 \n")

action = input("What do you want to do now \n")

if action == "1":
    print("What do you know about the book? Please select \n")
    print("title type 1 \n")
    print("publishYear type 2 \n")
    print("author type 3 \n")
    print("ISBN (exactly) type 4 \n")
    attribute = input("Please select 1 - 4\n")
    if attribute == "1":
        colID = 1
        attribute = "title"
    elif attribute == "2":
        colID = 2
        attribute = "publishYear"
    elif attribute == "3":
        colID = 3
        attribute = "author"
    elif attribute == "4":
        colID = 4
        attribute = "isbn"
    else:
        print("Error input\n")
        finish()
    keyword = input("Please input the exact information you know\n")
    queryBook("Book",attribute, keyword, conn, colID)
elif action == "2":
    print("What book do you want to borrow? Input a bookID \n")
    bookID = input()
    queryBorrow(bookID, conn)
    pass
elif action == "3":
    pass
elif action == "4":
    pass
elif action == "5":
    pass
elif action == "6":
    pass
elif action == "7":
    pass
elif action == "8":
    pass
else:
    print("Error input, please restart")
    finish()



# end of program



#######################
