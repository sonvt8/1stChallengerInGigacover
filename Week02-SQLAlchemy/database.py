import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
import sys, traceback

class Database():
    # replace the user, password, hostname and database according to your configuration according to your information
    url = 'postgresql://{user}:{passwd}@{host}:{port}/{db}'.format(
        user='postgres', passwd='abc123@@@', host='localhost', port=5432, db='PSQL_INTERN')
    engine = db.create_engine(url)
    session = sessionmaker(bind= engine)()

    def __init__(self):
        try:
            self.connection = self.engine.connect()
            print("Hura!!!Successfully connect to database...")
        except Exception:
            print("Ops!!!You have got fail connection")
            sys.exit(1)

    # Using RAW SQL to querry
    def fetchByQyery(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        for data in fetchQuery.fetchall():
            print(data)
