from flask import Flask, redirect, render_template, request, session


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

@app.route("/main_page")
def to_main_page():
    return render_template("main.html")


@app.route("/uploaded_page", methods=["POST"])
def upload_file():

    uploaded_image= request.files['image']

    if uploaded_image.filename != '':
        src_img=uploaded_image
        src_img.save("input/" + srcimg.filename)

    elif 'choose_img1' in request.form:
        #didnt upload and choose from temp
        src_img=img1
        src_img.save("input/" + "img1.png")

    elif 'choose_img2' in request.form:
        #didnt upload and choose from temp
        src_img=img2
        src_img.save("input/" + "img2.png")

    elif 'choose_img3' in request.form:
        #didnt upload and choose from temp
        src_img=img3
        src_img.save("input/" + "img3.png")


    uploaded_video = request.files['video']
    if uploaded_video.filename != '':
        driv_vid=uploaded_video
        driv_vid.save("input/" + uploaded_video.filename)

    elif  request.form.get('vid1') == 'choose_vid1':
        #didnt upload and choose from temp
        driv_vid=vid1
        driv_vid.save("input/" + "vid1.png")

    elif  request.form.get('vid2') == 'choose_vid2':
        #didnt upload and choose from temp
        driv_vid=vid2
        driv_vid.save("input/" + "vid2.png")
    elif  request.form.get('vid3') == 'choose_vid3':
        #didnt upload and choose from temp
        driv_vid=vid3
        driv_vid.save("input/" + "vid3.png")



    return render_template("output.html",url="static/output/" + "output.mp4" )
