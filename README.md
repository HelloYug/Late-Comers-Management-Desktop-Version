### Late Comers Management System - Desktop Application

A modern, secure **Late Comers Management System** developed in **Python** using **CustomTkinter** for GUI and **MySQL** as the database.

This project helps schools **digitally manage** late-coming students with a proper **strike policy**, **automatic parental email alerts**, **record exports**, and **visual analytics**.

---

## ✨ Features

- **Secure PTE (Staff) Login** system
- **Mark students late** with a reason
- **Automatic email notifications** to parents when a student is late
- **Three-strike rule** enforcement for repeated latecomers
- **Export latecomer records** into **CSV files** for reporting
- **Visual Analytics** using **matplotlib** (bar graph of student lateness)
- **Environment-based configuration** for database and email settings
- **Modular Python project structure** for easy maintenance

---

## 🛠️ Technologies Used

- **Python 3.x**
- **CustomTkinter** (for modern GUI)
- **MySQL** (Database)
- **SMTP (Gmail)** (for sending emails)
- **Matplotlib** (for analytics)
- **dotenv** (for environment variables)

---

## 🗂️ Project Structure

DesktopApp/
├── main.py              # Entry point of the application
├── db.py                # Database connection functions (MySQL)
├── email_utils.py       # Email sending functions via SMTP
├── gui.py               # CustomTkinter-based GUI code
├── utils.py             # Helper functions (Export CSV, Show Analytics)
├── requirements.txt     # List of required Python libraries
├── .env.example         # Template for environment variables (MySQL + Email credentials)
├── README.md            # Complete project documentation
├── exported_data/       # Folder where CSV exported files are saved
│
├── assets/              # (Optional) School logo, icons, or images
│   ├── school_logo.png
│   └── default_student_photo.png
│
├── student_photos/      # (Optional) Folder to store student profile images if needed


---

## ⚙️ Setup Instructions

# 1. Clone the Repository
```bash
cd latecomers-desktop
git clone https://github.com/yourusername/latecomers-desktop.git
```

# 2. Install Required Packages
```bash
pip install -r requirements.txt
```

# 3. Setup Environment Variables
Fill in your MySQL and email credentials:

```
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_db_password
DB_NAME=LateComersDB

SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
```

# 4. Setup MySQL Database
Create a database called LateComersDB and run these tables:
```sql
CREATE TABLE SchoolRecords (
  admission_no INT PRIMARY KEY,
  student_name VARCHAR(100),
  parent_email VARCHAR(100)
);

CREATE TABLE LateRecords (
  id INT AUTO_INCREMENT PRIMARY KEY,
  admission_no INT,
  date DATE,
  reason TEXT
);

CREATE TABLE ptes (
  username VARCHAR(50) PRIMARY KEY,
  password VARCHAR(100)
);
```

# 5. Run the Application
```bash
python main.py
```

---

## 🎯 How It Works
- PTE logs in using credentials.
- Student Admission No is entered and late reason is recorded.
- Three-strike system:
- 1st & 2nd late: Warn the parent via email.
- 3rd late: Final warning or action.
- All late records are saved in the MySQL database.
- Export all records easily as a CSV file.
- Visual analytics available via simple bar charts.

---

## ✅ Requirements
- Python 3.8+
- MySQL Server
- Internet Connection (for sending emails)

--- 

## 👨‍💻 Author

**Yug Agarwal**
- 📧 [yugagarwal704@gmail.com](mailto:yugagarwal704@gmail.com)
- 🔗 GitHub – [@HelloYug](https://github.com/HelloYug)