from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# 1. Создание сессии
spark = SparkSession.builder \
    .appName("Process Users CSV") \
    .getOrCreate()

# 2. Чтение CSV
df = spark.read.option("header", True).csv("/data/users.csv")

print("Данные:")
df.show()

# 3. Фильтрация email на .org
filtered_df = df.filter(col("email").endswith(".org"))

print("Отфильтрованные пользователи с .org:")
filtered_df.show()

# 4. Сохранение
filtered_df.write.mode("overwrite").option("header", True).csv("/data/filtered_users.csv")

print("Файл сохранён в /data/filtered_users.csv")
