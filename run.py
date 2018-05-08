from app import create_app
from logger import c_logger as log

if __name__ == '__main__':
    web_app = create_app()
    web_app.run(debug=True, port=8003)
    log.info('Web_app is running on ' + web_app.endpoint)
