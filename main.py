# Kon Banega Crorepati

import random

questions = ['What is the capital city of India ?',
             "Who is popularly known as the “Iron Man” of India ?",
             "Which place in India is also known as the “Land of Rising Sun” ?",
             "Which of the following states is not located in the North ?",
             "Which is the largest coffee-producing state of India ?",
             "Ministry of Culture launched an initiative 'India ki Udaan' along with which company ?",
             "Which is the first institution in India to join IBM Quantum Network ?",
             "Which city is known as the “summer capital” of Jammu and Kashmir ?",
             "Which company has launched dedicated air cargo service in India to speed up deliveries ?",
             "What is the name of India’s first regional AI news presenter ?"]

answer = ["New Delhi", "Sardar Vallabh Bhai Patel",
          'Arunachal Pradesh', 'Jharkhand', 'Karnataka', 'Google', 'IIT Madras', 'Srinagar', 'Amazon', 'Lisa']

options = ['New Delhi', 'Mumbai', 'Kolkata', 'Chennai',
           'Lal Bahadur Shastri', 'Sardar Vallabh Bhai Patel', 'Mahatma Gandhi', 'Dr. B.R Ambedkar',
           'Sikkim', 'Arunachal Pradesh', 'Karnataka', 'Gujarat',
           'Jharkhand', 'Jammu and Kashmir', 'Himachal Pradesh', 'Haryana',
           'Kerala', 'Tamil Nadu', 'Karnataka', 'Arunachal Pradesh',
           'Microsoft', 'Google', 'Meta', 'Amazon',
           'IIT Bombay', 'IIM Ahmedabad', 'IIM Bengaluru', 'IIT Madras',
           'Jammu', 'Srinagar', 'Shimla', 'Anantnag',
           'Flipkart', 'Amazon', 'Tata Cliq', 'Jiomart',
           'Tina', 'Lisa', 'Mona', 'Hira']

points = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]

index = 0
point = 0
number = 1

# Empty List
repeated = list()

while True:
    alphabet = 'A'

    random_que = random.randint(0, 9)

    # For Getting New Question
    if random_que not in repeated:
        repeated.append(random_que)
        print('-------------------------------------------------------------------------------------------------------')
        print("Question", number, ":", questions[random_que])
        number = number + 1
        print('-------------------------------------------------------------------------------------------------------')

        print("Options:", end=' ')

        # For Alphabetic Options
        for option in options[random_que*4:random_que*4+4]:
            print("{}.".format(alphabet), option, end='  ')
            alphabet = chr(ord(alphabet) + 1)

        print()
        print('-------------------------------------------------------------------------------------------------------')

        # User Input for Answer
        user = input("Answer -> ")
        if user == answer[random_que]:
            print("Answer is Right")
            point = points[index]
            print("Winning Amount:", point)
            index = index + 1
        else:
            print("Wrong")
            print("Winning Amount:", point)
            break
        print('-------------------------------------------------------------------------------------------------------')

    # Checking Questions are Completed.
    elif len(repeated) == len(questions):
        print("You Won the Game")
        break
