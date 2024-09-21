from typing import List
from datetime import datetime
from repository.mysql_repository import MysqlRepository

class SpacesRepository(MysqlRepository):
    def index(self) -> List[object]:
        query = (
                    '''
                    SELECT
                        spaces.id,
                        spaces.room_id,
                        spaces.maximum
                    FROM
                        spaces;
                    '''
                )

        returned_data = self._fetch_by_query(query)
        self._finish()

        return returned_data

    def fetch_space_users(self, space_id) -> List[object]:
        query = (
                    '''
                        SELECT
                            users.icon,
                            users.nickname,
                            users.interested_in,
                            space_users.status,
                            space_users.position
                        FROM
                            spaces
                        LEFT JOIN
                            space_users ON spaces.id = space_users.space_id
                        LEFT JOIN
                            users ON space_users.user_id = users.id
                        WHERE
                            spaces.id = '%s'
                            AND users.id IS NOT NULL;
                    '''
                )
        returned_data = self._fetch_by_query(query % (space_id,))
        self._finish()

        return returned_data
    
    def create_space_users(self, space_id, user_id, position):
        query = "INSERT INTO space_users VALUES ('%s','%s', '%s', '%s');"
        self._commit_query(query % (space_id, user_id, '作業中', position, datetime.now()))
        self._finish()
    
    def update_space_users_status(self, space_id, user_id, status):
        query = "UPDATE space_users SET status = '%s' WHERE space_id='%s' AND user_id='%s';"
        self._commit_query(query % (space_id, user_id, status))
        self._finish()
    
    def delete_space_users(self, space_id, user_id):
        query = "DELETE FROM space_users WHERE space_id='%s' AND user_id='%s';"
        self._commit_query(query % (space_id, user_id))
        self._finish()
