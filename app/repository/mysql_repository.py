import mysql.connector as mydb
from typing import Optional
import config

class MysqlRepository:
    def __init__(self):
        self.client = mydb.connect(
            host=config.HOST,
            user=config.USER,
            password=config.PASSWORD,
            database=config.DATABASE,
            charset='utf8mb4'
        )
        self.cur = self.client.cursor(dictionary=True)


    def _finish(self):
        self.cur.close()
        self.client.close()

    # get系    
    def _fetch_by_query(self, query: str) -> Optional[object]:
        self.cur.execute(query)    
        all_data = self.cur.fetchall()
        return all_data
    
    # post系
    def _commit_query(self, query: str):
        self.cur.execute(query)
        self.client.commit()

    # migration fileを実行する
    def _execute_migration(self, query: str):
        self.cur.execute(query, multi=True)
        self.client.commit()
