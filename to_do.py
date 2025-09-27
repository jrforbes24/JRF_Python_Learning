def todo_list():
    #Greeting
    print("Welcome to your todo list!")    
    #instantiate todo list
    todo = []
    #instantiate complete list
    complete = []
    #instantiate counter
    key = 0

    #start while loop
    while True: 
        print('__________________________\n')
        #display todo and completelist
        print("\033[1mTo Do\033[0m")
        for t in todo:
            # making the tuple a string with different types of variables
            t_string = " ".join([str(item)for item in t])
            print(t_string)
        
        print("\n\n\033[1mCompleted\033[0m")
        for c in complete:
            # making the tuple a string with different types of variables
            c_string= " ".join([str(item)for item in c])
            print(c_string)
        
        print('__________________________\n')

        #ask what user would like to do add, complete, delete, exit
        action = input("What would you like to do? ( [a]dd, [c]omplete, [d]elete, e[x]it ])").lower().strip()
        answers = 'a','c','d','x'
        if action in answers:
            print('okay')
        else:
            print(f'Not a valid choice, please use a, c, d, or x./n')
            continue

        #if x break
        if action == 'x':
            print('Goodbye and thanks!')
            break

        #elif a ask for string and add to todo list then continue
        elif action == 'a':
            to_add = input('What would you like add?')
            print()
            item_2_add = (str(key), to_add)
            todo.append(item_2_add)
            key += 1
            continue

        #elif c ask for number of todo to complete then continue
        elif action == 'c':
            to_move = input(str('What would you like to move to Completed? (the number?)'))
            print()
            my_Index = 0
            # find the index of the item to move, may not be the same as the number they input
            for t in todo:
                if to_move in t[0]:
                    my_Index = todo.index(t)
            # checking for a valid index
            if my_Index >= 0:
                print(f'Found {str(to_move)}. Moving now.')
            else:
                print('That does not seem correct')

            # pop from todo and append to completed
            popped = todo.pop(my_Index)
            complete.append(popped)
            print() 
            continue

            #else ask which number they would like to delete type all to delete all
        else:
            what_del = input(str('Which would you like to remove? number or all for nuclear option.')) 
            if what_del.lower() == 'all':
                todo = []
                complete = []
                continue
            else:                
                my_Index = None
                for i in todo:
                    if what_del in i[0]:
                        my_Index = todo.index(i)
                if my_Index is not None:
                    del todo[my_Index]
                my_Index = None
                for j in complete:
                    if what_del in j[0]:
                        my_Index = complete.index(j)
                if my_Index is not None:
                    del complete[my_Index]
            continue
                



if __name__ == "__main__":
    todo_list()
    

