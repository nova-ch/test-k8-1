
import pandas as pd
import json
import oracledb
from time import time

print("Import finished")

output_dir = "/app/output"

# Establish a connection to Oracle
conn = oracledb.connect(user=database_user, password=database_password, dsn=dsn)

query = """
SELECT * 
FROM ATLAS_PANDA.taskS_statuslog
WHERE JEDITASKID IN (
    SELECT DISTINCT JEDITASKID
    FROM ATLAS_PANDA.taskS_statuslog
    WHERE STATUS = 'scouting'
    AND JEDITASKID = 40880168
)
ORDER BY MODIFICATIONTIME
"""

# Using cursor to execute the query
try:
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetching data into a DataFrame
    df = pd.read_sql(query, con=conn)
    
    # Display DataFrame info and shape
    print(df.info(), df.shape)
    
    # Save the DataFrame to a CSV file
    df.to_csv(f"{output_dir}/test.csv", index=False)
    
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()

