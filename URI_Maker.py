from os import system
ip_address = str(input("Please enter the ip:\n"))
passname = str(input("Please enter the password:\n"))
print("source venv/bin/activate")
print(f'export DATABASE_URI="mysql+pymysql://root:{passname}@{ip_address}:3306/flaskappdb"')

