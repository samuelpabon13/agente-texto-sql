import os
import psycopg2
from fastapi import FastAPI

app = FastAPI(title="Agente Texto a SQL")


def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
    )


@app.get("/health")
def health():
    return {"estado": "ok"}


@app.get("/db-check")
def db_check():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT COUNT(*) FROM productos;")
            total = cur.fetchone()[0]
    finally:
        conn.close()
    return {"conexion": "exitosa", "total_productos": total}


@app.get("/productos")
def productos():
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT id, nombre, precio FROM productos;")
            filas = cur.fetchall()
    finally:
        conn.close()
    return [{"id": f[0], "nombre": f[1], "precio": float(f[2])} for f in filas]