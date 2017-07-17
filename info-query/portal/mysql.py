import torndb
from config import *


class Operation(object):
    def __init__(self):
        self.db = torndb.Connection(
            options.mysql_host, options.mysql_db, options.mysql_user, options.mysql_password)

    def gets(self, statement):
        data = self.db.get(statement)
        self.db.close()
        return data

    def create(self, statement):
        data = self.db.insert(statement)
        self.db.execute(data)
        self.db.close()
        return True

    def create_many(self, query, parameters):
        data = self.db.insertmany(query, parameters)
        self.db.execute(data)
        self.db.close()
        return True

    def updated(self, statement):
        data = self.db.update(statement)
        self.db.close()
        return True

    def update_many(self, query, parameters):
        data = self.db.updatemany(query, parameters)
        self.db.close()
        return True

    def query(self, statement):
        data = self.db.query(statement)
        self.db.close()
        return data
