class Publication: # defines a class called Publication
    def __init__(self, title, author): # initializes the Publication class with title and author parameters
        self.title = title 
        self.author = author 

    def get_title(self): # defines a method to get the title of the publication
        return self.title 

    def get_author(self): # defines a method to get the author of the publication
        return self.author 

    def set_title(self, title): # defines a method to set the title of the publication
        self.title = title 

    def set_author(self, author): # defines a method to set the author of the publication
        self.author = author 

    def display_info(self): # defines a method to display the information of the publication
        print(f"Title: {self.title} \nAuthor: {self.author}") # prints the title and author of the publication

class Book(Publication): # defines a subclass of Publication called Book
    def __init__(self, title, author, number_of_pages): # initializes the Book class with title, author, and number_of_pages parameters
        super().__init__(title, author) # gives access to the parent class's methods and attributes
        self.number_of_pages = number_of_pages 

    def get_number_of_pages(self): # defines a method to get the number of pages in the book
        return f"Number of Pages: {self.number_of_pages}" 

    def set_number_of_pages(self, number_of_pages): # defines a method to set the number of pages in the book
        if number_of_pages > 1: # checks if the number of pages is greater than 1
            self.number_of_pages = number_of_pages 
            return self.number_of_pages 
        else:
            print("The number of pages must be positive. ") # displays an error message
            return None 
        
class Magazine(Publication): # defines a subclass of Publication called Magazine
    def __init__(self, title, author, issue_number): # initialize the Magazine class with title, author, and issue_number parameters
        super().__init__(title, author) # gives access to the parent class's methods and attributes
        self.issue_number = issue_number 

    def get_issue_number(self): # defines a method to get the issue number of the magazine
        return f"Issue Number: {self.issue_number}" 

    def set_issue_number(self, issue_number): # defines a method to set the issue number of the magazine
        if issue_number > 0: # checks if the issue number is greater than 0
            self.issue_number = issue_number 
            return self.issue_number 
        else:
            print("The issue number must be positive. ") # displays an error message
            return None

publication = Publication("The Maze Runner", "James Dashner") # sets the title and author of the publication
book = Book("The Maze Runner", "James Dashner", 375) # adds the number of pages of the book
magazine = Magazine("National Geographic", "Various Authors", 202) # sets the title, author, and issue number of the magazine

print("Publication Info:") # prints the publication info
publication.display_info() # displays the publication info

print("\nBook Info:") # prints the book info
book.set_number_of_pages(-100)  # This sets the number of pages to an invalid value
book.display_info() # displays the book info
print(book.get_number_of_pages()) # prints the number of pages of the book

print("\nMagazine Info:") # prints the magazine info
magazine.display_info() # displays the magazine info
print(magazine.get_issue_number()) # prints the issue number of the magazine
