import sqlite3


class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.connection.execute('''
                                    CREATE TABLE IF NOT EXISTS dados (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT NOT NULL,
                                    record FLOAT NOT NULL,
                                    date TEXT NOT NULL)
                                ''')
    def save(self, record_dict: dict):
        self.connection.execute('INSERT INTO dados(name, record, date) VALUES(:name, :record, :date)', record_dict)
        self.connection.commit()

    def retrieve_top10(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY record DESC LIMIT 10').fetchall()

    def close(self):
        return self.connection.close()