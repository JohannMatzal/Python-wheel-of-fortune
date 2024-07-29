###############################################################################
# Author: Johann Matzal
# Date: 4/29/2021
# Description: This program calculates how often each letter of the alphabet
# appears in the phrases used for Wheel of Fortune.
###############################################################################
import matplotlib.pyplot as plt

def get_letters():
    with open('./phrases.txt') as doc:
        lines = doc.read()
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_list = []
    for n in list(lines):
        if n.upper() in letters:
            letter_list.append(n.upper())
    return letter_list #returns a list of only letters

def main():
    letter_list = get_letters()
    fig, ax = plt.subplots()
    x = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    y = []
    for n in x:
        frequency = letter_list.count(n)/len(letter_list) #counts the # of times each letter appears in the letter list, and then divides it by the total # of letters
        y.append(frequency)
    ax.bar(x, y)
    ax.grid()
    ax.set_title('Letter Frequency in Puzzle Phrases')
    ax.set_xlabel('Letter')
    ax.set_ylabel('Letter Appearance Frequency')
if __name__ == '__main__':
    main()
    plt.show()
