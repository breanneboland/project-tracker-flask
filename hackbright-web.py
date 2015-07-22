from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)

@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    project_info = hackbright.get_all_student_grades(github)

    # project_dict = {}
    # for project in project_info:
    #     project_dict[project_info[0]] = project_info[1]

    html = render_template("student_info.html",
                            first = first,
                            last = last,
                            github = github,
                            project_info = project_info,
                            # project_name = project_info[0][0],
                            # project_grade = project_info[0][1]
                        )
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

@app.route("/student-added", methods=["POST"])
def made_student():
    first_name = request.form.get("first_name") 
    last_name = request.form.get("last_name")
    github = request.form.get("github")
    hackbright.make_new_student(first_name, last_name, github)
    return render_template("student_added.html", first_name = first_name,
                            last_name = last_name,
                            github = github)

if __name__ == "__main__":
    app.run(debug=True)