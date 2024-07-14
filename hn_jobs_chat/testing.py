# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/testing.ipynb.

# %% auto 0
__all__ = ['conn', 'cur', 'connect']

# %% ../nbs/testing.ipynb 7
import psycopg2

def connect():
    conn = psycopg2.connect("dbname=Bumpant user=Bumpant password=ampegskb")
    cur = conn.cursor()
    return conn, cur

conn = psycopg2.connect("dbname=Bumpant user=Bumpant password=ampegskb")
cur = conn.cursor()

cur.execute(
    """CREATE TABLE IF NOT EXISTS parsedPosts (
        id SERIAL PRIMARY KEY, 
        hnuser TEXT, 
        date TIMESTAMP, 
        comment TEXT,
        embedding vector(1536)
        );"""
    )

conn.commit()    
