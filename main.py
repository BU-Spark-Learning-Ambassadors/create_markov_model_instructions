### Create a Markov Model

import random
import re

def create_markov_model(text, n=1):
    '''
    Creates a Markov model from the input text
    
    Args:
    - text (str): Input text
    - n (int): Size of n-grams (default is 1 for unigrams)
    
    Returns:
    - dict: Markov model dictionary
    '''
    

def generate_markov_text(model, num_words, n=1):
    '''
    Generates text using the Markov model
    
    Args:
    - model (dict): Markov model dictionary
    - num_words (int): Number of words to generate
    - n (int): Size of n-grams (default is 1 for unigrams)
    
    Returns:
    - str: Generated text
    '''
    

def create_bi_directional_markov_model(text, n=1):
    '''
    Creates a bi-directional Markov model from the input text
    
    Args:
    - text (str): Input text
    - n (int): Size of n-grams (default is 1 for unigrams)
    
    Returns:
    - tuple: Tuple containing forward and backward Markov models
    '''

def generate_sentence(model, max_words, n=1):
    '''
    Generates a sentence using the Markov model
    
    Args:
    - model (dict): Markov model dictionary
    - max_words (int): Maximum number of words to generate for a sentence
    - n (int): Size of n-grams (default is 1 for unigrams)
    
    Returns:
    - str: Generated sentence
    '''
    
