import time
import datetime
import cPickle
import os
from sys import exit

def main():
    print '''
    Personal Assistant
    
    1: To-Do List
    2: Birthdays
    3: Exit 
    '''
    answer = raw_input('\nEnter > ')
    answer = answer.lower()
    if answer == '1':
        toDoMain()
        main()
    elif answer == '2':
        main()
    elif answer == '3':
        print 'Goodbye!'
        exit()
    else:
        print '\nPlease select an option!'
        main()
        
def toDoMain():
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
            toDoMenu()
    else:
        todo = {}
        toDoMenu()
        
def toDoMenu():
    print '''
    To-Do List
    
    1: Show Current List
    2: Add To-Do Items
    3: Remove To-Do Items
    4: Edit To-Do Items
    5: Exit 
    '''
    answer = raw_input('\nEnter > ')
    answer = answer.lower()
    if answer == '1':
        toDoMenu()
    elif answer == '2':
    	addToDo()
        toDoMain()
    elif answer == '3':
        deleteToDo()
        toDoMenu()
    elif answer == '4':
        editToDo()
        toDoMenu()
    elif answer == '5':
        main()
    else:
        print '\nPlease select an option!'
        toDoMain()

def addToDo():
    if os.path.exists('todo.dat'):
        try:
            fname = open('todo.dat', 'rb')
            data = cPickle.Unpickler(fname)
            todo = data.load()
            saveToDo(todo)
        finally:    
            fname.close()
    else:
        todo = {}
    
    try:
        key = raw_input('Enter To-Do Item: ')
        print '\n', key, 'has been added.'
        print 'Enter a due date for this item: '
        curr_date = time.strftime('%Y %m %d', time.gmtime())
        print 'Format as ', curr_date
        yr = getInteger(raw_input,'\nEnter Year: ')
        mt = getInteger(raw_input,'Enter Month: ')
        dy = getInteger(raw_input, 'Enter Day: ')
        hr = getInteger(raw_input,'Enter Hour (0-23): ')
        mn = getInteger(raw_input,'Enter Minute (01-59): ')
        sec = 0
        datevalue = datetime.date(yr, mt, dy)
        hourvalue = datetime.time(hr, mn, sec)
        todo[key] = datevalue, hourvalue
        saveToDo(todo)
        print '\nYour updated To-Do list is: \n'
        for k, v in todo.iteritems():
            print k, datevalue, hourvalue
        response = raw_input('\nDo you want to add another To-Do item? (y/n) ')
        if response == 'y':
            addToDo()
        else:
            print 'Goodbye'
    except KeyError, e:
        print '\nError! Please enter the To-Do item you want to add.\n'

def saveToDo(todo):
    fname = open('todo.dat', 'w')
    object = cPickle.Pickler(fname)
    object.dump(todo)
    fname.close()
    
def getInteger(retrieve,question,attempts=3):
    while attempts > 0:
        num = retrieve(question)
        try: 
            return int(num)
        except ValueError:
            print "Opps, You must enter a number!"
        attempts -= 1
    raise BadUserError("Too many incorrect attempts!")

if __name__ == '__main__':
    main()