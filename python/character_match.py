# Don't forget to run your tests!

# def is_character_match(string1, string2):
# 	str1_arr = sorted(list(string1.lower()))
# 	str2_arr = sorted(list(string2.lower()))

# 	for i,x in enumerate(str1_arr) :
# 		if str1_arr[i] != str2_arr[i]:
# 			return False

# 	return True

def is_character_match(str1, str2):
	# remove spaces
	str1 = ''.join(str1.split())
	str2 = ''.join(str2.split())

	# can't be anagrams if different number of characters
	if len(str1) != len(str2):
		return False

	# make all characters lowercase and convert to elements in a list
	str1_arr = list(str1.lower())
	str2_arr = list(str2.lower())

	for i in range(len(str1_arr)):
		target = str1_arr
		if str1_arr.count(target) != str2_arr.count(target):
			return False
	
	return True
	
# print(is_anagram('Anna Madrigal', 'A man and a girl'))
