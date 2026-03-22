from database import get_db

# ---------- USER ----------
def create_user(username, password):
    conn = get_db()
    conn.execute("INSERT INTO users (username,password) VALUES (?,?)",
                 (username, password))
    conn.commit()
    conn.close()

def get_user(username, password):
    conn = get_db()
    user = conn.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    ).fetchone()
    conn.close()
    return user


# ---------- ITEMS ----------
def get_items(user_id):
    conn = get_db()
    items = conn.execute(
        "SELECT * FROM items WHERE user_id=?",
        (user_id,)
    ).fetchall()
    conn.close()
    return items

def add_item(data, user_id):
    conn = get_db()
    conn.execute(
        "INSERT INTO items (name, quantity, price, category, user_id) VALUES (?, ?, ?, ?, ?)",
        (data["name"], data["quantity"], data["price"], data["category"], user_id)
    )
    conn.commit()
    conn.close()

def update_item(data, id, user_id):
    conn = get_db()
    conn.execute(
        "UPDATE items SET name=?, quantity=?, price=?, category=? WHERE id=? AND user_id=?",
        (data["name"], data["quantity"], data["price"], data["category"], id, user_id)
    )
    conn.commit()
    conn.close()

def delete_item(id, user_id):
    conn = get_db()
    conn.execute(
        "DELETE FROM items WHERE id=? AND user_id=?",
        (id, user_id)
    )
    conn.commit()
    conn.close()