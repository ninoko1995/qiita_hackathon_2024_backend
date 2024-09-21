from datetime import datetime
from repository.mysql_repository import MysqlRepository

class UsersRepository(MysqlRepository):
    def check_login(self, email, password) -> object:
        query = (
                    '''
                        SELECT
                            password
                        FROM
                            users
                        WHERE
                            email = '%s';
                    '''
                )

        returned_data = self._fetch_by_query(query % (email,))
        self._finish()

        return returned_data[0]['password'] == password

    def fetch_user_id_by_email(self, email) -> object:
        query = (
                    '''
                        SELECT
                            id
                        FROM
                            users
                        WHERE
                            email = '%s';
                    '''
                )

        returned_data = self._fetch_by_query(query % (email,))
        self._finish()

        return returned_data[0]['id']

    def create(self, data) -> str:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        query = (
                    '''
                        INSERT INTO
                            users
                            (email, password, nickname, interested_in, twitter_screenname, icon, created_at)
                        VALUES
                            ('%s', '%s', '%s', '%s', '%s', '%s', '%s');
                    '''
                )
        self._commit_query(query % (
            data['email'], 
            data['password'], 
            data.get('nickname', ''), 
            data.get('interested_in', ''), 
            data.get('twitter_screenname', ''), 
            data.get('icon', ''), 
            now
        ))
        created_user_id = self._fetch_by_query('SELECT id FROM users WHERE email = "%s";' % (data['email'],))
        self._finish()

        return created_user_id[0]['id']

    def update(self, user_id, data):
        query = (
                    '''
                        UPDATE
                            users
                        SET
                            email = '%s',
                            nickname = '%s',
                            interested_in = '%s',
                            twitter_screenname = '%s',
                            icon = '%s'
                    '''
        )

        if data.get('password', '') != '':
            query += ', password = "%s"' % (data['password'],)
        query += ' WHERE id = "%s";'

        self._commit_query(query % (
            data['email'],
            data.get('nickname', ''), 
            data.get('interested_in', ''), 
            data.get('twitter_screenname', ''), 
            data.get('icon', ''), 
            user_id
        ))
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

        return returned_data[0]