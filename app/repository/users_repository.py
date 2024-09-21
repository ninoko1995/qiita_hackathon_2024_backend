from datetime import datetime
from repository.mysql_repository import MysqlRepository

class UsersRepository(MysqlRepository):
    def create(self, data) -> str:
        query = (
                    '''
                        INSERT INTO
                            users
                            (email, password, created_at)
                        VALUES
                            ('%s', '%s');
                    '''
                )
        self._commit_query(query % (data['email'], data['password'], datetime.now()))
        self._finish()
        

    def update(self, user_id, data):
        query = (
                    '''
                        UPDATE
                            users
                        SET
                            email = '%s',
                            password = '%s',
                            nickname = '%s',
                            interested_in = '%s',
                            twitter_screenname = '%s',
                            icon = '%s'
                        WHERE user_id = '%s';
                    '''
        )
        self._commit_query(query % (data['email'], data['password'], data['nickname'], data['interested_in'], data['twitter_screenname'], data['icon'], user_id))
        self._finish()


    def show(self, user_id) -> object:
        query = (
                    '''
                        SELECT
                            id,
                            email,
                            nickname,
                            interested_in,
                            twitter_screenname,
                            icon
                        FROM
                            users
                        WHERE
                            id = '%s';
                    '''
                )

        returned_data = self._fetch_by_query(query % (user_id,))
        self._finish()

        return returned_data