
questions = [
    ["Who is Chanakya?","WWE wrestler","Finance minister","Scientist","Astronomer",2],
    ["What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Perth", 2], # type: ignore
    ["Who invented the telephone?", "Albert Einstein", "Alexander Graham Bell", "Isaac Newton", "Thomas Edison", 1],
    ["What is the chemical symbol for Gold?", "Ag", "Au", "Gd", "Go", 1],
    ["Which planet is known as the Red Planet?", "Earth", "Jupiter", "Mars", "Venus", 2],
    ["Who wrote the play 'Romeo and Juliet'?", "Charles Dickens", "Leo Tolstoy", "William Shakespeare", "George Orwell", 2],
    ["Which is the largest ocean on Earth?", "Indian Ocean", "Arctic Ocean", "Atlantic Ocean", "Pacific Ocean", 3]
    ]
prizes = [10,100,1000,2000,3000,5000,10000]
i=0
for question in questions:
    print(question[0])
    print(f"1.{question[1]}")
    print(f"2.{question[2]}")
    print(f"3.{question[3]}")
    print(f"4.{question[4]}")
#now checking if the answer is correct or not 
    a= int(input("Enter your answer: 1/2/3/4: \n"))
    if a==question[5]:
        print("Right answer")
        for j in range(len(prizes)):
            if j==i:
                print(f"You won {prizes[a-1]}\n")
                break
        i+=1
    else:
        print("That was incorrect.")
        break