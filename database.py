import mysql.connector

from config import Config


def get_connection():

    connection = mysql.connector.connect(

        host=Config.MYSQL_HOST,

        user=Config.MYSQL_USER,

        password=Config.MYSQL_PASSWORD,

        database=Config.MYSQL_DATABASE

    )

    return connection


def get_cursor(

    dictionary=True

):

    connection = get_connection()

    cursor = connection.cursor(

        dictionary=dictionary

    )

    return connection, cursor