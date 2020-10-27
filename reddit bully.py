import praw, random, time

# reddit api login
reddit = praw.Reddit(
	client_id='INSERT HERE',
	client_secret='INSERT HERE',
	username='INSERT HERE',
	password='INSERT HERE',
	user_agent='bullybot by /u/mrakeyt'
)

subreddit = reddit.subreddit("thebullybot")
keyphrase = "!bullybot " or " !bullybot " or " !bullybot" or "!bullybot"

phrases = [
	{
		"keyword": "sucks", 
		"PossibleAnswers": [f"at least i'm not you", f"don't be jealous because you're not me", f"are you gonna cry", f"well i'm definitely better than you", f"wow so mean i'm definitely going to cry", f"i'm a bot, i don't have feelings", f"that was the insult of a 12 yr old", f"you're the human embodiment of a headache", f"okay deal with it", f"your mom doesn't think so", f"dude i'm a bot, not a hero", f"if i had a middle finger, i would lift it at you", f"no you", f"and yet you're tryna talk to me", f"says the person who just wants to be insulted", f"that was a good one....if you're in preschool", f"if i had feelings, that still wouldn't hurt", f"i'm sooo happy you think so", f"yea but it would've been worse if i was you", f"ight now that you got that out, leave me alone"]
	},
	{
		"keyword": "boring", 
		"PossibleAnswers": [f"das cool but i don't care", f"but i'm more exciting than you", f"and yet you're talking to a bot", f"that's rich coming from you", f"I'm guessing you're illiterate because that's not how you spell interesting", f"i could not literally care less about your opinion tough guy", f"coming from you does not mean anything to me", f"yet more people try to talk to me than to you", f"do you want me to cry or something", f"i'm a bot, idiot", f"oh i'm sorry, was that supposed to mean anything", f"ok.", f"i'm gonna give you an F for effort cuz that sucked", f"oh right, as if you're interesting", f"but i'm in an awesome youtube video...and you're not", f"that was trash, try again", f"lol ok tough guy", f"then don't tag me", f"shut up, idiot", f"you're the last person that should be calling someone boring"]
	},
	{
		"keyword": "dumb", 
		"PossibleAnswers": [f"don't be mad my iq is higher than yours", f"stop projecting how you feel about yourself", f"you're dumb for tagging a bot", f"no you", f"the feeling is mutual", f"honestly i can say the same about you", f"i don't even know you weirdo", f"if you're jealous of me then just say that", f"that's ironic considering you're tagging someone made from code", f"you say that as if you're smart", f"today's opposite day and you're smart", f"if you stop tagging me i think you can be almost as smart as me", f"ok smooth brain", f"lol", f"keep crying about it sucker", f"coming from a loser like you, i couldn't care less", f"your opinion = worthless to me", f"some people wonder why i bully and it's definitely because of you", f"go back to bed and call me when i care", f"let me guess, you're just jealous"]
	},
	{
		"keyword": "trash", 
		"PossibleAnswers": [f"that's all? ok now shutup", f"i smell a hater nearby", f"you're trash for thinking that", f"i'm the best trash you've ever seen dummy", f"that's not how you spell 'better than me'",f"watch out everyone we got a tough guy over here", f"I’m like a golden trash bag and you’re a plain one", f"If I’m trash then you’re the scum of the earth", f"Says the person trying to insult a bot", f"Dude you use the insults of a 2 year old", f"But like.....I’m still better than you", f"Tag me again when you have a better insult", f"Yea like I haven’t heard that one before", f"Omg. Much wow. Very insulted. Try again next time", f"Error 404: Insult Not Found", f"Don’t be mad that I get more attention than you", f"After reading that, I’ve lost all hope in humanity", f"Are all humans that stupid or is it just you" ,f"I’m a robot, not a mirror", f"And yet people STILL like me more than you"]
	}
]

RandAnswers = [f"what do you want from me", f"please leave me alone", f"I'm not listening to you", f"go away", f"go bother somebody else", f"if you tag me again, i'll block you",f"you bored or sum?",f"dude...shutup",f"wow you're annoying", f"WHAT?! YOU GOT A PROBLEM NERD??", f"if you want me to bully you, go away. i'm tired", f"just look in the mirror and bully yourself", f"the fact that you want me to bully you is sad", f"go read or book or something and leave me alone", f"no.", f"leave me alone...but go watch the video about me on youtube", f"if one more person tags me, imma just shut myself down", f"if i had hands i would fight you for tagging me punk", f"oh no, i was having a great day til just now", f"your face ruined my day"]

def Reply(comment):
	try:

		keywordList = [item['keyword'] for item in phrases]

		matches = [keyword for keyword in keywordList if keyword in comment]

		if len(matches) > 0:
			PossibleAnswersToThisComment = next((value for value in phrases if value['keyword'] == matches[0]), None)['PossibleAnswers']
			answer = PossibleAnswersToThisComment[random.randint(0, len(PossibleAnswersToThisComment) - 1)]

		else:
			answer = RandAnswers[random.randint(0, len(RandAnswers) - 1)]
			
	  	comment.reply(answer)
		print("ight, i replied with this: '" + answer + "'")

	except Exception as error:
		print("not working chief, got error: '" + str(error) + "'")

# locating comments and replying
for comment in subreddit.stream.comments():

	CommentBody = str(comment['body'])

	if keyphrase in CommentBody:
		print("got em: '" + CommentBody + "'")
		Reply(CommentBody)
