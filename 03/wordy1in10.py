#
# wordy1in10.py
#
import inflect

def convert_to_wordy(number):
    p = inflect.engine()
    return p.number_to_words(number)

def main():
    for i in range(101):
        if i % 10 == 0 and i > 0:
            print(convert_to_wordy(i))
        else:
            print(i)

if __name__ == "__main__":
    main()
