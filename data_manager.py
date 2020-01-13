import database_common
import psycopg2


@database_common.connection_handler
def get_mentor_names_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    WHERE first_name = %(first_name)s ORDER BY first_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_all_mentors(cursor):
    cursor.execute("""
                    SELECT first_name, last_name FROM mentors
                    ORDER BY last_name;
                   """
                   )
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_all_applicants(cursor):
    cursor.execute("""
                    SELECT first_name, last_name, phone_number, email, application_code FROM applicants
                    ORDER BY last_name;
                   """
                   )
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_nicknames(cursor):
    cursor.execute("""
                    SELECT first_name, nick_name, last_name FROM mentors
                    WHERE city='Miskolc'
                    ORDER BY nick_name;
                   """
                   )
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_names_and_phone_by_first_name(cursor, first_name):
    cursor.execute("""
                    SELECT first_name, last_name, phone_number FROM applicants
                    WHERE first_name = %(first_name)s ORDER BY last_name;
                   """,
                   {'first_name': first_name})
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def get_names_and_phone_by_part_email(cursor, part_email):
    cursor.execute(f"""
                    SELECT first_name, last_name, phone_number, email FROM applicants
                    WHERE email LIKE '%{part_email}%' ORDER BY last_name;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def insert_new_applicant(cursor, first_name, last_name, phone_number, email, application_code):
    try:
        cursor.execute(f"""
                        INSERT INTO applicants (first_name, last_name, phone_number, email, application_code) 
                        VALUES ('{first_name}', '{last_name}', '{phone_number}', '{email}', '{application_code}');
                       """)
        return f"{first_name} {last_name}, {phone_number}, {email} with application code {application_code} has been " \
               f"successfully added."
    except psycopg2.IntegrityError:
        return f"An applicant with application code {application_code} has already been added."
    # names = cursor.fetchall()
    # return names


@database_common.connection_handler
def update_applicant(cursor, first_name, last_name, phone_number):
    try:
        cursor.execute(f"""
                        UPDATE applicants 
                        SET phone_number = '{phone_number}'
                        WHERE first_name = '{first_name}' AND last_name = '{last_name}';
                       """)
        return f"The phone number of {first_name} {last_name}, was successfully changed to {phone_number}."
    except psycopg2.IntegrityError:
        return f"The applicant with application code {application_code} cannot be updated."
    # names = cursor.fetchall()
    # return names



@database_common.connection_handler
def get_applicant_details_by_first_name_last_name(cursor, first_name, last_name):
    cursor.execute(f"""
                    SELECT first_name, last_name, phone_number FROM applicants
                    WHERE first_name = '{first_name}' AND last_name = '{last_name}' ORDER BY last_name;
                   """)
    names = cursor.fetchall()
    return names


@database_common.connection_handler
def delete_applicant_by_part_email(cursor, part_email):
    try:
        cursor.execute(f"""
                        DELETE FROM applicants 
                        WHERE email LIKE '{part_email}';
                       """)
        return f"{part_email} applicants successfully deleted."
    except psycopg2.IntegrityError:
        return f'Applicants with the "{part_email}" cannot be deleted.'
