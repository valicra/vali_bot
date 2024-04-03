# in this file we handle normal text anwers 

from datetime import datetime

def sample_answers(input_text) -> str:

    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi','what\'s up'):
        return 'Hi! What can I do for you?'
    
    if user_message in ('who are you', 'who are you ?'):
        return 'I\'m Vali\'s bot, his assistant.'

    if user_message in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime('%d/%m/%y, %H:%M:%S')
        return str(date_time)

    if user_message in ('bye', 'thank you'):
        return 'ok.'


    
    return 'Sorry, I don\'t understand you.'

