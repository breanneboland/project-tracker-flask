from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    html = render_template("student_info.html",
                            first = first,
                            last = last,
                            github = github)
    return html

@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

    # "%s is the GitHub account for %s %s" % (github, first, last)

@app.route("/add-student")
def make_student():
    
    return render_template("student_add.html")

# def make_new_student(first_name, last_name, github):

@app.route("/student-added")
def made_student():
    first_name, last_name, github = request.args.get()
    hackbright.make_new_student(first_name, last_name, github)
    return render_template("student_added.html", first_name = first_name,
                            last_name = last_name,
                            github = github)

if __name__ == "__main__":
    app.run(debug=True)