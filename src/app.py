from flask import Flask, redirect, render_template, request, session
#for cookies setting

name="app"
# Configure application
app = Flask(name)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=['GET'])
def index():
  return render_template("firstPage.html")

@app.route("/tomain")
def to_main_page():
    return render_template("main.html")


@app.route("/uploaded", methods=["POST"])
def upload_file():
    uploaded_image= request.files['image']
    if uploaded_image.filename != '':
        uploaded_image.save("input/" + uploaded_image.filename)

    uploaded_video = request.files['video']
    if uploaded_video.filename != '':
        uploaded_video.save("input/" + uploaded_video.filename)
    return render_template("output.html",url="static/output/" + uploaded_video.filename)
