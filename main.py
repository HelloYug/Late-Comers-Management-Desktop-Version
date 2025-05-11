import customtkinter as ctk
from customtkinter import AppGUI
from db import init_db_connection, close_db_connection
from email_utils import init_email_session, close_email_session
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')

def main():
    db_conn = init_db_connection()
    email_session = init_email_session()

    app = AppGUI(db_conn, email_session)
    app.run()

    close_db_connection(db_conn)
    close_email_session(email_session)

if __name__ == '__main__':
    main()
