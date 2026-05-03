from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory message storage (resets on restart)
messages = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form.get("username")
        content = request.form.get("content")

        if username and content:
            messages.append({
                "username": username,
                "content": content
            })

        return redirect("/")

    return render_template("index.html", messages=messages)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)