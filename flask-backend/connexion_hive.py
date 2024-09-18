from pyhive import hive

# Hive connection parameters
hive_host = 'hive-server'
hive_port = 10000
hive_database = 'default'

# Create a connection to Hive
conn = hive.Connection(
    host=hive_host,
    port=hive_port,
    database=hive_database
)

# Create a cursor
cursor = conn.cursor()

# Create a Hive table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS users (
    id STRING,
    nom STRING,
    prenom STRING,
    age INT,
    email STRING,
    preferences ARRAY<STRING>,
    solde FLOAT,
    ne INT
)
STORED AS PARQUET
"""
cursor.execute(create_table_query)

# Example user data
user_data = [
    ('1', 'Dupont', 'Jean', 30, 'jean.dupont@example.com', ['sports', 'music'], 2500.75, 3),
    ('2', 'Martin', 'Marie', 25, 'marie.martin@example.com', ['tech', 'travel'], 3200.00, 2),
    ('3', 'Durand', 'Pierre', 40, 'pierre.durand@example.com', ['cooking', 'hiking'], 4200.50, 4)
]

# Insert user data into the Hive table
insert_query = """
INSERT INTO TABLE users VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
for user in user_data:
    cursor.execute(insert_query, user)

# Commit the transaction
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()

print("User data inserted successfully into Hive table.")
