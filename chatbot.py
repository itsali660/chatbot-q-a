FILE_NAME = "qa.txt"

# load q/a from file
def load_data():
    data = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            if "|" in line:
                q,a = line.strip().split("|")
                data.append((q,a))
    return data

# save q/a back to file
def save_data(data):
    with open(FILE_NAME, "w") as file:
        for q,a in data:
            file.write(f"{q}|{a}\n")

# display all questions
def display_questions(data):
    print("\nAvailable Questions: \n")

    if not data:
        print("No questions found.")
        return

    for i in range(len(data)):
        print(f"{i + 1}. {data[i][0]}")

# only allowed numbers within range
# max_choice = 5
def get_valid_choice(max_choice):
    while True:
        choice =input("\n Enter Question number to ans/del : \n")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= max_choice:
                return choice
        print("Invalid input, plz enter a valid number \n")
# add a new question
def add_question(data):
    q = input("Enter Question: ")
    a = input("Enter Answer: ")
    data.append((q,a))
    save_data(data)
    print("Question added successfully!!!! \n")

# delete a question
def delete_question(data):
    if not data:
        print("No questions to delete.")
    display_questions(data)
    choice = get_valid_choice(len(data))
    removed = data.pop(choice - 1)
    save_data(data)
    print(f"Removed: {removed[0]}? \n")

# main function
def chatbot():
    data = load_data()

    while True:
        print("\nMenu: \n")
        print("1. Ask a question")
        print("2. Add a question")
        print("3. Delete a question")
        print("4. Exit \n")

        choice = input("Enter your choice: ")
        print(" ")

        if choice == "1":
            if not data:
                print("No questions found.")
                return
            display_questions(data)
            q_choice = get_valid_choice(len(data))
            print("Answer: ", data[q_choice - 1][1])
        elif choice == "2":
            add_question(data)
        elif choice == "3":
            delete_question(data)
        elif choice == "4":
            print("Thank you for using the program!!, bye")
            break
        else:
            print("Invalid input, plz enter a valid number")



if __name__ == "__main__":
    chatbot()