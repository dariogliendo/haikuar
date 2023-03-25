import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
    

    auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
    api = tweepy.API(auth)
    try:
      api.verify_credentials()
    except Exception as e:
      logger.error("Error creating API", exc_info=True)
      raise e
    logger.info("API Created")
    return api

def create_client():
  consumer_key = os.getenv("CONSUMER_KEY")
  consumer_secret = os.getenv("CONSUMER_SECRET")
  access_token = os.getenv("ACCESS_TOKEN")
  access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")
  bearer_token = os.getenv("BEARER_TOKEN")

  try:
    client = tweepy.Client(bearer_token, consumer_key, consumer_secret, access_token, access_token_secret)
    return client
  except Exception as e:
    print(e)
    raise e

       
    