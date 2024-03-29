from settings import *

DEBUG = False

ALLOWED_HOSTS = ['ec2-13-126-5-76.ap-south-1.compute.amazonaws.com', '13.126.5.76']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'inception',
        'USER': 'inception',
        'PASSWORD': '!nc3pt!0n',
        'HOST': 'inception.cu6bw1tu5ilm.ap-south-1.rds.amazonaws.com',
        'PORT': '5432',
    }
}
