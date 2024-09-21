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

    def is_joinable(self, space_id) -> object:
        query = (
                    '''
                        SELECT
                            spaces.maximum as maximum,
                            COUNT(space_users.id) as current_number
                        FROM
                            spaces
                        LEFT JOIN
                            space_users ON spaces.id = space_users.space_id
                        WHERE
                            spaces.id = '%s'
                        GROUP BY
                            spaces.id;
                    '''
                )

        returned_data = self._fetch_by_query(query % (space_id,))
        self._finish()

        return returned_data[0]['maximum'] > returned_data[0]['current_number']

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
    
    def user_by_space_users_uid(self, uid) -> object:
        query = (
                    '''
                        SELECT
                            users.icon as icon,
                            users.nickname as nickname,
                            users.interested_in as interested_in,
                            space_users.status as status,
                            space_users.uid as uid
                        FROM
                            users
                        LEFT JOIN
                            space_users ON users.id = space_users.user_id
                        WHERE
                            space_users.uid = '%s';
                    '''
                )
        returned_data = self._fetch_by_query(query % (uid))
        self._finish()

        return returned_data[0]
    
    def create_space_users(self, space_id, user_id, position):
        query = "INSERT INTO space_users (space_id, user_id, position, status, created_at) VALUES ('%s', '%s', '%s', '%s', '%s');"
        self._commit_query(query % (space_id, user_id, position, '作業中', datetime.now()))
        self._finish()
    
    def update_space_users_uid(self, user_id, room_id, uid):
        query = 'select id from spaces where room_id="%s";'
        space_ids = self._fetch_by_query(query % (room_id,))
        if len(space_ids) == 0:
            raise Exception('room_id not found')

        query = "UPDATE space_users SET uid = '%s' WHERE user_id='%s' AND space_id='%s';"
        self._commit_query(query % (uid, user_id, space_ids[0]['id']))
        self._finish()
    
    def update_space_users_status(self, user_id, status):
        query = "UPDATE space_users SET status = '%s' WHERE user_id='%s';"
        self._commit_query(query % (user_id, status))
        self._finish()
    
    def delete_space_users(self, room_id, user_id):
        query = 'select id from spaces where room_id="%s";'
        space_ids = self._fetch_by_query(query % (room_id,))
        if len(space_ids) == 0:
            raise Exception('room_id not found')
        
        query = "DELETE FROM space_users WHERE user_id='%s' AND space_id='%s';"
        self._commit_query(query % (user_id, space_ids[0]['id']))
        self._finish()
