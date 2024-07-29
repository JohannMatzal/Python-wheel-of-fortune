import matplotlib.pyplot as pl
filepath = './phrases.txt'
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def get_letters():
    """Returns a list of only letters, removing all punctuation, spaces, etc."""
    try:
        with open(filepath, 'r') as doc:
            lines = doc.read()
        letter_list = [n.upper() for n in lines if n.upper() in letters]
        return letter_list

    except FileNotFoundError:
        print(f'Error: The file {filepath} was not found.')


def main():
    letter_list = get_letters()
    total_letters = len(letter_list)
    x = list(letters)
    y = [letter_list.count(letter)/total_letters for letter in x] # counts the number of times each letter appears in the letter list, and then divides it by the total number of letters

    fig, ax = plt.subplots()
    ax.bar(x, y, color = 'darkcyan', edgecolor = 'black')
    ax.grid(True, which = 'both', linestyle = '--')
    ax.set_title('Letter Frequency in phrases.txt', fontweight = 'bold')
    ax.set_xlabel('Letter')
    ax.set_ylabel('Letter Appearance Frequency')
    plt.show()


if __name__ == '__main__':
    main()
