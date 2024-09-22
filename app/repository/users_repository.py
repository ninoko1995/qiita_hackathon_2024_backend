import hashlib
import os
from datetime import datetime
from repository.mysql_repository import MysqlRepository

class UsersRepository(MysqlRepository):
    # パスワードをハッシュ化する関数
    def hash_password(self, plain_password):
        # ソルトを生成
        salt = os.urandom(16)  # ランダムな16バイトのソルトを生成
        # ソルトとパスワードを組み合わせてハッシュ化
        hashed_password = hashlib.sha256(salt + plain_password.encode('utf-8')).hexdigest()
        return hashed_password, salt

    def verify_password(self, plain_password, stored_hashed_password, stored_salt):
        # 入力されたパスワードと保存されたソルトを組み合わせてハッシュ化
        hashed_password = hashlib.sha256(bytes.fromhex(stored_salt) + plain_password.encode('utf-8')).hexdigest()
        return hashed_password == stored_hashed_password


    def check_login(self, email, plain_password) -> object:
        query = (
                    '''
                        SELECT
                            password,
                            salt
                        FROM
                            users
                        WHERE
                            email = '%s';
                    '''
                )

        returned_data = self._fetch_by_query(query % (email,))
        self._finish()

        if not returned_data:
            return False 

        return self.verify_password(plain_password, returned_data[0]['password'], returned_data[0]['salt'])

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
        hashed_password, salt = self.hash_password(data['password'])

        query = (
                    '''
                        INSERT INTO
                            users
                            (email, password, salt, nickname, interested_in, twitter_screenname, icon, created_at)
                        VALUES
                            ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');
                    '''
                )
        self._commit_query(query % (
            data['email'], 
            hashed_password,
            salt.hex(), 
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
            hashed_password, salt = self.hash_password(data['password'])
            query += ', password = "%s", salt = "%s"' % (hashed_password, salt.hex())
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