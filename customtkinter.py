import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import date
from db import fetch_one, execute_query
from email_utils import send_mail
from utils import export_csv, show_analytics

class AppGUI:
    def __init__(self, db_conn, email_session):
        self.db_conn = db_conn
        self.email_session = email_session

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.root = ctk.CTk()
        self.root.title("Late Comers Management - Desktop App")
        self.root.geometry("800x600")

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        self.login_frame = ctk.CTkFrame(master=self.root)
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.title_label = ctk.CTkLabel(self.login_frame, text="PTE Login", font=ctk.CTkFont(size=20, weight="bold"))
        self.title_label.pack(pady=10)

        self.username_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Username")
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.login_frame, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=10)

        login_button = ctk.CTkButton(self.login_frame, text="Login", command=self.handle_login)
        login_button.pack(pady=10)

    def handle_login(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        result = fetch_one(self.db_conn, "SELECT * FROM ptes WHERE username=%s AND password=%s", (username, password))

        if result:
            self.logged_in_user = result
            self.create_main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials!")

    def create_main_screen(self):
        self.clear_screen()

        self.main_frame = ctk.CTkFrame(master=self.root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.heading = ctk.CTkLabel(self.main_frame, text="Late Comers Management", font=ctk.CTkFont(size=24, weight="bold"))
        self.heading.pack(pady=10)

        self.adm_label = ctk.CTkLabel(self.main_frame, text="Enter Student Admission No:")
        self.adm_label.pack(pady=5)

        self.adm_entry = ctk.CTkEntry(self.main_frame)
        self.adm_entry.pack(pady=5)

        mark_late_button = ctk.CTkButton(self.main_frame, text="Mark Late", command=self.mark_late)
        mark_late_button.pack(pady=10)

        export_button = ctk.CTkButton(self.main_frame, text="Export to CSV", command=self.export_records)
        export_button.pack(pady=5)

        analytics_button = ctk.CTkButton(self.main_frame, text="Show Analytics", command=show_analytics)
        analytics_button.pack(pady=5)

    def mark_late(self):
        adm_no = self.adm_entry.get().strip()
        if not adm_no:
            messagebox.showerror("Error", "Please enter a valid admission number.")
            return

        late_count_result = fetch_one(self.db_conn, "SELECT COUNT(*) FROM LateRecords WHERE admission_no=%s", (adm_no,))
        late_count = late_count_result[0] if late_count_result else 0

        if late_count < 3:
            reason = simpledialog.askstring("Reason", "Enter reason for being late:")
            if not reason:
                messagebox.showerror("Error", "Reason cannot be empty.")
                return

            execute_query(self.db_conn,
                          "INSERT INTO LateRecords (admission_no, date, reason) VALUES (%s, %s, %s)",
                          (adm_no, date.today(), reason))

            # Send email to parent
            parent_email_result = fetch_one(self.db_conn,
                                            "SELECT parent_email FROM SchoolRecords WHERE admission_no=%s",
                                            (adm_no,))
            if parent_email_result:
                parent_email = parent_email_result[0]
                subject = "Late Arrival Notification"
                body = f"Dear Parent,\n\nYour child (Admission No: {adm_no}) was marked late on {date.today()}.\nReason: {reason}\n\nRegards,\nSchool Administration"
                send_mail(self.email_session, parent_email, subject, body)

            messagebox.showinfo("Success", "Late record saved and email sent!")
        else:
            messagebox.showwarning("Limit Reached", "This student has already exceeded 3 late entries.")

    def export_records(self):
        export_csv(self.db_conn)
        messagebox.showinfo("Exported", "Records exported successfully to 'exported_data/late_records.csv'.")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        self.root.mainloop()
