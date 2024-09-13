    # Connect to the database

import psycopg2
from pgvector.psycopg2 import register_vector

dbName = 'Bumpant'
dbUser = 'Bumpant'
dbPassword = 'ampegskb'

def setupVector():
    conn = psycopg2.connect("dbname=" + dbName + " user=" + dbUser + " password=" + dbPassword)
    cursor = conn.cursor()

    cur = conn.cursor()
    cur.execute('CREATE EXTENSION IF NOT EXISTS vector')

    conn.commit()
    conn.close()


def connectToDB():
    conn = psycopg2.connect("dbname=" + dbName + " user=" + dbUser + " password=" + dbPassword)
    cursor = conn.cursor()
    return conn, cursor

def searchDB(query, params):
    conn, cursor = connectToDB()
    register_vector(conn)
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results
