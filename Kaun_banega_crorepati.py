questions = [["Which language was used to create FB ?", "Python", "French", "Javascript", "Php", "None", 4],
["What are the mostly used languages for frontend ?", "HTML and Python", "C# and CSS", "HTML and CSS", "C++ and Java", "None", 3],
["Which language is mostly used for Data Structures ?", "Python", "C#", "Javascript", "C++",  "None", 4], 
["Which language is best known for secure data ?", "Python", "Java", "Javascript", "Php",  "None", 2]] 

levels = [4000, 6000, 8000, 10000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"\nQuestion for Rs. {levels[i]}")
    print(f"\n{question[0]} ")
    print(f"a. {question[1]}         b. {question[2]}")
    print(f"c. {question[3]}         d. {question[4]}")
    
    reply = int(input("Enter your answer (1-4) : "))
    if(reply == question[-1]):
        print(f"Correct answer, you won Rs. {levels[i]}")
        if(i == 3):
            money = 28000
        elif(i == 2):
            money = 18000
        elif(i == 1):
            money = 10000
        elif(i == 0):
            money = 4000
    else:
        print("Wrong Answer")
        break
print(f"\n\nYour total money is {money}")