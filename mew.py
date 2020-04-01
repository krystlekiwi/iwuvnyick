import xmltodict
import pyodbc
with open('test.xml') as nyan:
    test=xmltodict.parse(nyan.read())