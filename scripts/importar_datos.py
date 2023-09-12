import sqlite3
import json

try:
    conn = sqlite3.connect("MOCK_DATA.db")
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS datos (
                   id INTEGER PRIMARY KEY,
                   first_name TEXT,
                   last_name TEXT,
                   email TEXT,
                   gender TEXT,                  
                   "Plan de Salud" TEXT,
                   phone TEXT
               )''')
    with open('MOCK_DATA.json', 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        mitad = len(data) // 2
        insertar_datos = data[:mitad]

        for i in insertar_datos:
            id_persona = i['id']
            first_name = i['first_name']
            last_name = i['last_name']
            email = i['email']
            gender = i['gender']
            plan_de_salud = i['Plan de Salud']
            phone = i['phone']
            cursor.execute('''INSERT INTO datos(
                           id, 
                           first_name, 
                           last_name,
                           email, 
                           gender, 
                           "Plan de Salud", 
                           phone)
                           VALUES(?, ?, ?, ?, ?, ?, ?)''',
                           (id_persona, first_name, last_name, email, gender, plan_de_salud, phone))
    conn.commit()
except sqlite3.Error as e:
    print("Error al conectar con la base de datos", e)
finally:
    if conn:
        conn.close()
