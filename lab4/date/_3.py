from datetime import datetime

current = datetime.now()
dwm = current.replace(microsecond=0)

print("Date without Microseconds:", dwm)
