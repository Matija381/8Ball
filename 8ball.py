from flask import Flask, render_template, request
import random
# pip install flask
app = Flask(__name__)
@app.route("/", methods = ["GET"])
def index():

    return render_template("index.html")
@app.route("/ball", methods = ["post"])
def ball():
    tmp=dict(request.form)
    vpr=tmp.get("vprašanje")
    odgovori = [
    "Da, zagotovo!",
    "Brez dvoma.",
    "Verjetno.",
    "Ne morem napovedati zdaj.",
    "Možno, ampak ne zelo verjetno.",
    "Ne morem reči, poskusi kasneje.",
    "Ne, nikakor.",
    "Moje vire pravijo, da ne.",
    "Boljše boš izvedel kmalu.",
    "Zdi se, da je odgovor ne.",
    "Samo čas bo pokazal.",
    "Zdaj ni pravi trenutek.",
    "Zagotovo ne.",
    "Brez dvoma, da!",
    "Ostani pozitiven, odgovor bo prišel.",
    "Usoda je neodločena.",
    "Vse kaže, da bo to težko.",
    "Možno, toda lahko se spremeni.",
    "Vse kaže, da je odgovor pritrdilen.",
    "Nikakor, to ne bo šlo.",
]
    if "ljubezen" in vpr:
        return render_template("index.html", rezultat="Kupi raje GPU.")
    if "vikend" in vpr:
        return render_template("index.html", rezultat="TikTok all day.")
    if "denar" in vpr:
        return render_template("index.html", rezultat="Burek only.")
    if "profesor" in vpr:
        return render_template("index.html", rezultat="F speedrun.")
    if vpr[-1]=="!":
        return render_template("index.html", rezultat="Ne kriči.")
    r=random.choice(odgovori)
    return render_template("index.html", rezultat=r)


app.run(debug = True)