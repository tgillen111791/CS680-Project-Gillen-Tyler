import time
import datetime
import os
from sys import exit

def main():
    print '\nYour current Todo list is: \n'
    if os.path.exists('todo.dat'):
        try:
            fname = open('todo.dat', 'rb')
            data = cPickle.Unpickler(fname)
            todo = data.load()
            save_todo(todo)
            for k, v in todo.iteritems():
                print k, v[0], v[1]
        finally:    
            fname.close()
            menu()
    else:
        todo = {}
        menu()

def menu():
    print '''
    Todo List
    
    Enter I: Show Current List
    Enter A: Add Todo
    Enter D: Remove Todo
    Enter E: Edit Todo
    Enter X: Exit 
    '''
    answer = raw_input('\nEnter > ')
    answer = answer.lower()
    if answer == 'a':
        add_todo()
        main()
    elif answer == 'i':
        main()
    elif answer == 'd':
        del_todo()
        main()
    elif answer == 'e':
        edit_todo()
        main()
    elif answer == 'x':
        print 'Goodbye'
        exit()
    else:
        print '\nPlease enter an option!'
        main()

if __name__ == '__main__':
    main()