import sqlite3

class Store:
    def __init__(self, db_name='reStore.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                login TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

        self.cursor.execute('DELETE FROM products')
        self.conn.commit()

        self.cursor.execute('DELETE FROM sqlite_sequence WHERE name="products"')
        self.conn.commit()

        self.cursor.executemany('INSERT INTO products (name, price) VALUES (?, ?)', [
            ('iPhone 15 Pro Max', 1199.0),
            ('iPhone 14 Plus', 799.0),
            ('iPhone 13', 599.0),
            ('AirPods Pro', 249.0),
            ('MacBook Pro', 3999.0),
            ('Apple Watch Ultra 2', 799.0),
            ('iPad Pro', 799.0),
            ('Apple TV 4K', 149.0)
        ])
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS shopping_cart (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                product_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id),
                FOREIGN KEY(product_id) REFERENCES products(id)
            )
        ''')
        self.conn.commit()

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                address TEXT,
                total_amount REAL,
                order_number INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')
        self.conn.commit()

    def close_connection(self):
        self.conn.close()