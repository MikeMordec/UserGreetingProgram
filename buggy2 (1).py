'''
CSC 157
Discussion 2:
Program 2
'''

def main():
    userName = input("Please enter your name: ")
    print("Hello", userName + ", how are you?")
    ageString = input("Please enter your age: ")
    age = int(ageString)
    twiceTheAge=age*2
    print("Here is your age doubled:", twiceTheAge)
main()
