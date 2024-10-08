import json
import requests


def additional_info ():
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzI1OGE1ZjItZDU3Zi00OWJkLWIzYzUtMDNjYmE3NTI5MDRiIiwidHlwZSI6ImFwaV90b2tlbiJ9.IfIMw8HQV3BgBe3HPfiyWLCzjpZzcksVI9iYcvlz2Gc"}

        url = "https://api.edenai.run/v2/text/chat"
        with open("output.txt", "r") as file:
            corrected_text = file.read()

        payload = {
            "providers": "openai",
            "text": corrected_text,
            "chatbot_global_action": "You are given a text transcript from a college/ high school/ grade school lesson course."
                                     "Based on the information provided in the text you need to provide additional useful/ relevant information."
                                     "Whatever you output, format it as markdown",

            "previous_history": [],
            "temperature": 0.0,
            "max_tokens": 3000,
            "fallback_providers": ""
        }

        response = requests.post(url, json=payload, headers=headers)

        result = json.loads(response.text)

        with open("outputboss.txt", "w") as output_file:
            output_file.write(result['openai']['generated_text'])

def fun_fact ():
        headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzI1OGE1ZjItZDU3Zi00OWJkLWIzYzUtMDNjYmE3NTI5MDRiIiwidHlwZSI6ImFwaV90b2tlbiJ9.IfIMw8HQV3BgBe3HPfiyWLCzjpZzcksVI9iYcvlz2Gc"}

        url = "https://api.edenai.run/v2/text/chat"
        with open("output.txt", "r") as file:
            corrected_text = file.read()

        payload = {
            "providers": "openai",
            "text": corrected_text,
            "chatbot_global_action": "You are given a text transcript from a college/ high school/ grade school lesson course."
                                     "Based on the information provided you need to give fun facts about the topic discussed in the text."
                                     "The fun facts must be written in a witty/ freaky nature, as to be easily differentiated from the more serious source material"
                                     "Whatever you output, format it as markdown",
            "previous_history": [],
            "temperature": 0.0,
            "max_tokens": 3000,
            "fallback_providers": ""
        }

        response = requests.post(url, json=payload, headers=headers)

        result = json.loads(response.text)

        with open("outputboss.txt", "w") as output_file:
            output_file.write(result['openai']['generated_text'])

def summarize():
        headers = {
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzI1OGE1ZjItZDU3Zi00OWJkLWIzYzUtMDNjYmE3NTI5MDRiIiwidHlwZSI6ImFwaV90b2tlbiJ9.IfIMw8HQV3BgBe3HPfiyWLCzjpZzcksVI9iYcvlz2Gc"}

        url = "https://api.edenai.run/v2/text/chat"
        with open("output.txt", "r") as file:
            corrected_text = file.read()

        payload = {
            "providers": "openai",
            "text": corrected_text,
            "chatbot_global_action": "You are given a text transcript from a college/ high school/ grade school lesson course."
                                     "Based on the information provided in the text you need to summarize it in such a way that the essential information is preserved."
                                     "Whatever you output, format it as markdown",
            "previous_history": [],
            "temperature": 0.0,
            "max_tokens": 3000,
            "fallback_providers": ""
        }

        response = requests.post(url, json=payload, headers=headers)

        result = json.loads(response.text)

        with open("outputboss.txt", "w") as output_file:
            output_file.write(result['openai']['generated_text'])


def word_pool():
    headers = {
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzI1OGE1ZjItZDU3Zi00OWJkLWIzYzUtMDNjYmE3NTI5MDRiIiwidHlwZSI6ImFwaV90b2tlbiJ9.IfIMw8HQV3BgBe3HPfiyWLCzjpZzcksVI9iYcvlz2Gc"}

    url = "https://api.edenai.run/v2/text/chat"
    with open("output.txt", "r") as file:
        corrected_text = file.read()

    payload = {
        "providers": "openai",
        "text": corrected_text,
        "chatbot_global_action": "You are given a pool of words that belong to a subject from transcript of a college/ high school/ grade school lesson course."
                                 "Based on the pool of words, generate a lesson that incorporates all the words and tackles the specific field, of which the words belong"
                                 "Whatever you output, format it as markdown",
        "previous_history": [],
        "temperature": 0.0,
        "max_tokens": 3000,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)

    result = json.loads(response.text)

    with open("outputboss.txt", "w") as output_file:
        output_file.write(result['openai']['generated_text'])


additional_info()