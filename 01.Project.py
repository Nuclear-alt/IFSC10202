
Seconds = 50000001
years = 365 * 24 * 60 * 60
years = Seconds // years
Seconds = Seconds - years

days = 24 * 60 * 60
days = Seconds // days
Seconds = Seconds - days

hours = 60 * 60
hours = Seconds // hours
Seconds = Seconds - hours

minutes = 60
minutes = Seconds // minutes

Seconds = Seconds - minutes

print("Years:", years)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", Seconds)