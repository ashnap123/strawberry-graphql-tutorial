from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation
from retrieved_schema import retrieved_schema as schema

url = 'http://localhost:8000/graphql'
headers = {}
endpoint = HTTPEndpoint(url, headers)

if __name__ == '__main__':
    op = Operation(schema.Query)
    query = op.get_book_by_title(book_title='Bible')

    # Call the endpoint:
    data = endpoint(op)

    # Get native objects
    book = op + data

    pass