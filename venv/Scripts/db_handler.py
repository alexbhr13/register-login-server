from mysql import connector

DEFAULT_USER = 'root'
DEFAULT_PASSWORD = 'alexbhrsebianc'

_db_connection = None
_user = DEFAULT_USER


def get_connection(user, password):
    global _db_connection
    global _user
    if _db_connection is not None and _user == user and _db_connection.is_connected():
        return _db_connection
    _user = user
    connection = connector.connect(
        host='localhost',
        port=3306,
        user=user,
        passwd=password,
        database='account_db'
    )
    _db_connection = connection
    return _db_connection


_db_connection = get_connection(DEFAULT_USER, DEFAULT_PASSWORD)
# print(db_connection)
