import datetime
import os
# os.getcwd()

class LMS:
    """ This class is used to keep record of books library.
    It has total four modules: "Display Books", "Issue Books", "Return Books", "Add Books" """
    def __init__(self,list_of_books, library_name):
        self.list_of_books = "List_Of_Books.txt"
        self.library_name = library_name
        self.books = {}
        Id = 101
        with open(self.list_of_books) as bk:
            content = bk.readlines()
        for line in content:
            self.books.update({str(Id):{"books_title":line.replace("\n",""),
            "lender_name": "","Issue_date":"","Status":"Available"}})
            Id =Id + 1
    def display_books(self):
        print("------------------------List Of Books--------------------------")
        print("Books ID", "\t","Title")
        print("---------------------------------------------------------------")
        for key, value in self.books.items():
            print(key,"\t\t",value.get("books_title"), "- [",value.get("Status"),"]")

    def Issue_books(self):
        books_id = input("Enter books ID: ")
        current_date = datetime.datetime.now().strftime("%Y-%m_%d %H:%M:%S")
        if books_id in self.books.keys():
            if not self.books[books_id]["Status"] == "Available":
                print(f"This book is already issued to {self.books[books_id]['lender_name']}\
                    on {self.books[books_id]['Issue_date']}")
                return self.Issue_books()
            elif self.books[books_id]['Status'] == "Available":
                your_name = input("Enter your name: ")
                self.books[books_id]['lender_name'] = your_name
                self.books[books_id]['Issue_date'] = current_date
                self.books[books_id]['Status'] = "Already Issued"
                print("Books Issued Successfully !!! \n")
        else:
            print("Book ID not found !!!")
            return self.Issue.books()

    def add_books(self):
        new_books = input("Enter books title: ")
        if new_books == "":
            return self.add_books()
        elif len(new_books)>25:
            print("Books title length is too long!!! Title length should be 20 chars")
            return self.add_books()
        else:
            with open(self.list_of_books,"a") as bk:
                bk.writelines(f"{new_books}\n")
                self.books.update({str(int(max(self.books))+1):{'books_title':new_books,'lender_name':"",
                'Issue_date':"",'Status':"Available"}})
                print(f"This books '{new_books}' has been added successfully !!!")

    def return_books(self):
        books_id = input("Enter books ID: ")
        if books_id in self.books.keys():
            if self.books_dict[books_id]["Status"] == "Available":
                print("This books is already available in library. Please check your book ID.")
                return self.return_books()
            elif not self.books[books_id]["Status"]=="Available":
                self.books[books_id]["lender_name"] = ""
                self.books[books_id]["Issue_date"] = ""
                self.books[book_id]["Status"] = "Available"
                print("Successfully updated !!! \n")
        else:
            print("Book ID is not found")


try:
    myLMS = LMS("List_Of_Books.txt","Python's Library")
    press_key_list = {"D": "Display Books","I": "Issue Books","A": "Add Books","R": "Return Books","Q":"Quit"}
    key_press = False
    while not(key_press == "q"):
        print(f"\n---------------Welcome To {myLMS.library_name} Library management System---------------- \n")
        for key,value in press_key_list.items():
            print("Press",key,"To",value)
        key_press = input("Press Key: ").lower()
        if key_press == "i":
            print("\nCurrent Selection : Issue Books\n")
            myLMS.Issue_books()
        elif key_press == "a":
            print("\nCurrent Selection : Add Books\n")
            myLMS.add_Books()
        elif key_press == "d":
            print("\nCurrent Selection : Display Books\n")
            myLMS.display_books()
        elif key_press == "r":
            print("\nCurrent Selection : Return Books\n")
            myLMS.return_books()
        elif key_press == "q":
            break
        else:
            continue
except Exception as e:
    print("Something went wrong. Please check your input !!!")





