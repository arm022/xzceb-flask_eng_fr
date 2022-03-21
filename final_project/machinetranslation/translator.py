import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION_LT='2018-05-01'

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=VERSION_LT, authenticator=authenticator)
language_translator.set_service_url(url)
language_translator

def englishToFrench(englishText):
    #write the code here
    """ dummy docstring """
    if englishText!="":
        frenchText=language_translator.translate(text=englishText , model_id='en-fr').get_result()
        return frenchText.get['translations'][0].get['translation']
    else:
        return str('Test input cannot be null')

def frenchToEnglish(frenchText):
    #write the code here
    """ dummy docstring """
    if frenchText!="":
        englishText=language_translator.translate(text=frenchText , model_id='fr-en').get_result()
        return englishText.get['translations'][0].get['translation']
    else :
        return str('Test input cannot be null')
        