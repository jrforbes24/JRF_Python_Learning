sequence = [10, 1, 2, 3, 4, 5]

def almostIncreasingSequence(sequence):
    the_sequence = list(range(0, len(sequence)))
    valid_count = 0
    invalid_count = 0

    for i in the_sequence:
        print(valid_count)
        print(invalid_count)
        if(i+1 != len(sequence)):
            if(sequence[i] < sequence[i+1]):
                valid_count += 1
                
            else:
                if(invalid_count == 1):                    
                    return False
                    break
                else:
                    
                        

    if(invalid_count >= 2):
        return False
    else:
        return True                               
    


print(almostIncreasingSequence(sequence))

