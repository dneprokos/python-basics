# Example of iterators in Python

# Iterators are used to iterate through a collection of data types.

days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysPoland = ["Niedziela", "Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek", "Sobota"]
daysUkraine = ["Неділя", "Понеділок", "Вівторок", "Середа", "Четвер", "П'ятниця", "Субота"]

daysDict = {"Sun": "Niedziela", "Mon": "Poniedziałek", "Tue": "Wtorek", "Wed": "Środa", "Thu": "Czwartek", "Fri": "Piątek", "Sat": "Sobota"}

# TODO: Itereate over the list
print("------")
print("Using iter:")
i = iter(days) # Create an iterator object
print(next(i)) # Sun
print(next(i)) # Mon
print(next(i)) # Tue

# TODO: Iterate over dictionary
print("------")
print("Using iter:")
for key in daysDict:
    print(key, ":", daysDict[key]) # Sun : Niedziela, Mon : Poniedziałek, Tue : Wtorek, Wed : Środa, Thu : Czwartek, Fri : Piątek, Sat : Sobota

print("------")
print("Using iteritems:")
for k, v in daysDict.items():
    print(k, ":", v) # Sun : Niedziela, Mon : Poniedziałek, Tue : Wtorek, Wed : Środa, Thu : Czwartek, Fri : Piątek, Sat : Sobota

# TODO: Use enumerate function
print("------")
for i, m in enumerate(days, start=1):
    print(i, m) # 0 Sun, 1 Mon, 2 Tue, 3 Wed, 4 Thu, 5 Fri, 6 Sat

# Use zip function
print("------")
for i, m in zip(days, daysPoland):
    print(i, m) # Sun Niedziela, Mon Poniedziałek, Tue Wtorek, Wed Środa, Thu Czwartek, Fri Piątek, Sat Sobota

# TODO: Combine iter and zip functions
print("------")
for i, m in zip(iter(days), daysPoland):
    print(i, m) # Sun Niedziela, Mon Poniedziałek, Tue Wtorek, Wed Środa, Thu Czwartek, Fri Piątek, Sat Sobota

# TODO: Combine enumerate and zip functions
print("------")
for i, m in enumerate(zip(days, daysPoland), start=1):
    print(i, m) # 1 ('Sun', 'Niedziela'), 2 ('Mon', 'Poniedziałek'), 3 ('Tue', 'Wtorek'), 4 ('Wed', 'Środa'), 5 ('Thu', 'Czwartek'), 6 ('Fri', 'Piątek'), 7 ('Sat', 'Sobota')