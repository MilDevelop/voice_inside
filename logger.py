from termcolor import colored

def debug(msg, comment=""):
    print(colored('DEBUG', 'green'), colored(comment, 'green'), msg)

def error(msg, comment=""):
    print(colored('ERROR', 'red'), colored(comment, 'red'), msg)

def worning(msg, comment=""):
    print(colored('WORNING', 'yellow'), colored(comment, 'yellow'), msg)
