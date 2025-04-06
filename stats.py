# Finds the number of words in the string of book
def num_words(text):
        words = text.split()
        word_count = len(words)
        return word_count

# Finds the number of times a character shows up 
def num_recurrances(text, word_count):
	lower_text = text.lower()
	lower_text_dict = {}
	for count in lower_text:
		if count in lower_text_dict:
			lower_text_dict[count] += 1
		else:
			lower_text_dict[count] = 1
	return lower_text_dict

# Sorts the lower_text_dict into a sorted list to be greatest to least amount
def sort_list(dict):
	sorted_list = []
	for char, count in dict.items():
		if char.isalpha() == True:
			sorted_list.append({"character": char, "count": count})	
	sorted_list.sort(key=lambda x: x["count"], reverse=True)
	
	return sorted_list


