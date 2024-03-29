#!/usr/bin/env python2
# -*- coding: utf-8 -*- #

from twitterbot import TwitterBot
import keys
import StringIO
from effects import mirror, saturation
#from saturation import saturation
from PIL import Image
from image import get_image_file
from sys import argv

class PicBot(TwitterBot):
	"""
	Whenever you tweet a sentence at this bot, it will tweet back at you with an image
	containing the sentence, with some words replaced by images
	"""
	def bot_init(self):
		""" Initialize and configure the bot """

		############################
		# REQUIRED: LOGIN DETAILS! #
		############################
		self.config['api_key'] = keys.consumer_key	
		self.config['api_secret'] = keys.consumer_secret
		self.config['access_key'] = keys.access_token
		self.config['access_secret'] = keys.access_token_secret


		######################################
		# SEMI-OPTIONAL: OTHER CONFIG STUFF! #
		######################################
		

		# how often to tweet, in seconds
		self.config['tweet_interval'] = 1 * 5     # default: 1 minutes

		# use this to define a (min, max) random range of how often to tweet
		# e.g., self.config['tweet_interval_range'] = (5*60, 10*60) # tweets every 5-10 minutes
		self.config['tweet_interval_range'] = None

		# only reply to tweets that specifically mention the bot
		self.config['reply_direct_mention_only'] = True

		# only include bot followers (and original tweeter) in @-replies
		self.config['reply_followers_only'] = False

		# fav any tweets that mention this bot?
		self.config['autofav_mentions'] = False

		# fav any tweets containing these keywords?
		self.config['autofav_keywords'] = []

		# follow back all followers?
		self.config['autofollow'] = False
		
		self.state['last_mention_id'] = 'last_tweer_id'
		
		
                
        

	def on_scheduled_tweet(self):
		""" Make a public tweet to the bot's own timeline. """
		# We might take senteces from somewhere and tweet them on a regular basis ...
		pass # don't do anything here ...


	def on_mention(self, tweet, prefix):
		""" Actions to take when a mention is received. """
		
		print("---")
		print("- Mention received: " + tweet.text)

		# get image from the tweet

		try:
			
			image_file = get_image_file(tweet)

			if image_file is None:
				text = "{} Hey there! If you want to get mesmerized you need to attach an image.".format(prefix)
			else:
				# create a tweet and make sure to cut it off at 140 chars
				text = "{} I am done kaleidofying your image. I hope you like it.".format(prefix)
	
		except Exception as e:
			print(e)
			pass


		# do the tweeting based on wether we have an image
		

		tweetsize = 140 - len(prefix) - 1
		text = text[:140]
	


		if image_file is None:

			# post a default reply
			print("---")
			print("- No Image received")
			self.post_tweet(text, reply_to=tweet)
			return


		else:

			# image processing
			filename, file = image_file
			img = Image.open(file)
			img.save('img.png')
            
			# Applying the effects
			print("---")
			print("- Mirroring and sharpening the image")
			img = mirror(img)
			img = saturation (img)



		try:
			# post the tweet
			print("---")
			print("- Replying to user")
			print("---")
			self.post_tweet(text, reply_to=tweet, media='img.png')
			print("---")
			print("- Waiting for new mentions")
			print("---")


		except Exception as e:
			# did anything go wrong when we tried to create and post the tweet?
			print(e)
			

	def on_timeline(self, tweet, prefix):
		""" Actions to take on a timeline tweet. """
		pass # Don't do anything here ...

if __name__ == '__main__':

	bot = PicBot()
	
	if len(argv) == 1:

		# running the bot
		print("---")
		print("Running the bot")
		print("---")
		bot.run()

	else:
		# testing the on_mention function of our bot
		print("Testing the bot")
		api = bot.api
		tweet = api.get_status("608998028943478785")
		prefix = bot.get_mention_prefix(tweet)
		bot.on_mention(tweet, prefix)





