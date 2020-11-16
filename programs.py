import tkinter as tk
import random

window = tk.Tk()
window.title('Проверка знаний ученков')
window.geometry('300x280')

topics = ['Основы','Переменные', 'Условия', 'Циклы', 'Списки', 'Функции', 'Tkinter', 'Классы']

questions = {
    'Основы':
        [
            [
                ["Как вывести информацию на печать (экран)", "командой print()"],
                ["Как попросить пользователя ввести данные", "командой input()"],
                ["Как отличить строку(текст) от переменной", "Строка пишется в кавычках"],
                ["Какие есть два типа данных и их команды", "Строки str() и целые числа int()"],
                ["Как преобразовать число в текст?", "Использовать команду int()"],
                ["Можно ли складывать текст", "Да, с помощью знака +"]
            ]
        ],
    'Переменные':
        [
            [
                ["Что такое переменные?", "Ответит подходит под шаблон Это что-то, что можно как-то назвать и положить туда какие-то значения."],
                ["Как создать переменную?", "Написать имя переменной и присвоить/положить/записать туда какие значения."],
                ["Как присвоить/положить/записать какие-то значения в переменную?", "Использовать знак равно"]
            ],
            [
                "Как увеличить значение переменной на 1?: Записать в переменную сумму старого значения переменной плюс 1, или на примере переменной проговорил всё словами <имя_переменной>=<имя_переменной>+1",
                "Какие имена можно использовать для переменных, или может ли в именах переменных стоять пробел?: Как угодно, пробел ставить нельзя."
            ]
        ]
}

users = {
    'Имя': ['уровень игрока',['уровень простых воросов, правильных ответов, неправильных ответов']],
    'name': [3,[0,0,0]]
        }


frame_question = tk.Frame(window)
frame_buttons = tk.Frame(window)



for user in users.keys():
    if user == 'name':
        user_name = user

frame_question.pack()

name_user = tk.Label(frame_question, text=user_name, font=('Arial', 10, 'bold'), fg='blue')


frame_level_user = tk.Frame(frame_question)
frame_level_user.pack()

level_user = tk.Label(frame_level_user, text=f"Прошёл уроков: {users[user_name][0]}")


level_up = tk.Button(frame_level_user, width=2, height=1, text='+')

text_topic = tk.Label(frame_question)


text_question = tk.Label(frame_question, wraplength=250, height=3,font=('Arial', 10, 'bold'))


text_answer = tk.Label(frame_question, wraplength=250, height=5, fg='green')


def start_view():
    name_user.pack()
    level_user.pack(side='left')
    level_up.pack(side='left')
    text_topic.pack()
    text_question.pack()
    text_answer.pack()
    left_button.pack(side='left')
    right_button.pack(side='left', padx=5)
    button_new_game.pack_forget()

def hidden_elements():
    text_topic.pack_forget()
    text_question.pack_forget()
    text_answer.pack_forget()
    name_user.pack_forget()
    level_user.pack_forget()
    right_button.pack_forget()
    left_button.pack_forget()
    level_up.pack_forget()

def start_data():
    global list_topics, question_answer
    list_topics = []
    question_answer = []
    user_level = users[user_name][0]
    if user_level < 3:
        list_topics = topics[0:1]
    elif user_level == 3:
        list_topics += topics[0:2]


def start_quiz():
    global count_question, topic, question_answer, random_list_topic, random_question_answer

    start_data()
    start_view()

    random_list_topic = random.sample(list_topics, len(list_topics))
    topic = random_list_topic[0]
    random_list_topic.remove(topic)
    [question_answer.append(qa) for qa in questions[topic][0]]
    random_question_answer = random.sample(question_answer, len(question_answer))
    text_topic['text'] = f"Тема: {topic}"
    text_question['text'] = random_question_answer[0][0]
    text_answer['text'] = random_question_answer[0][1]
    random_question_answer.remove(random_question_answer[0])
    count_question = 1


def work_quiz():
    global count_question, topic, question_answer, random_list_topic, random_question_answer
    try:
        if count_question == 3:
            topic = random_list_topic[0]
            random_list_topic.remove(topic)
            [question_answer.append(qa) for qa in questions[topic][0]]
            random_question_answer = random.sample(question_answer, len(question_answer))
            count_question = 0

        text_topic['text'] = f"Тема: {topic}"
        text_question['text'] = random_question_answer[0][0]
        text_answer['text'] = random_question_answer[0][1]
        random_question_answer.remove(random_question_answer[0])
        count_question += 1
    except IndexError:
        hidden_elements()
        button_new_game.pack()




def right_answer():
    work_quiz()

def wrong_answer():
    pass

frame_buttons.pack(pady=5)

left_button = tk.Button(frame_buttons, command=wrong_answer)
left_button.config(width=15, height=2, text='Не правильно')


right_button = tk.Button(frame_buttons, command=right_answer)
right_button.config(width=15, height=2, text='Правильно')


button_new_game = tk.Button(command=start_quiz)


start_quiz()


window.mainloop()