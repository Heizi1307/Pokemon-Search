'''File Name: pokemon.py
   Author: Longxin Li
   Purpose: A program to read in Pokemon data from a file and organize it according to Pokemon type then
            repeatedly read in queries from the user and print out solutions to those queries.
   CS120'''
import os
def read_csv(filename, dict):
    file_info = open(filename)
    for line in file_info:
        if line[0] == '#':
            continue
        line = line.strip('\n').split(',')
        if line[2] not in dict:
            dict[line[2]] = {}
            dict[line[2]].update({line[1]: line[4:11]})
        else:
            dict[line[2]].update({line[1]: line[4:11]})
    return filename
    '''Access the csv file that user wants to access and stored data as an two-level dictionary.
    Parameters: filename is the name of the csv file that user enter, dict is an empty list.
    Returns: The filename that user input for this program.
    Pre-condition: filename is a string and dict is an empty dictionary.
    Post-condition: The return value is a string.'''

def command(filename):
    enter = input()
    enter = enter.lower()
    if enter == '':
        os._exit(0)
    if enter == 'total':
        index = 0
        return index
    if enter == 'hp':
        index = 1
        return index
    if enter == 'attack':
        index = 2
        return index
    if enter == 'defense':
        index = 3
        return index
    if enter == 'specialattack':
        index = 4
        return index
    if enter == 'specialdefense':
        index = 5
        return index
    if enter == 'speed':
        index = 6
        return index
    else:
        return command(filename)
    '''Go through the command and check it.
    Parameters: filename is the name of the csv file that user enter, dict is an empty list.
    Returns: an index or command(filename).
    Pre-condition: filename is a string and dict is an empty dictionary.
    Post-condition: The return value index is an int and command(filename) is a function.'''

def process(dict, index):
    total = []
    poke_name = []
    for key in dict:
        num = 0
        for value in dict[key].values():
            num += int(value[index])
        total.append(num/(len(dict[key])))
        poke_name.append(key+ ':')
    for i in range(len(total)):
        if total[i] == max(total):
            print(poke_name[i],total[i])
    '''Go through the dict with index, then print out the maximum average value for that query across all types
       with type name.
    Parameters: dict is a dictionary that stored all data for the csv file, index is a number that return by
                command(filename).
    Returns: the maximum average value for that query across all types with type name.
    Pre-condition: dict is an empty dictionary, index is an int.
    Post-condition: The return value is a string'''

def repeat(filename, dict):
    index = command(filename)
    process(dict, index)
    repeat(filename, dict)
    '''Repeat the function and itself.
    Parameters: dict is a dictionary that stored all data for the csv file, filename is the name of the csv
                file that user enter.
    Returns: None.
    Pre-condition: dict is an empty dictionary, filename is a string.
    Post-condition: None'''

def main():
    dict = {}
    filename = input()
    read_csv(filename, dict)
    index = command(filename)
    process(dict, index)
    repeat(filename, dict)

main()