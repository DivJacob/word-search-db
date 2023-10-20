import pyodbc 

with open('FreqWords.csv', 'r') as file:
    # Create an empty list to store the lines
    lines = []

    # Iterate over the lines of the file
    for line in file:
        line = line.strip()
        lines.append(line.lower())


dict = {}
for word in lines:
    arr = [0] * 26
    if word =='FreqWords':
        continue
    for letter in word:
        if not letter.isalpha():
            continue
        indx = ord(letter)-ord('a')
        arr[indx] += 1
    dict[word] = arr

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-3K0CDKQ'
DATABASE_NAME = 'SpatialDatabase'

connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection = yes;

        """

conn = pyodbc.connect(connection_string) 
cursor = conn.cursor()


for key, values in dict.items():
    values_str = "'POINT (" + ' '.join(map(str, values)) + ")'" 
    key_str = f"'{key}'"
    insert_sql = f"INSERT INTO SpatialPoints VALUES (geometry::STPointFromText({values_str}, 4326), {key_str})"
    print(insert_sql)
    cursor.execute(insert_sql)

conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()