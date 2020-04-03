import xmltodict
import pyodbc
import mysql.connector

with open('test.xml') as nyan:
    test=xmltodict.parse(nyan.read())

meooowwww = mysql.connector.connect(user='root', password='0412',
    host='127.0.0.1', database='val')

kirB = meooowwww.cursor(buffered=False)

query = (
    "SELECT * FROM pet"
)

kirB.execute(query)

for kitties in kirB:
    print(kitties)

print ( '............................................ =^.^=')

kirB = meooowwww.cursor(buffered=False)
query2 = (
    "UPDATE pet SET cuteness = '69' WHERE name = 'Pebbles'"
)

kirB.execute(query2)
kirB.execute(query)

for kitties in kirB:
    print(kitties)

print('it end k')

meooowwww.commit()
meooowwww.close()