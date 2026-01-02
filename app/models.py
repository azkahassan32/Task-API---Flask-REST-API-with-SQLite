from app.database import get_db_connection

def create_table():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)
    conn.commit()       #Saves changes to the DB
    conn.close()        #Always close connections to avoid locking the DB

def get_all_tasks():
    conn = get_db_connection()
    tasks = conn.execute("SELECT * FROM tasks").fetchall() #.fetchall() → Returns a list of all rows.
    conn.close()
    return tasks

def get_task(task_id):
    conn = get_db_connection()
    task = conn.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)      # ? Placeholder for SQL parameter (prevents SQL injection!).
    ).fetchone()            #Returns a single row
    conn.close()
    return task

def create_task(title):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO tasks (title) VALUES (?)", (title,)
    )
    conn.commit()
    conn.close()

def update_task(task_id, completed):
    conn = get_db_connection()
    conn.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?",
        (completed, task_id)
    )
    conn.commit()
    conn.close()

def delete_task(task_id):
    conn = get_db_connection()
    conn.execute(
        "DELETE FROM tasks WHERE id = ?", (task_id,)
    )
    conn.commit()
    conn.close()
