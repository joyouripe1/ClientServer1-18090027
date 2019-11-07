days = {"senin": "SENIN",
        "selasa": "SELASA",
        "rabu": "RABU",
        "kamis": "KAMIS",
        "jumat": "JUMAT"}

for day in days:
    print(day)
print("-----------------------\n")

for day in days:
    print(days[day])
print("-----------------------\n")

days["sabtu"] = "SABTU"
for day in days:
    print(days[day])
print("-----------------------\n")

days.pop("jumat")
for day in days:
    print(days[day])
print("-----------------------\n")