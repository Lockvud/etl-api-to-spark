import requests
import pandas as pd
import psycopg2

# 1. Получение данных
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data)

if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    df.to_csv("data/users.csv", index=False)
    print("Данные успешно сохранены в data/users.csv")
else:
    print(f"Ошибка при запросе данных: {response.status_code}")
    
# 2. Загрузка в PostgreSQL
conn = psycopg2.connect(
    host="localhost", port=5432,
    database="etldb", user="user", password="password"
)

cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS users")
cur.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        username TEXT,
        email TEXT,
        phone TEXT,
        website TEXT
    )
""")

for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO users (id, name, username, email, phone, website)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, tuple(row[["id", "name", "username", "email", "phone", "website"]]))

conn.commit()
cur.close()
conn.close()
print("Данные загружены в PostgreSQL")