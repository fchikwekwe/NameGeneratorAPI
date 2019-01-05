""" Series of functions that take in a text file, clean it, tokenize it and make
it into a markov chain. The output is made into a sentence based on the
conditions established below. The entire process can also be benchmarked for
improving algorithmic speed """

import json # to decode and encode JSON data from main app
import re # regex so that we can do text cleanup
import time # needed to record performance time
import datetime # needed to record timestamp when trials are done
import random
import sample # to get words for sentence
from dictogram import Dictogram

def copy_text(input_text, output_text):
    """ copies text from input file to corpus file """
    with open(input_text, 'r') as in_text, open(output_text, 'a') as out_text:
        out_text.write(in_text.read())

def make_source_text(input_one, input_two, input_three, output_text):
    """ Clear out the output file, copy text from the input files and return
    the file with new contents"""
    # clear out the previous file contents
    open(output_text, 'w').close()
    # copy from three input files based on question answers
    copy_text(input_one, output_text)
    copy_text(input_two, output_text)
    copy_text(input_three, output_text)
    return output_text

def cleanup(text):
    """ takes in a text file, opens it and cleans text using regex. outputs
    string of cleaned text """
    with open(text, 'r') as uncleaned_text:
        no_chapters = re.sub('[A-Z]{3,}', ' ', uncleaned_text.read())
        remove_periods = re.sub('(\s\.){4,}', '', no_chapters)
        new_text = re.sub('\*', '', remove_periods)
    return new_text

def tokenize(text):
    """ takes in cleaned text as string and makes it into a list of tokens """
    source = list(text.rstrip().replace('\n', ' '))
    return source

# takes in list of words
def first_order_markov(text_list):
    """ takes in a word and checks to see what words come after it
    to determine the word sequence for our generated markov chain"""
    markov_dict = dict()
    # for each word in list, key is word and value is dictogram
    for index in range(len(text_list) - 1):
        # text_list[index] should be our word from list
        word = text_list[index]
        # check if key is stored already
        if word in markov_dict:
            # if it is, then append it to the existing histogram
            markov_dict[word].add_count([text_list[index + 1]])
        else:
            # if not, create new entry with word as key and dictogram as value
            markov_dict[word] = Dictogram([text_list[index + 1]])
    # return dictionary
    return markov_dict

def nth_order_markov(order, text_list):
    """ this function takes in a word and checks to see what words come after it
    to determine the word sequence for our generated markov chain"""
    markov_dict = dict()
    # for each word in list, key is word and value is dictogram
    for index in range(len(text_list) - order):
        # text_list[index] should be our word from list
        window = tuple(text_list[index: index + order])
        # check if key is stored already
        if window in markov_dict:
            # if it is, then append it to the existing histogram
            markov_dict[window].add_count([text_list[index + order]])
        else:
            # if not, create new entry with window as key and dictogram as value
            markov_dict[window] = Dictogram([text_list[index + order]])
    # return dictionary
    return markov_dict

def start_tokens(dictionary):
    """ Get words that can start a sentence; this method is O(n) worst case
    because one must check every word in the corpus"""
    start_token_list = []
    for key in dictionary:
        if key[0].islower() is False and key[0].endswith('.') is False:
            start_token_list.append(key)
    token = random.choice(start_token_list)
    return token

def stop_token(dictionary):
    """ Get words that can end a sentence"""
    stop_tokens = []
    for key, value in dictionary.items():
        # the key number must be changed depending on order number
        if key[2].endswith('.') or key[2].endswith('?'):
            stop_tokens.append(key)
    return stop_tokens

def list_names(text):
    """ creates list of names that were in original list to check against
        so that the new name is not a duplicate of names in the list"""
    with open(text, 'r') as names:
        list_of_names = list(names)
        name_list = [name.strip() for name in list_of_names]
    return name_list

def create_name(start_token, dictionary):
    """ takes dictionary, start and end tokens and makes a sentence """
    # create sentence and add first word
    name = []
    # this is hard coded; must be changed to fit the order number; currently second
    (letter1, letter2) = start_token
    name.append(letter1)
    name.append(letter2)

    current_token = start_token
    # stop when current_token is a stop token
    while not current_token[1].isspace() and len(name) <= 15:
        for key, value in dictionary.items():
            if key == current_token:
                # sample from histogram of values
                cumulative = sample.cumulative_distribution(value)
                sample_letter = sample.sample(cumulative)
                # add new sample to name_list
                name.append(sample_letter)
                # assign second word of key and value to current token
                # this is hard coded; must be changed to fit the order number
                # I am unpacking the current token
                (current_token_one, current_token_two) = current_token
                current_token = (current_token_two, sample_letter)
                # get out of for loop and start process over
                break
    return name

def logger(start_time, file):
    """ Benchmarking to improve performance """
    with open(file, "a") as text:
        text.write("""

        Current date and time: {}
        Program ran in {} seconds.
        """.format(datetime.datetime.now(), time.process_time() - start_time))

    return 'hello'

def main(name_list, text_list):
    """ calling functions and defining variables """
    while True:
        dictionary = nth_order_markov(2, text_list)
        first_letter = start_tokens(dictionary)
        markov_list = create_name(first_letter, dictionary)
        # make word and remove whitespace
        first_name = "".join(markov_list).strip()
        # check if name is match for any name in list; if so, start over
        if first_name in name_list:
            print("not valid name", first_name)
            continue

        # return the valid name
        print(repr(first_name))
        return first_name


if __name__ == '__main__':
    # start_time = time.process_time()
    CORPUS = make_source_text('girl.txt', 'app_names.txt', 'modern.txt', 'corpus.txt')
    CLEAN_TEXT = cleanup(CORPUS)
    TEXT_LIST = tokenize(CLEAN_TEXT)
    NAME_LIST = list_names(CORPUS)
    main(NAME_LIST, TEXT_LIST)

    # logger(start_time, 'markov_logger.txt')
