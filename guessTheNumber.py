import random

print ('Hi! Try guess and enter number from 1 to 20. You have 6 attemps only.')

secretNumber = random.randint(1,20)
#print('DEBUG: secret number is ' + str(secretNumber))

attempt = 0

while (attempt < 6):
    try:
        attempt = attempt + 1
        number = input()
        if attempt == 1:
            suffix = 'st'
        elif attempt == 2:
            suffix = 'nd'
        elif attempt == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
        
        if int(number) < secretNumber:
            print('Your number is less than mine. This is your ' + str(attempt) + suffix + ' attempt. Take a guess.')
        elif int(number) > secretNumber:
            print('Your number is greater than mine. This is your ' + str(attempt) + suffix + ' attempt. Take a guess.')            
        else:
            break
    except ValueError:
        print('You didn\'t input a number. Please try again')
        attempt = attempt - 1
    

if int(number) == secretNumber:
    print('Congrats! You guessed my number.')
else:
    print('Sorry. You don\'t have any attempts. Try again.')


