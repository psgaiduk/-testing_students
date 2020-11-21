import tkinter as tk
import tkinter.messagebox as tmb
import random
import json

window = tk.Tk()
window.title("Проверка знаний ученков")
window.geometry("300x300")

topics = ["Основы","Переменные", "Условия", "Циклы", "Списки", "Функции", "Tkinter", "Классы"]

questions = {
    "Основы":
        [
            [
                ["Как вывести информацию на печать (экран)", "командой print()"],
                ["Как попросить пользователя ввести данные", "командой input()"],
                ["Какие есть два типа данных и их команды", "Строки str() и целые числа int()"],
                ["Как преобразовать число в текст?", "Использовать команду int()"],
                ["Как отличить строку(текст) от переменной", "Строка пишется в кавычках"],
                ["Можно ли складывать текст", "Да, с помощью знака +"]
            ],
            [
                ["Какие есть два типа данных и их команды", "Строки str() и целые числа int()"],
                ["Как преобразовать число в текст?", "Использовать команду int()"],
                ["Можно ли складывать текст", "Да, с помощью знака +"]
            ]
        ],
    "Переменные":
        [
            [
                ["Что такое переменные?", "Ответит подходит под шаблон Это что-то, что можно как-то назвать и положить туда какие-то значения."],
                ["Как создать переменную?", "Написать имя переменной и присвоить/положить/записать туда какие значения."],
                ["Как присвоить/положить/записать какие-то значения в переменную?", "Использовать знак равно"]
            ],
            [
                ["Как увеличить значение переменной на 1?"], ["Записать в переменную сумму старого значения переменной плюс 1, или на примере переменной проговорил всё словами <имя_переменной>=<имя_переменной>+1"],
                ["Какие имена можно использовать для переменных, или может ли в именах переменных стоять пробел?"], ["Как угодно, пробел ставить нельзя."],
                ["",""]
            ]
        ]
}


with open("students.txt", "r", encoding="utf-8") as file:
    students = json.load(file)



count_question = 0

def start_view():
    name_user["text"] = f"{student_name}"
    level_user["text"] = f'Прошёл уроков: {students[student_name]["level"]}'

    frame_start.pack_forget()
    frame_game.pack()

def get_label_questions():
    label_count_right_answer["text"] = f"Правильных ответов подряд: {students[student_name][topic]['right_series']} ({students[student_name][topic]['right_all']})"
    label_count_wrong_answer["text"] = f"Не правильных ответов подряд: {students[student_name][topic]['wrong']} ({students[student_name][topic]['wrong_all']})"
    text_topic["text"] = f"Тема: {topic} - уровень {students[student_name][topic]['level']}"

def get_question():
    global count_question, random_question_answer
    text_question["text"] = random_question_answer[0][0]
    text_answer["text"] = random_question_answer[0][1]
    random_question_answer.remove(random_question_answer[0])
    count_question += 1

def get_info_end():
    message_repeat = 'Темы к повторению: '
    for topic_name, data_from_topic in students[student_name].items():

        if topic_name != 'level' and data_from_topic['count_10'] >= 10:
            if data_from_topic['right_10'] <= 6:
                message_repeat += f'\n{topic_name} - точность ответов {data_from_topic["right_10"]/data_from_topic["count_10"]} %'
            data_from_topic['count_10'] = 0
            data_from_topic['right_10'] = 0
            with open("students.txt", "w", encoding="utf-8") as file:
                json.dump(students, file)
    if  message_repeat != 'Темы к повторению: ':
        tmb.showinfo("Внимание", f"{message_repeat}")


def check_level_topic():
    global level_topics
    if len(questions[topic]) <= students[student_name][topic]['level']:
        level_topics = len(questions[topic]) - 1
    else:
        level_topics = students[student_name][topic]['level']

def start_data():
    global list_topics, question_answer, student_name, num_questions, count_question
    student_name = listbox_user_name.get("active")
    count_question = 0
    list_topics = []
    question_answer = []
    user_level = students[student_name]["level"]
    if user_level < 3:
        list_topics = topics[0:1]
        num_questions  = 5
    elif user_level == 3:
        list_topics += topics[0:2]
        num_questions  = 3



