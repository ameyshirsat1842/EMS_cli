from db_connection import create_connection, close_connection

def add_employee(first_name, last_name, email, ph_number, job):
    conn = create_connection()
    if not conn:
        print("Failed to create database connection.")
        return
    cursor = conn.cursor()
    try:
        add_employee_query = ("INSERT INTO employees "
                              "(first_name, last_name, email, ph_number, job) "
                              "VALUES (%s, %s, %s, %s, %s)")
        data_employee = (first_name, last_name, email, ph_number, job)
        cursor.execute(add_employee_query, data_employee)
        conn.commit()
        print("Employee added successfully!")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        close_connection(conn)

def get_employee(emp_id):
    conn = create_connection()
    if not conn:
        print("Failed to create database connection.")
        return
    cursor = conn.cursor()
    try:
        query = "SELECT * FROM employees WHERE id = %s"
        cursor.execute(query, (emp_id,))
        result = cursor.fetchone()
        if result:
            print("Employee details: ", result)
        else:
            print("Employee not found!")
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        cursor.close()
        close_connection(conn)

def update_employee(emp_id, first_name=None, last_name=None, email=None, ph_number=None, job=None):
    conn = create_connection()
    if not conn:
        print("Failed to create database connection.")
        return
    cursor = conn.cursor()
    try:
        update_query = "UPDATE employees SET "
        updates = []
        data = []
        if first_name:
            updates.append("first_name = %s")
            data.append(first_name)
        if last_name:
            updates.append("last_name = %s")
            data.append(last_name)
        if email:
            updates.append("email = %s")
            data.append(email)
        if ph_number:
            updates.append("ph_number = %s")
            data.append(ph_number)
        if job:
            updates.append("job = %s")
            data.append(job)

        if updates:
            update_query += ", ".join(updates) + " WHERE id = %s"
            data.append(emp_id)
            cursor.execute(update_query, tuple(data))
            conn.commit()
            print("Employee updated successfully!")
        else:
            print("No updates provided.")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        close_connection(conn)

def delete_employee(emp_id):
    conn = create_connection()
    if not conn:
        print("Failed to create database connection.")
        return
    cursor = conn.cursor()
    try:
        delete_query = "DELETE FROM employees WHERE id = %s"
        cursor.execute(delete_query, (emp_id,))
        conn.commit()
        print("Employee deleted successfully!")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
    finally:
        cursor.close()
        close_connection(conn)
