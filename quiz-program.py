# Project_3: quiz program

# dictionary for a variety of questions
quiz = {
    "question1":{
        "question": "What is the name of our planet?",
        "answer": "World"
        
    },
    "question2":{
        "question": "How many levels are there in the OSI model?",
        "answer": "7"
    },
    "question3":{
        "question": "Which command in the Linux terminal displays a list of directories: ls or cat?",
        "answer": "ls"
    },
    "question4":{
        "question": "How many layers are there in the data transmission network model?",
        "answer": "4"
    }
}


def quiz_process():
    user_points = 0

    for key, value in quiz.items():
        print(value['question'])
        answer = input("What is your answer: ")
        edit_answer = answer.strip() # removing spaces before and after a word

        if edit_answer.lower() == value['answer'].lower():
            print("Correct!")
            user_points+=1
        else:
            print("Incorrect...")
        
    print(f"Your have {user_points} points out of 4")


if __name__ == "__main__":
    quiz_process()



