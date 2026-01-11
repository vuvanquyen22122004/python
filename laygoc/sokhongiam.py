from datetime import datetime
a=datetime.strptime(input(),"%d/%m/%Y")
b=datetime.strptime(input(),"%d/%m/%Y")
print((b-a).days)
