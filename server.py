from waitress import serve
from stock-club-api/api import app
#serve(app, listen='0.0.0.0:5000', url_scheme='https')
serve(app, unix_socket='/tmp/nginx.socket', url_scheme='https')