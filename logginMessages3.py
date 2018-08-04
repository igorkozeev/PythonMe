import logging

logging.basicConfig(level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')
# Now if you want to store a logging in a file, just insert a "filename ='myProgramLog.txt',"
# in a basic config call. See beyond:
# logging.basicConfig(filename = 'myProgramLog.txt', level=logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')


#logging.disable(logging.CRITICAL) # disable logging function
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial %s' % (n))
    total = 1
    for i in range(1, n+1):
        total = total * i
        logging.debug('i is %s and total is %s' % (i,total))
    logging.debug('Return value is %s' % (total))
    return total

print(factorial(5))

logging.debug('End of program')
