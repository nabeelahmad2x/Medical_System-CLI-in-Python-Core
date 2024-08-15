import psycopg2

connection = psycopg2.connect(
    database = "medical_db",
    host = 'localhost',
    user = 'postgres',
    password = 'postgres1234',
    port = '5432'
)


cursor = connection.cursor()

