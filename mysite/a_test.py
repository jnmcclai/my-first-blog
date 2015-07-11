import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')


print(BASE_DIR)
print(STATIC_URL)
print(STATIC_ROOT)
