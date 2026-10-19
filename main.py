import os

from flask import Flask, render_template

app = create_app()

def main():
    app.run(host="127.0.0.1", port= int(os.environ.get("PORT", 8080)))

if __name__ == "__main__":
    main()
