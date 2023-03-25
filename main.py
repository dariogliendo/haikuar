from config import create_client
import os
import openai
import random
import schedule
client = create_client()

openai.api_key = os.getenv("OPEN_AI_KEY")
PROMPTS = [
    "un haiku en lenguaje argentino como si fuera una letra del indio solari",
    "escribe un haiku como si fueras un argentino",
    "escribe un tweet bien argentino, no uses hashtags",
    "un poema argentino en menos de 200 caracteres"
]

def on_schedule():
    print('algo')


def prompt_gpt():
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=random.choice(PROMPTS),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return str(response.choices[0].text)

def tweet():
    haiku=prompt_gpt()
    client.create_tweet(text=haiku)
    print('tweet \n\n' + haiku + '\n\n realizado')

schedule.every(12).hours.do(tweet)

while True:
    schedule.run_pending()

