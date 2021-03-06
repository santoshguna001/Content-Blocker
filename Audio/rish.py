# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 12:52:30 2018

@author: Santosh
"""

#import argparse
import io
from load_words import bad_words_list_final1
from google.oauth2 import service_account
from begin import samplerate
aList = ['words', 0.0, 0.0]
credentials = service_account.Credentials.from_service_account_file('api-key.json')
start_time_indices=[]
end_time_indices=[]

# [START def_transcribe_gcs]
def transcribe_gcs_with_word_time_offsets(gcs_uri):
    """Transcribe the given audio file asynchronously and output the word time
    offsets."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US',
        enable_word_time_offsets=True)

    operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    result = operation.result(timeout=90)

    for result in result.results:
        alternative = result.alternatives[0]
        print('Transcript: {}'.format(alternative.transcript))
        print('Confidence: {}'.format(alternative.confidence))

        for word_info in alternative.words:
            word = word_info.word
            print(word)
            start_time = word_info.start_time
            end_time = word_info.end_time
            if word in bad_words_list_final1:
                aList.append(word)
                aList.append(start_time)
                aList.append(end_time)
            print('Word: {}, start_time: {}, end_time: {}'.format(
                word,
                start_time.seconds + start_time.nanos * 1e-9,
                end_time.seconds + end_time.nanos * 1e-9))
# [END def_transcribe_gcs]

def transcribe_file_with_word_time_offsets(speech_file):
    """Transcribe the given audio file synchronously and output the word time
    offsets."""
    print("Start")
    
    from google.cloud import speech
    #from google.cloud.speech import enums
    from google.cloud.speech import types  
    
    print("checking credentials")
      
    client = speech.SpeechClient(credentials=credentials)
    
    print("Checked")
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()
              
    print("audio file read")    
    
    audio = types.RecognitionAudio(content=content)
    
    print("config start")
    config=speech.types.RecognitionConfig(
         encoding='LINEAR16',
         language_code='en-US',
         profanity_filter=False,
         enable_word_time_offsets=True,
         sample_rate_hertz=samplerate,
     )
    #config1=types.RecognitionConfig(
            #encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            #language_code='en-US',
            #enable_word_time_offsets=True,
            #profanityFilter=False)
    print("Recognizing:")
    response = client.recognize(config, audio) 
    print("Recognized")

    for result in response.results:
        alternative = result.alternatives[0]
        print('Transcript: {}'.format(alternative.transcript))

        for word_info in alternative.words:
            word = word_info.word
            start_time = word_info.start_time
            end_time = word_info.end_time
            #print(word)
            if word in bad_words_list_final1:                             
                start_time_indices.append(start_time.seconds + start_time.nanos * 1e-9)
                end_time_indices.append(end_time.seconds + end_time.nanos * 1e-9)
            print('Word: {}, start_time: {}, end_time: {}'.format(
                    word,
                    start_time.seconds + start_time.nanos * 1e-9,
                    end_time.seconds + end_time.nanos * 1e-9))

            
import os
audio=os.fspath(r'stereo_file.wav')
transcribe_file_with_word_time_offsets(audio)