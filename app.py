from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    try:
      text = request.form.get("initial")
      rtext = request.form.get("replace")
      ntext = request.form.get("newtext")

      final = text.replace(rtext,ntext)
    except:
      text = ''
      rtext = ''
      ntext = ''
      final = ''

    return render_template('home.html', intial_text=text, replace_text=rtext, new_text=ntext, final_text=final)

app.run()
 