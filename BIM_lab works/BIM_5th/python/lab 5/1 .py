class Book:
    def __init__(self,title,author,genre):
        self.title=title
        self.author=author
        self.genre=genre
    def display(self):
        print("Title: ",self.title)
        print("Author: ",self.author)
        print("Genre: ",self.genre)
b=Book('Python','John Doe','Education')
b.display()
        