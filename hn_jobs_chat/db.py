# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/util/db.ipynb.

# %% auto 0
__all__ = ['dbName', 'dbUser', 'dbPassword', 'connectToDB']

# %% ../nbs/util/db.ipynb 2
import psycopg2

dbName = 'Bumpant'
dbUser = 'Bumpant'
dbPassword = 'ampegskb'

def connectToDB():
    conn = psycopg2.connect("dbname=" + dbName + " user=" + dbUser + " password=" + dbPassword)
    cursor = conn.cursor()
    return conn, cursor

