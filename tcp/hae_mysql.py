
import mysql.connector
import csv
import os
from dotenv import load_dotenv
from pathlib import Path

# Luetaan ympäristömuuttujat .env-tiedostosta
# Haetaan .env samasta kansiosta kuin Python-skripti
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

DB_HOST = os.getenv("DB_HOST")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

GROUP_ID = 34

# Projektin juurikansio
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Measurements-kansion polku
OUTPUT_DIR = PROJECT_ROOT / "measurements"

# Luodaan kansio automaattisesti, jos sitä ei ole
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# CSV-tiedoston polku
CSV_FILE = OUTPUT_DIR / "mittaukset.csv"

connection = None
cursor = None

try:
    connection = mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

    print("Yhteys MySQL-palvelimeen onnistui!")

    cursor = connection.cursor()

    query = """
        SELECT id, timestamp, groupid, from_mac,
               sensorvalue_a, sensorvalue_b, sensorvalue_c, sensorvalue_d
        FROM rawdata
        WHERE groupid = %s
    """

    cursor.execute(query, (GROUP_ID,))
    rows = cursor.fetchall()

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "id", "timestamp", "groupid", "from_mac",
            "direction", "x", "y", "z"
        ])

        writer.writerows(rows)

    print(f"Haettiin {len(rows)} mittausta.")
    print("Tiedot tallennettu tiedostoon mittaukset.csv")

except mysql.connector.Error as err:
    print(f"MySQL-virhe: {err}")

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
        print("MySQL-yhteys suljettu.")
