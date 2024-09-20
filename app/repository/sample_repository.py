from typing import List
from datetime import datetime
from repository.mysql_repository import MysqlRepository

class SampleRepository(MysqlRepository):
    def fetch(self) -> List[object]:
        query = (
                    'SELECT '
	                    'id,'
                        'content,'
                        'created_at,'
                        'updated_at '
                    'FROM '
                        'sample_table;'
                )

        returned_data = self._fetch_by_query(query)
        self._finish()

        return returned_data
    
    def create(self, data):
        query = "INSERT INTO sample VALUES ('%s','%s')"
        self._commit_query(query % (data["id"], data["content"],))
        self._finish()
