import mysql.connector
from odoo import models, fields

class MySQLConnection(models.Model):
    _name = 'mi_modulo.mysql_connection'
    _description = 'Conexión a MySQL'

    def conectar_mysql(self):
        try:
            conexion = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="api_bd"
            )
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios")
            resultado = cursor.fetchall()
            conexion.close()
            return resultado
        except Exception as e:
            return f"Error de conexión: {str(e)}"
