import os
import csv
import matplotlib.pyplot as plt
from db import fetch_all

def export_csv(db_conn):
    query = "SELECT * FROM LateRecords"
    records = fetch_all(db_conn, query)
    export_path = os.path.join(os.getcwd(), "exported_data", "late_records.csv")
    os.makedirs(os.path.dirname(export_path), exist_ok=True)

    with open(export_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Admission No", "Date", "Reason"])
        for record in records:
            writer.writerow(record)

def show_analytics():
    data = {"0-1": 10, "2-3": 5, "4+": 2}  # Sample data, can be dynamic
    labels = list(data.keys())
    values = list(data.values())

    plt.bar(labels, values, color="skyblue")
    plt.xlabel("Late Counts")
    plt.ylabel("Number of Students")
    plt.title("Late Arrival Analytics")
    plt.tight_layout()
    plt.show()
