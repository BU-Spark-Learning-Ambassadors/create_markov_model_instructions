### Create a Markov Model
## this file provides more detailed hints as to how to code each function

import random
import re



def create_markov_model(text, n=1):
    '''
    Creates a Markov model
    
    Args:
    - text (str): Input text
    - n (int): Size of n-grams
    
    Returns:
    - dict: Markov model
    '''
    # Tokenize words
    # Initialize dictionary
    # Initialize n-gram
    # Iterate through words
        # Check if n-gram is in the dictionary
            # Add it with the next word if not
            # Append the next word if yes
            # Update n-gram by shifting and adding the next word
    
    # Return the Markov model

def generate_markov_text(model, num_words, n=1):
    '''
    Generates text using the Markov model
    
    Args:
    - model (dict): Markov model
    - num_words (int): Number of words to generate
    - n (int): Size of n-grams
    
    Returns:
    - str: Generated text
    '''
    # Initialize string
    # Choose random starting n-gram
    # Iterate to generate words
        # Check if n-gram is in the model
            # Choose the next word randomly
        # If not, choose a new random starting n-gram
        # Append the next word
        # Update n-gram by shifting and adding the next word
    
    # Return the generated text

def create_bi_directional_markov_model(text, n=1):
    '''
    Creates a bi-directional Markov model
    
    Args:
    - text (str): Input text
    - n (int): Size of n-grams
    
    Returns:
    - tuple: Forward and backward Markov models
    '''
    # Tokenize words
    # Initialize dictionaries for forward and backward models
    # Initialize n-grams for both models
    # Iterate through words
        # Update the forward model
        # Update the backward model
        # Update n-grams for both models
    
    # Return the tuple containing forward and backward Markov models

def generate_sentence(model, max_words, n=1):
    '''
    Generates a sentence using the Markov model
    
    Args:
    - model (dict): Markov model
    - max_words (int): Maximum number of words for a sentence
    - n (int): Size of n-grams
    
    Returns:
    - str: Generated sentence
    '''
    # Initialize string for the sentence
    # Choose random starting n-gram
    # Variable to track words generated
    # Iterate to generate the sentence
        # Check if n-gram is in the model
            # Choose the next word randomly
        # If not, choose a new random starting n-gram
        # Append the next word to the sentence
        # Update n-gram by shifting and adding the next word
        # Check if the next word ends with punctuation
            # If so, break out of the loop
    
    # Capitalize the first letter of the sentence
    # Remove trailing space and return the generated sentence
