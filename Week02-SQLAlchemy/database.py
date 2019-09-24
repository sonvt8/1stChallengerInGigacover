import sqlalchemy as db

class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user='postgres', passwd='abc123@@@', host='localhost', port=5432, db='PSQL_INTERN')
    engine = db.create_engine(url)

    def __init__(self):
        self.connection = self.engine.connect()
        print("Hura!!!Successfully connect to database...")

    def fetchByQyery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")

        for data in fetchQuery.fetchall():
            print(data)


