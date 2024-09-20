#!/home/miyablo/.pyenv/versions/3.7.0/bin/python
# -*- coding: utf-8 -*-
import os
import sys
sys.path.append('/home/miyablo/www/kosugiiz')

from glob import glob

from consts import BASE_FOLDER
from repository.mysql_repository import MysqlRepository

if __name__ == '__main__':
    try:
        migaration_folder = BASE_FOLDER + 'migration/'
        migration_paths = list(glob(migaration_folder + '*.sql'))
        for path in migration_paths:
            print("==================== %s ====================" % os.path.basename(path))
            with open(path, 'r', encoding='utf-8') as f:
                query = f.read()
                repository = MysqlRepository()
                returned_data = repository._execute_migration(query)
                repository._finish()
                print(returned_data)
                print("==================== finished ====================")
        print('finish migrations successfully!')
    except Exception as e:
        print('there are some errors')
        print(e)
