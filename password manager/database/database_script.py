import sqlite3
import os

db = os.path.abspath(r"database\PasswordManager_DB.db")     #database absolute path

#connect to database and setup cursor
connection = sqlite3.connect(db)
cursor = connection.cursor()

#search username from USERS(used to get login informations)
def search_user(username):
    cursor.execute(f"""
    SELECT * FROM users WHERE username = '{username}';
    """)
    return cursor.fetchone()

#add new user to USERS, then create a new INFO table to it
def add_user(username, password, preferredTheme="default"):
    cursor.execute(f"""
    INSERT INTO users (username, passwordKey, preferredTheme)
    VALUES   ('{username}', '{password}', '{preferredTheme}');
    """)
    cursor.execute(f"""
    CREATE TABLE {username}Info (
    _id          INTEGER       NOT NULL
                               PRIMARY KEY,
    username     VARCHAR (255),
    eMail        VARCHAR (255),
    appName      VARCHAR (255),
    passwordKey  VARCHAR (255),
    creationDate VARCHAR (255) );
    """)
    connection.commit()

#sheck if username exist in USERS or not(used in signup_script)
def isUsernameAvailable(username):
    cursor.execute(f"""
    SELECT * FROM users WHERE username = '{username}';
    """)
    return True if not cursor.fetchall() else False

#save new informations to user INFO table
def add_info(PmUsername, username, email, appName, password, creationDate):
    cursor.execute(f"""
    INSERT INTO {PmUsername}Info (username, eMail, appName, passwordKey, creationDate)
    VALUES ('{username}', '{email}', '{appName}', '{password}', '{creationDate}');
    """)
    connection.commit()

#search informations from user INFO table
def search_info(PmUsername, searchBy, searchKeyword):
    cursor.execute(f"""
    SELECT * FROM {PmUsername}Info WHERE {searchBy} = '{searchKeyword}';
    """)
    return cursor.fetchall()

#return all info saved in user INFO table
def return_all_info(PmUsername):
    cursor.execute(f"SELECT * FROM {PmUsername}Info ;")
    return cursor.fetchall()

#delete an info row
def delete_info(PmUsername, info_lst):
    usn, email, appName, pswd, date = info_lst
    cursor.execute(f"""
    DELETE FROM {PmUsername}Info WHERE
    username = '{usn}' and
    email = '{email}' and 
    appName = '{appName}' and
    passwordKey = '{pswd}' and
    creationDate = '{date}';
    """)
    connection.commit()

#update an info row
def update_info(PmUsername, old_info_lst, new_info_lst):
    old_usn, old_email, old_appName, old_pswd, old_date = old_info_lst
    new_usn, new_email, new_appName, new_pswd, new_date = new_info_lst
    cursor.execute(f"""
    UPDATE {PmUsername}Info
    SET 
        username = '{new_usn}',
        email = '{new_email}',
        appName = '{new_appName}',
        passwordKey = '{new_pswd}',
        creationDate = '{new_date}'
    WHERE
        username = '{old_usn}' and
        email = '{old_email}' and
        appName = '{old_appName}' and
        passwordKey = '{old_pswd}' and
        creationDate = '{old_date}'
    """)
    connection.commit()

#remove a user INFO table
def clear_user_info(username):
    cursor.execute(f"""
    DELETE FROM {username}Info;
    """)
    connection.commit()

#remove user from USERS, then remove it INFO table
def remove_user(username):
    cursor.execute(f"""
    DELETE FROM users
    WHERE username= '{username}';
    """)
    cursor.execute(f"""
    DROP TABLE {username}INFO;
    """)
    connection.commit()