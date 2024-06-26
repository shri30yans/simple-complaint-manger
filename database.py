import mysql.connector as m

class databaseClass():
    def __init__(self):
        self.conn = self.connection()

    def connection(self):
        conn = m.connect(host="localhost",user="root",password="Welcome1")
        if conn.is_connected():
            print("Connection is succesful.")
        return conn

    def intialize(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute('CREATE DATABASE IF NOT EXISTS complaint_manager_db')
        self.conn.commit()
        self.cursor.execute('USE complaint_manager_db')
        self.conn.commit()
        #self.cursor.execute("DROP TABLE issues")
        self.conn.commit()
        self.cursor.execute('''
                    CREATE TABLE IF NOT EXISTS issues
                    (id INTEGER(10) AUTO_INCREMENT PRIMARY KEY,
                    description VARCHAR(255),
                    house_no VARCHAR(255),
                    category VARCHAR(255),
                    status VARCHAR(20))
                    ''')
        self.conn.commit()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS login
            (username VARCHAR(255),
            password VARCHAR(20))
            ''')
        self.conn.commit()
    
    def get_all_issues(self):
        query = f"SELECT * FROM issues"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data
    
    def get_issues_for_house(self,house_no):
        query = f"SELECT * FROM issues WHERE house_no = {house_no}"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    
    def add_issue(self,description,house_no,category,status):
        query = f"INSERT INTO issues(description,house_no,category,status) VALUES('{description}','{house_no}','{category}','{status}')"
        self.cursor.execute(query)
        self.conn.commit()

    def get_password(self,username):
        query = f"SELECT * FROM login WHERE user_name = {username}"
        self.cursor.execute(query)
        data = self.cursor.fetchall()
        return data

    def add_account(self,username,password,house_no,):
        query = f"INSERT INTO login(username,password) VALUES('{username}','{password}','{house_no}',)"
        self.cursor.execute(query)
        self.conn.commit()

