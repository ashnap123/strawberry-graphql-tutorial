from typing import List

import strawberry

# Create and activate a venv.
# step 1. pip install requirements.txt
# step 2. strawberry server schema.schema -> this loads up our server, open the webpage
# step 3. Add some documentation to the book type
# step 4. refresh your your web page -> check the documentation is added to the book type
# step 5. Play with our database -> open the database file and run the main. Assure ourselves this is just an on disk dict.
# step 6. Let's create a mutation to add a book to the database.
# step 7. Let's add a query to get all books from the database.
# step 8. Add a book by the title.
from dataclasses_json import dataclass_json
from schema.database import Database

print("Opening database")
db = Database()


@dataclass_json
@strawberry.type(description="")
class Book:
    author: str
    title: str  # This is the title of the book hooray


@dataclass_json
@strawberry.type(description="")
class Result:
    success: bool
    message: str


example_books: List[Book] = [
    Book(
        title='The Great Gatsby',
        author='F. Scott Fitzgerald'),
    Book(
        title='Code',
        author='Programmer'),
    Book(
        title='Bible',
        author='God')]

[db.store_book(item.to_dict()) for item in example_books]


def get_books() -> List[Book]:
    # 1. Lets actually get our books from the database here
    # book_list = []
    # for book in db.get_all_books():
    #     book = Book.from_dict(book)
    #     book_list.append(book)
    #
    # return book_list

    # 2. We shouldn't actually return junk. Get rid of this
    return [Book.from_dict(item) for item in db.get_all_books()]


def get_book_by_title(book_title: str = "Bible") -> Book:
    return Book.from_dict(db.get_book_by_title(book_title))


@strawberry.type(description="This is the root level query description")
class Query:
    books: List[Book] = strawberry.field(resolver=get_books, description="")
    get_book_by_title: Book = strawberry.field(resolver=get_book_by_title)


@strawberry.type
class Mutation:

    @strawberry.field
    def add_book(self, title: str, author: str) -> Result:
        added_book = Book(title=title, author=author)
        # 1. Let's check if our inputs are valid GIGO you put junk in you'll get junk out....
        validation = Book.schema().validate(added_book.to_dict())
        # print(validation)
        if validation != {}:
            return Result(False, 'You give me shit, I fart in your general direction....')

        # 2. Let's actually add a book to the database here
        db.store_book(added_book.to_dict())
        # print("stored a book")

        # 3. Returning a book for adding a book is a little weird lets return a bool or something a bit saner / an id
        return Result(True, 'Go you!')


# This is all you have to do to turn the above into a graphql interface
schema = strawberry.Schema(query=Query, mutation=Mutation)
