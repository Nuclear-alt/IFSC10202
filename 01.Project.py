Seconds = 50000001

seconds_in_a_years = 365 * 24 * 60 * 60
years = Seconds // seconds_in_a_years
Seconds = Seconds - years * seconds_in_a_years

seconds_in_a_days = 24 * 60 * 60
days = Seconds // seconds_in_a_days
Seconds = Seconds - days * seconds_in_a_days

seconds_in_a_hours = 60 * 60
hours = Seconds // seconds_in_a_hours
Seconds = Seconds - hours * seconds_in_a_hours

minutes = Seconds // 60
Seconds = Seconds - minutes * 60

print("Years:", years)
print("Days:", days)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", Seconds)