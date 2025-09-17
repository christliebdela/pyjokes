from flask import Flask, render_template, jsonify
import pyjokes

app = Flask(__name__)

@app.route('/')

def index():
    return render_template("index.html")


@app.route('/get_joke')
def get_joke():
    try:
        joke = pyjokes.get_joke()
        return jsonify({"joke": joke})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)