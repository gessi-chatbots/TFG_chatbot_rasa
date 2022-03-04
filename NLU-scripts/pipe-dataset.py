from termcolor import colored
import sys

args = sys.argv[1:]

if '-h' in args or '--help' in args:
    print(colored('positional arguments', attrs=["bold"]))
    print('replace <path>              Replace data foun ')
    print('add <path>                  Add data to existing set ')
    print('path for add/replace should lead to the data folder in your rasa chatbot')
    print()
    print(colored('optional arguments', attrs=["bold"]))
    print('-n <path>            replace/add NLU data found in specified set ')
    print('-r <path>            replace/add rules to specified path.')
    print('-s <path>            replace/add stories to specified path.')
    sys.exit()

if args[0].strip() != 'replace' and args[0].strip() != 'add':
    raise Exception("ERROR: wrong positional argument specified" + args[1])

#copy folder?
data = args[0].strip() == 'replace'
path = args[1]
for i in range(2, len(args)):
    if i%2 == 1: continue
    x = args[i]
    y = args[i+1]
    file = ""
    if x.strip() == '-n': file = '/nlu.yml'
    elif x.strip() == '-r': file = '/rules.yml'
    elif x.strip() == '-s': file = '/stories.yml'
    else: raise Exception("ERROR: wrong optional argument specified")
    
    lines = open(y).readlines()
    type = 'w' if data else 'a'
        
    with open(path + file, type) as f:
        for l in lines: f.write(l)
        f.close()