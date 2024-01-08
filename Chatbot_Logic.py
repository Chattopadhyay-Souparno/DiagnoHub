# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 16:02:33 2023

@author: User
"""


import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings("ignore")
#from summarizer import Summarizer
#import spacy


import requests
from bs4 import BeautifulSoup

def use_api(query):
  api_key = "AIzaSyCGrZ25CGJni7Vr8zzxGHqZW7KCEzUFchg"
  url = "https://www.googleapis.com/customsearch/v1"
  params = {
      "key": api_key,
      "cx": "c42dd0d386d8f4934",
      "q": query
  }
  response = requests.get(url, params=params)
  if response.status_code == 200:
      data = response.json()
  else:
      print("Error: Unable to fetch data from Google API")
  return data
def get_text(link):
  response = requests.get(link)
  input_text = []

  if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')

      subheading1 = soup.find('h2', string="Management and Treatment")
      subheading2 = soup.find('h2', string="Care and Treatment")

      if subheading1:
        subheading = subheading1
      elif subheading2:
        subheading = subheading2
      if subheading:
          next_sibling = subheading.find_next_sibling()
          for i in next_sibling:

            if i.name=='ul' or i.name=='ol':
                points = ''
                list_items = i.find_all('li')
                for j in list_items:

                  points += j.get_text() + ' '

                input_text.append(points)

            elif i.name=='p':

              input_text.append(i.get_text())

            # print()


      else:
          print(f"Subheading '{target_subheading}' not found on the page.")
  else:
      print(f"Failed to retrieve data. Status code: {response.status_code}")

  return input_text


#def get_summary(input_text, min):

  #bert_model = "bert-base-uncased"
  #model = Summarizer(model=bert_model)

  #summary = model(input_text, min_length=min)
  #return summary


#def disease_identifier(text_query):
  #nlp = spacy.load("en_ner_bc5cdr_md")

  #sample_transcription = 'I am suffering from fever headache and hypertension'
  #doc = nlp(text_query)
  #disease_entities = [ent.text for ent in doc.ents if ent.label_ == 'DISEASE']
  #disease_string = ' '.join(disease_entities)
  # for i in disease_entities:
  #   disease_string += i
  #print(disease_string)

# Print identified diseases
  #return disease_string


def API_Response(user_input):
  query = user_input
  #disease_list = disease_identifier(query)
  #print(disease_list)


  data = use_api(query)
  for i in range(10):
    link = data['items'][i]['link']
    if 'my.clevelandclinic.org' in link:

        break

  #summary_final = ''
  try:
    input_data = get_text(link)
    
    input_data = ''.join(input_data)



    #for i in input_data:

      #summary_final += get_summary(i, 50) + ' '
    Final_Answer = 'The suggestion is:\n' + input_data

    return Final_Answer
  except Exception as e:
    return 'I am Sorry I cannot answer that'

  # return summary_final


#API_Response()


def get_user_input():
    return input("Enter your message: ")


def get_chatbot_response(user_message):
   
    # Basic chatbot logic with conditional responses
    if "hello" in user_message.lower() or "hey" in user_message.lower() or "what's up" in user_message.lower() or "hi" in user_message.lower():
        return "Hello! How can I help you?"
    elif "how are you" in user_message.lower():
        return "I'm just a computer program, but thanks for asking!"
    elif "bye" in user_message.lower():
        return "Goodbye! Have a great day!"
    else:
        return API_Response(user_message.lower())
        

#user_message = get_user_input()
       
#get_chatbot_response(user_message)
