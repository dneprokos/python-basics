import itertools

# permutations
election = {1: "Barb", 2: "Karen", 3: "Erin"}
for p in itertools.permutations(election):
    print(p)

'''
(1, 2, 3)
(1, 3, 2)
(2, 1, 3)
(2, 3, 1)
(3, 1, 2)
(3, 2, 1)
'''

# combinations
colors = ["Red", "Yellow", "Green", "Purple", "Orange", "Yellow", "Pink"]

for c in itertools.combinations(colors, 2):
    print(c)

'''
('Red', 'Yellow')
('Red', 'Green')
('Red', 'Purple')
('Red', 'Orange')
('Red', 'Yellow')
('Red', 'Pink')
('Yellow', 'Green')
('Yellow', 'Purple')
('Yellow', 'Orange')
('Yellow', 'Yellow')
('Yellow', 'Pink')
('Green', 'Purple')
('Green', 'Orange')
('Green', 'Yellow')
('Green', 'Pink')
('Purple', 'Orange')
('Purple', 'Yellow')
('Purple', 'Pink')
('Orange', 'Yellow')
('Orange', 'Pink')
('Yellow', 'Pink')
'''