def start_quiz():
    global count_question, topic, question_answer, random_list_topic, random_question_answer, right_answer, level_topics

    start_data()
    start_view()

    random_list_topic = random.sample(list_topics, len(list_topics))
    topic = random_list_topic[0]
    random_list_topic.remove(topic)
    check_level_topic()
    [question_answer.append(qa) for qa in questions[topic][level_topics]]
    random_question_answer = random.sample(question_answer, len(question_answer))
    get_question()
    get_label_questions()


def work_quiz():
    global count_question, topic, question_answer, random_list_topic, random_question_answer, right_answer
    try:
        if count_question == num_questions:
            topic = random_list_topic[0]
            random_list_topic.remove(topic)
            [question_answer.append(qa) for qa in questions[topic][level_topics]]
            random_question_answer = random.sample(question_answer, len(question_answer))
            count_question = 0

        get_question()
    except IndexError:
        start_window()
        get_info_end()

def right_answer():
    students[student_name][topic]["right"] += 1
    students[student_name][topic]["right_all"] += 1
    students[student_name][topic]["all_answer"] += 1
    students[student_name][topic]["right_10"] += 1
    students[student_name][topic]["right_series"] += 1
    students[student_name][topic]['count_10'] += 1
    if students[student_name][topic]["right"] == 6:
        students[student_name][topic]["right"] = 0
        if len(questions[topic]) > students[student_name][topic]["level"] + 1:
            students[student_name][topic]["level"] += 1
    if students[student_name][topic]["right_series"] == 10:
        students[student_name][topic]["wrong"] = 0
    with open("students.txt", "w", encoding="utf-8") as file:
        json.dump(students, file)
    check_level_topic()
    get_label_questions()
    work_quiz()




def wrong_answer():
    students[student_name][topic]["wrong"] += 1
    students[student_name][topic]["wrong_all"] += 1
    students[student_name][topic]["all_answer"] += 1
    students[student_name][topic]["right"] = 0
    students[student_name][topic]['count_10'] += 1
    students[student_name][topic]["right_series"] = 0
    if students[student_name][topic]["wrong"] == 3:
        students[student_name][topic]["wrong"] = 0
        if students[student_name][topic]["level"] > 0:
            students[student_name][topic]["level"] -= 1
    with open("students.txt", "w", encoding="utf-8") as file:
        json.dump(students, file)
    check_level_topic()
    get_label_questions()
    work_quiz()

def start_window():
    frame_game.pack_forget()
    frame_start.pack()

    listbox_user_name.delete(0,"end")

    for student in students:
        listbox_user_name.insert("end",student)



frame_start = tk.Frame(window)
frame_game = tk.Frame(window)

frame_question = tk.Frame(frame_game)
frame_buttons = tk.Frame(frame_game)
frame_info = tk.Frame(frame_game)

frame_level_user = tk.Frame(frame_question)

frame_game.pack()
frame_start.pack()


frame_question.pack()
frame_level_user.pack()
frame_buttons.pack(pady=5)
frame_info.pack()

listbox_user_name = tk.Listbox(frame_start, selectmode="single")
listbox_user_name.pack()

button_new_game = tk.Button(frame_start, command=start_quiz, text="Начать")
button_new_game.pack()

level_user = tk.Label(frame_level_user)
level_user.pack(side="left")

level_up = tk.Button(frame_level_user, width=2, height=1, text="+")
level_up.pack(side="left")

name_user = tk.Label(frame_question, font=("Arial", 10, "bold"), fg="blue")
name_user.pack()

text_topic = tk.Label(frame_question)
text_topic.pack()

text_question = tk.Label(frame_question, wraplength=250, height=3,font=("Arial", 10, "bold"))
text_question.pack()

text_answer = tk.Label(frame_question, wraplength=250, height=5, fg="green")
text_answer.pack()

left_button = tk.Button(frame_buttons, command=wrong_answer)
left_button.config(width=15, height=2, text="Не правильно")
left_button.pack(side="left")

right_button = tk.Button(frame_buttons, command=right_answer)
right_button.config(width=15, height=2, text="Правильно")
right_button.pack(side="left", padx=5)

label_count_right_answer = tk.Label(frame_info, fg='green')
label_count_right_answer.pack()
label_count_wrong_answer = tk.Label(frame_info, fg="red")
label_count_wrong_answer.pack()

#start_quiz()
start_window()


window.mainloop()