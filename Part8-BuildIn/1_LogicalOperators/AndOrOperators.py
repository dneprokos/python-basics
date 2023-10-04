isRaining = True
isSunny = True

# AND
# True and True -> True
# False and True -> False
# True and False -> False
# False and False -> True

if isRaining and isSunny:
    print("We might see Rainbow")

# Or
# True and True -> True
# False and True -> True
# True and False -> True
# False and False -> False

if isRaining or isSunny:
    print("It might be rainy or it might be sunny")

# NOT
# true --> false
# false --> true

if not isRaining:
    print("It must be raining")

ages = [12, 18, 39, 87, 7, 2]
for age in ages:
    isAdult = age > 17;
    if not isAdult:
        print("Being " + str(age) + " does not make you an adult.")
