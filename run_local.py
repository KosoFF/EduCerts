from app import create_app

if __name__ == '__main__':
    web_app = create_app()
    web_app.run(debug=True, port=8003)