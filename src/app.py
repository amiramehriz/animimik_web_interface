from flask import Flask, redirect, render_template, request, session
from demo import main
from flask_sqlalchemy import SQLAlchemy

name="app"
# Configure application
app = Flask(name)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# SQL alchemy configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Rating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return str(self.rating)

db.create_all()



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
    imgpath = "static/"
    option = request.form.get('img_options')
    if option == "img1" :
        imgpath = imgpath +"img1.png"
    elif option == "img2":
        imgpath = imgpath +"img2.png"
    elif option == "img3":
        imgpath = imgpath +"img3.png"

    uploaded_image= request.files['image']

    if uploaded_image.filename != '':
        uploaded_image.save("static/input/" + uploaded_image.filename)
        imgpath = "static/input/" +uploaded_image.filename

    vidpath = "static/"
    option = request.form.get('vid_options')
    if option == "vid1" :
        vidpath = vidpath +"1.mp4"
    elif option == "vid2":
        vidpath = vidpath +"3.mp4"
    elif option == "vid3":
        vidpath = vidpath +"4.mp4"

    uploaded_video = request.files['video']
    if uploaded_video.filename != '':
        uploaded_video.save("static/input/" + uploaded_video.filename)
        vidpath = "static/input/" +uploaded_video.filename

    main(config = 'config/vox-256.yaml', driving_video = vidpath,
    source_image = imgpath, checkpoint = '00000061-checkpoint.pth.tar',
    result_video = 'static/output/output.mp4')

    return render_template("output.html",originalURL = vidpath, outputURL="static/output/output.mp4" )



@app.route("/ThankYou", methods=["POST"])
def take_rating():
    rating_score = request.form.get('rate_options')
    if rating_score == "rate1" :
        score=1
    elif rating_score == "rate2":
        score=2
    elif rating_score == "rate3":
        score=3
    elif rating_score == "rate4":
        score=4
    elif rating_score == "rate5":
        score=5

    rating_ = Rating(rating = score)
    db.session.add(rating_)

    db.session.commit()

    current_rating_ = Rating.query.all() # hhhh sorry
    return render_template("thankyou.html", current_rating = current_rating_)
