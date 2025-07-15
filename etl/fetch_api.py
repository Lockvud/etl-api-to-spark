import requests
import pandas as pd

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