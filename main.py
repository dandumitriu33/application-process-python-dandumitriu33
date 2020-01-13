import data_manager
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names_by_first_name('László')

    return render_template('mentor_names.html',
                           mentor_names=mentor_names)


@app.route('/all-mentors')
def all_mentors():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_all_mentors()
    return render_template('all-mentors.html',
                           mentor_names=mentor_names)


@app.route('/all-applicants')
def all_applicants():
    # We get back dictionaries here (for details check 'database_common.py')
    applicant_names = data_manager.get_all_applicants()
    return render_template('all-applicants.html',
                           applicant_names=applicant_names)


@app.route('/nicknames')
def nicknames():
    # We get back dictionaries here (for details check 'database_common.py')
    nicknames = data_manager.get_nicknames()
    return render_template('nicknames.html',
                           nicknames=nicknames)


@app.route('/carol-hat')
def carol_hat():
    # We get back dictionaries here (for details check 'database_common.py')
    applicant_names = data_manager.get_names_and_phone_by_first_name('Carol')
    return render_template('carol-hat.html',
                           applicant_names=applicant_names)


@app.route('/adipisci')
def adipisci():
    # We get back dictionaries here (for details check 'database_common.py')
    applicant_names = data_manager.get_names_and_phone_by_part_email('@adipiscingenimmi.edu')
    return render_template('adipisci.html',
                           applicant_names=applicant_names)


@app.route('/add-markus')
def add_markus():
    message = data_manager.insert_new_applicant('Markus', 'Schaffarzyk', '003620/725-2666', 'djnovus@groovecoverage.com', '54823')
    return render_template('add-markus.html',
                           message=message)


@app.route('/update-jemima')
def update_jemima():
    message = data_manager.update_applicant('Jemima', 'Foreman', '003670/223-7459')
    return render_template('update-jemima.html',
                           message=message)


@app.route('/check-jemima')
def check_jemima():
    # We get back dictionaries here (for details check 'database_common.py')
    applicant_details = data_manager.get_applicant_details_by_first_name_last_name('Jemima', 'Foreman')
    return render_template('check-jemima.html',
                           applicant_details=applicant_details)


@app.route('/delete-mauriseu')
def delete_mauriseu():
    message = data_manager.delete_applicant_by_part_email('@mauriseu.net')
    return render_template('delete-mauriseu.html',
                           message=message)


@app.route('/info')
def info():
    return render_template('info.html')


@app.route('/mentors')
def mentor_and_city():
    mentors = data_manager.get_mentor_and_city()
    return render_template('mentors.html',
                           mentors=mentors)


@app.route('/all-school')
def all_schools():
    schools = data_manager.get_all_schools()
    return render_template('all-schools.html',
                           schools=schools)


@app.route('/mentors-by-country')
def mentors_by_country():
    mentors = data_manager.get_mentors_by_country()
    return render_template('mentors-by-country.html',
                           mentors=mentors)


@app.route('/contacts')
def contacts():
    contacts = data_manager.get_contacts()
    return render_template('contacts.html',
                           contacts=contacts)


@app.route('/applicants')
def applicants():
    applicants = data_manager.get_applicants()
    return render_template('applicants.html',
                           applicants=applicants)


@app.route('/applicants-and-mentors')
def applicants_and_mentors():
    applicants = data_manager.get_applicants_and_mentors()
    return render_template('applicants-and-mentors.html',
                           applicants=applicants)


if __name__ == '__main__':
    app.run(debug=True)
