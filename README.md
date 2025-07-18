# Мини ETL пайплайн: API → PostgreSQL → PySpark

## Описание
Проект демонстрирует простой поток обработки данных:
1. Получение пользователей с публичного API
2. Сохранение данных в CSV
3. Загрузка данных в PostgreSQL
4. Обработка с помощью Apache Spark
5. Фильтрация пользователей по домену email `.org`

## Используемые технологии
- Python (requests, pandas, psycopg2)
- PostgreSQL (через Docker)
- Apache Spark (PySpark)
- Docker Compose

## Как запустить

## Предварительные требования
Убедитесь, что у вас установлены:
- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

## Установка и запуск

1. **Клонируйте репозиторий и перейдите в директорию проекта:**
```bash
   git clone <URL-репозитория>
   cd <имя-папки-проекта>
```   
2. **Запустите контейнеры:**
```bash
docker-compose up --build
```

## Визуализация данных

Ниже представлен график распределения пользователей по доменам электронной почты.

![Распределение пользователей по доменам email](images/email_domain_distribution.png)