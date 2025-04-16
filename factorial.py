import logging
logging.basicConfig(filename='factorialLogging.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.DEBUG)

logging.debug('Start of program')

total = 0

def factorial(n):
    total = 1
    logging.debug('Start of the factorial (%s)' % (n))
    for i in range(1,n + 1):
        total = total * i
        logging.debug('i is %s, total is %s' % (i, total))
        
    logging.info('Return value is %s' % (total))
    return total

total = factorial(7)
# print(factorial(1000))
print('The type of total:', type(total), ' The total:', str(total))
logging.debug('End of program')