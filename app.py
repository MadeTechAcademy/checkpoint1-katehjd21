from flask import Flask, render_template
from themes_data import duties_list, themes_dict

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("duties.html", duties=None, theme=None, themes=themes_dict)

@app.route("/all")
def view_all_duties():
    return render_template("duties.html", duties=duties_list, theme="All Duties", themes=themes_dict)

@app.route("/theme/<theme_key>")
def show_theme(theme_key):
    theme = themes_dict.get(theme_key)
    if not theme:
        return "Theme not found", 404
    duties = theme.get_associated_duties(duties_list)
    return render_template("duties.html", duties=duties, theme=theme.name, themes=themes_dict)

if __name__ == "__main__":
    app.run(debug=True)



