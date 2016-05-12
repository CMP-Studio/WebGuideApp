
def secretKey():
    return 'YOUR SECRET KEY'

def databaseConfig():
    db = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'DATABASE',
            'USER': 'USER',
            'PASSWORD': 'PASSWORD',
            'HOST': 'localhost',
            'PORT': '',
        }
    }

    return db
