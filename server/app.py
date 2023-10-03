#!/usr/bin/env python3


from config import app, db
from config.models import Heroes, Powers, Heroes_Powers

if __name__ == "__main__":
    app.run(debug=True, port=5555)