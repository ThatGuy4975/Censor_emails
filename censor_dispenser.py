single_string_sample_text = "bada bee da be da bo bo be ba be de doe learning algorithms cha cha cha HOY."
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# def censor_single_phrase(email_input) :
# 	#defining word to be censored
# 	censored_phrase = "learning algorithms"
# 	if censored_phrase in email_input :
# 		new_input = email_input.replace(censored_phrase, "[Redacted]")
# 	return new_input

def censor_open_words(old_input) :
	split_email_input = old_input.split(' ')
	new_input = []
	for word in split_email_input :
		#for words without paragraphs
			if word.lower() in proprietary_terms :
				for letter in word :
					new_input.append('*')
				new_input.append(' ')
			else :
				new_input.append(word + ' ')

	joined_email_input = ''.join(new_input)
	return joined_email_input

def censor_paragraph_words(old_input) :
	split_input = old_input.split(' ')
	new_input = []
	for word in split_input :
		#for words without paragraphs
		if "\n" not in word:
			if word.lower() in proprietary_terms :
				for letter in word :
					new_input.append('*')
				new_input.append(' ')
			else :
				new_input.append(word + ' ')
		#for words in between paragraphs
		else :
			paragraph_words = word.split("\n")
			# print(paragraph_words)
			for word in paragraph_words :
				if word.lower() in proprietary_terms :
					for letter in word :
						new_input.append('*')
					new_input.append(' ')
				else :
					if word == paragraph_words[-1] :
						new_input.append(word + ' ')
					else:
						new_input.append(word + '\n')

	joined_email_input = ''.join(new_input)				
	return joined_email_input



def censor_multiple_phrases(email_input) :
	before_censorship = email_input

	initial_censor = censor_open_words(before_censorship)
	# print(initial_censor)

	second_censor = censor_paragraph_words(initial_censor)
	# print(second_censor)






# print(censor_single_phrase(email_one))
censor_multiple_phrases(email_two)
