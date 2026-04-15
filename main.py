from app import app, log
from app.controllers import html, static
from config import HOST, PORT, DEBUG, RELOADER


if __name__ == "__main__":
    app.run(
    	host=HOST,
    	port=PORT,
    	debug=DEBUG,
    	reloader=RELOADER)
