from config import create_client
import os
import openai
import random
import schedule
import traceback
client = create_client()

openai.api_key = os.getenv("OPEN_AI_KEY")
PROMPTS = [
    "un haiku en lenguaje argentino como si fuera una letra del indio solari",
    "escribe un haiku como si fueras un argentino",
    "hacé un haiku en estilo y lenguaje argentino",
    "un poema argentino en menos de 200 caracteres"
]

def on_schedule():
    print('algo')


def prompt_gpt():
    try:
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
    except:
        print("Algo salió mal con OpenAI")
        return(False)

def tweet():
    try:
        haiku=prompt_gpt()
        if haiku == False:
            return
        client.create_tweet(text=haiku)
        print('tweet \n\n' + haiku + '\n\n realizado')
    except Exception:
        print('Algo salió mal con twitter')
        traceback.print_exc()

tweet()
schedule.every(12).hours.do(tweet)

while True:
    schedule.run_pending()
