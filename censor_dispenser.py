single_string_sample_text = "bada bee da be da bo bo be ba be de doe learning algorithms cha cha cha HOY."
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_single_phrase(email_input) :
	#defining word to be censored
	censored_phrase = "learning algorithms"
	if censored_phrase in email_input :
		new_input = email_input.replace(censored_phrase, "[Redacted]")
	return new_input

def censor_multiple_phrases(email_input) :
	#splitting the email input into seperate words, and checking to see if words were split properly
	split_email_input = email_input.split(' ')
	# print(split_email_input)
	new_input = []
	#checking each word in split email to see if it should be censored
	for word in split_email_input :
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
	# split_email_input = joined_email_input.split("\n\n")
	# print(split_email_input)


# print(censor_single_phrase(email_one))
print(censor_multiple_phrases(email_two))
