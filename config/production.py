from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'7\xd2\xa4\xf4\x0f\xd2\xcc\x0bT\xce\xe7\xfd;\\3h'
