# 🕒 Time Calculator

This is a simple Python project that implements a **Time Calculator**. It adds a duration to a given start time and returns the new time in 12-hour format with AM/PM, handling:

- Minute and hour overflow
- Day transitions (e.g., "next day", "2 days later")
- Optional day of the week
- Case-insensitive day input

---

## 📌 Features

- ✅ Add hours and minutes to a 12-hour formatted time
- ✅ Handles AM/PM transition correctly
- ✅ Calculates and displays the correct day of the week (if provided)
- ✅ Displays how many days later if duration spans multiple days

---

## 🧠 Example Usage

```python
from time_calculator import add_time

print(add_time("3:00 PM", "3:10"))  
# Returns: '6:10 PM'

print(add_time("11:30 AM", "2:32", "Monday"))  
# Returns: '2:02 PM, Monday'

print(add_time("10:10 PM", "3:30"))  
# Returns: '1:40 AM (next day)'

print(add_time("11:43 PM", "24:20", "tuesday"))  
# Returns: '12:03 AM, Thursday (2 days later)'

print(add_time("6:30 PM", "205:12"))  
# Returns: '7:42 AM (9 days later)'
