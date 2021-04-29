import sgqlc.types


retrieved_schema = sgqlc.types.Schema()



########################################################################
# Scalars and Enumerations
########################################################################
Boolean = sgqlc.types.Boolean

String = sgqlc.types.String


########################################################################
# Input Objects
########################################################################

########################################################################
# Output Objects and Interfaces
########################################################################
class Book(sgqlc.types.Type):
    __schema__ = retrieved_schema
    __field_names__ = ('author', 'title')
    author = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='author')
    title = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='title')


class Mutation(sgqlc.types.Type):
    __schema__ = retrieved_schema
    __field_names__ = ('add_book',)
    add_book = sgqlc.types.Field(sgqlc.types.non_null('Result'), graphql_name='addBook', args=sgqlc.types.ArgDict((
        ('title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='title', default=None)),
        ('author', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='author', default=None)),
))
    )


class Query(sgqlc.types.Type):
    __schema__ = retrieved_schema
    __field_names__ = ('books', 'get_book_by_title')
    books = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(Book))), graphql_name='books')
    get_book_by_title = sgqlc.types.Field(sgqlc.types.non_null(Book), graphql_name='getBookByTitle', args=sgqlc.types.ArgDict((
        ('book_title', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='bookTitle', default='Bible')),
))
    )


class Result(sgqlc.types.Type):
    __schema__ = retrieved_schema
    __field_names__ = ('success', 'message')
    success = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='success')
    message = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='message')



########################################################################
# Unions
########################################################################

########################################################################
# Schema Entry Points
########################################################################
retrieved_schema.query_type = Query
retrieved_schema.mutation_type = Mutation
retrieved_schema.subscription_type = None

