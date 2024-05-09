from flask import Flask, render_template, request

app = Flask(__name__)

# Initial state
state = "off"


@app.route('/')
def index():
    return render_template('index.html', state=state)


@app.route('/toggle', methods=['POST'])
def toggle():
    global state
    if state == "off":
        state = "on"
    else:
        state = "off"
    return render_template('index.html', state=state)


if __name__ == '__main__':
    app.run(debug=True)
