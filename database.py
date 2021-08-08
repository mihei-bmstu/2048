import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS records (
    name text,
    score integer
)"""
            )
def get_best_result():
    cur.execute("""
    SELECT name, MAX(score) AS score FROM records
    GROUP BY name
    ORDER BY score DESC
    LIMIT 3
    """
                )
    return cur.fetchall()


def insert_result(name, score):
    cur.execute("""
        INSERT INTO records values ( ?, ?)
    """, (name, score))
    bd.commit()
