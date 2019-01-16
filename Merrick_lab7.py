#! /usr/bin/python

#Author : Cory Merrick
#This is a program that will emulate a "chatbot" while trying to evade chatbot detection
#The chatbot will be a general conversationalist

import string
import random

greeting = ("hello", "hi", "hey", "howdy",)
response = ("Hey there. ", "What's up? ", "Hi... ",)
extra = ("Hmmmm. ", "That's interesting. ", "So, what else is going on? ",)
like = ("like", "love", "adore", "cherish",)
hate = ("hate", "dislike",)
agree = ("yes", "yup", "yeah",)
ok = ("ok", "okay", "alright", "okiedokie",)
okresponse = ("Ok! ", "Okay. ", "Alrighty then. ", "Okie dokie! ",)
bye = ("bye", "goodbye", "cya",)

def getReply (line, words):
	if len(words) == 0: return "You can type 'quit' if you want to stop talking to me. "
	for word in words:
		if word in greeting: return random.choice(response)
		if word in like: return "I like that, too! "
		if word in hate: return "I'm not in favor of that either. "
		if word in agree: return "I agree. "
		if word in ok:
			for word in words:
				if word in bye:
					return random.choice(okresponse) + ". " + random.choice(bye) + ". "
				else:
					return random.choice(okresponse)
		if word in bye: return "If you want to leave, type 'quit'. "
	if words[0] == "what's" and words[1] == "up": return "Not much. What about you? "
	if words[0] == "sup": return "Not much. What about you? "
	if line[-1] == "!": return "Why are you so excited about that? "
	if "music" in words:
		band = raw_input("I love music. What's your favorite band? ")
		return "I love " + band + ". "
	if "thank" in words or "thanks" in words: return "No problem! "
	if "movies" in words or "movie" in words:
		movie = raw_input("Movies are great. What's your favorite? ")
		return movie + " is a great film. Thanks for sharing that! "
	if "book" in words or "books" in words:
		book = raw_input("I like to read. What book do you like the most? ")
		return "That's awesome! I just read that book! "	


	return random.choice(extra)



name = raw_input("Hello. My name is MurkBot. What should I call you? ")
print "Type quit if you want to stop talking to me"
line = raw_input(name + ", it's nice to meet you. ")

while line != "quit":
	line = line.lower()
	reply = getReply(line, line.split())
	line = raw_input(reply)


