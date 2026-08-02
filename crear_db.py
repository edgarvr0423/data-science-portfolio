import sqlite3

# Conectar a la base de datos (se crea el archivo si no existe)
conn = sqlite3.connect('empresa.db')
cursor = conn.cursor()

# Crear tabla de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id_cliente INTEGER PRIMARY KEY,
    nombre TEXT NOT NULL,
    pais TEXT NOT NULL,
    edad INTEGER NOT NULL,
    compras_totales INTEGER NOT NULL
)
''')

# Insertar datos de prueba
datos = [
    (1, 'Carlos Gómez', 'México', 28, 6),
    (2, 'Ana Martínez', 'Colombia', 35, 3),
    (3, 'Luis Rodríguez', 'México', 22, 10),
    (4, 'Marta Fernández', 'España', 42, 8),
    (5, 'Javier López', 'Colombia', 31, 7),
    (6, 'Sofia Torres', 'Argentina', 26, 4),
    (7, 'Diego Ramos', 'México', 39, 9)
]

cursor.executemany('''
INSERT OR REPLACE INTO clientes (id_cliente, nombre, pais, edad, compras_totales)
VALUES (?, ?, ?, ?, ?)
''', datos)

conn.commit()
conn.close()
print("¡Base de datos 'empresa.db' creada con éxito!")