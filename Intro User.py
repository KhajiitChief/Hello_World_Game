caffine = input()
if caffine == "coffee":
    caffine = 100
elif caffine == "tea":
    caffine = 60
elif caffine == "energy drink":
    caffine = 300

value1 = caffine/2
value2 = value1/2
value3 = value2/4
print('After 6 hours ' + str(value1))
print(f"After 12 hours {value2}")
print(f"After 24 hours {value3}")


