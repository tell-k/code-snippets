
DATABASES = {
    'default': {  # default = master
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tciua',                       # Or path to database file if using sqlite3.
        'USER': 'tciua-user',                  # Not used with sqlite3.
        'PASSWORD': 'tciua-pass',              # Not used with sqlite3.
        'HOST': '/tmp/mysql.sock',             # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',                        # Set to empty string for default. Not used with sqlite3.
    },
    'slave1': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tciua',                       # Or path to database file if using sqlite3.
        'USER': 'tciua-user',                  # Not used with sqlite3.
        'PASSWORD': 'tciua-pass',              # Not used with sqlite3.
        'HOST': '/tmp/mysql2.sock',            # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3307',                        # Set to empty string for default. Not used with sqlite3.
    },
    'slave2': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tciua',                       # Or path to database file if using sqlite3.
        'USER': 'tciua-user',                  # Not used with sqlite3.
        'PASSWORD': 'tciua-pass',              # Not used with sqlite3.
        'HOST': '/tmp/mysql2.sock',            # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3307',                        # Set to empty string for default. Not used with sqlite3.
    }
}
import copy
hoge = copy.copy(DATABASES)
del hoge['default']

print DATABASES.keys()
print hoge.keys()
