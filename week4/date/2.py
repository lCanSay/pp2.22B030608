from datetime import datetime, timedelta

y = datetime.now() - timedelta(days = 1)
x = datetime.now()
t = datetime.now() + timedelta(days = 1)
print(y,x,t, sep = "\n")