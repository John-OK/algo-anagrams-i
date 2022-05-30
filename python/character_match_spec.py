from character_match import is_character_match

# This should return a bunch of trues
print(is_character_match('charm', 'march') == True)
print(is_character_match('zach', 'attack') == False)
print(is_character_match('CharM', 'mARcH') == True)
print(is_character_match('abcde2', 'c2abed') == True)
print(is_character_match('reduces', 'rescued') == True)
print(is_character_match('reduces', 'secured') == True)
print(is_character_match('reduces', 'seducer') == True)
print(is_character_match('teachers', 'cheaters') == True)
print(is_character_match('teachers', 'hectares') == True)
print(is_character_match('retails', 'saltier') == True)
print(is_character_match('retails', 'realist') == True)
print(is_character_match('painter', 'repaint') == True)
print(is_character_match('retails', 'pertain') == True)

print("This test is for the challenge quesiton")
print(is_character_match('Anna Madrigal', 'A man and a girl') == True)


# Can you translate this driver code to unit tests?
