from datetime import datetime, timedelta
a = datetime(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")),  int(input("Hour: ")),  int(input("Minute: ")),  int(input("Second: ")),  int(input("Microsecond: ")))
y = datetime.now() - a
print(y.total_seconds())