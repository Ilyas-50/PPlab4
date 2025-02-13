from datetime import datetime
date1 = datetime.now()

inp = input("YYYY MM DD HH MM SS: ")
year, month, day, hour, minute, second = map(int, inp.split())
date2 = datetime(year, month, day, hour, minute, second)

difference = abs((date1 - date2).total_seconds())

print(f"Difference in seconds: {difference:.0f}")
