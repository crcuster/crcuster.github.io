from flask import Flask, render_template_string, request

app = Flask(__name__)

vote_count = 0

@app.route('/')
def index():
    return render_template_string(open('index.html').read())

@app.route('/get_votes')
def get_votes():
    global vote_count
    return str(vote_count)

@app.route('/vote', methods=['POST'])
def vote():
    global vote_count
    vote_count += 1
    return str(vote_count)

if __name__ == '__main__':
    app.run(debug=True)
