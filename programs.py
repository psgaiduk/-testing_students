import tkinter as tk

window = tk.Tk()
window.title('Проверка знаний ученков')
window.geometry('300x280')

topics = ['Переменные', 'Условия', 'Циклы', 'Списки', 'Функции', 'Tkinter', 'Классы']

questions = {
    'Переменные':
        [
            [
                ["Что такое переменные?", "Ответит подходит под шаблон Это что-то, что можно как-то назвать и положить туда какие-то значения."],
                "Как создать переменную?: Написать имя переменной и присвоить/положить/записать туда какие значения.",
                "Как присвоить/положить/записать какие-то значения в переменную?: Использовать знак равно"
            ],
            [
                "Как увеличить значение переменной на 1?: Записать в переменную сумму старого значения переменной плюс 1, или на примере переменной проговорил всё словами <имя_переменной>=<имя_переменной>+1",
                "Какие имена можно использовать для переменных, или может ли в именах переменных стоять пробел?: Как угодно, пробел ставить нельзя."
            ]
        ]
}

users = {
    'name':
        [
            {'level': 0},
            {'variables': {'level': 0, 'right_answer': 0, 'wrong_answer': 0}}
        ]
        }


frame_question = tk.Frame(window)
frame_buttons = tk.Frame(window)



for user in users.keys():
    if user == 'name':
        user_name = user

frame_question.pack()

name_user = tk.Label(frame_question, text=user_name, font=('Arial', 10, 'bold'), fg='blue')
name_user.pack()

frame_level_user = tk.Frame(frame_question)
frame_level_user.pack()

level_user = tk.Label(frame_level_user, text=f"Прошёл уроков: {users[user_name][0]['level']}")
level_user.pack(side='left')

level_up = tk.Button(frame_level_user, width=2, height=1, text='+')
level_up.pack(side='left')

topic = 'Переменные'

text_topic = tk.Label(frame_question, text=f"Тема: {topic}")
text_topic.pack()

text_question = tk.Label(frame_question, wraplength=250, height=3, text=questions[topic][0][0][0], font=('Arial', 10, 'bold'))
text_question.pack()

text_answer = tk.Label(frame_question, wraplength=250, height=5, text=questions[topic][0][0][1], fg='green')
text_answer.pack()

def right_answer():
    pass

def wrong_answer():
    pass

frame_buttons.pack(pady=5)

right_button = tk.Button(frame_buttons, command=right_answer)
right_button.config(width=15, height=2, text='Правильно')
right_button.pack(side='left', padx=5)

right_button = tk.Button(frame_buttons, command=wrong_answer)
right_button.config(width=15, height=2, text='Не правильно')
right_button.pack(side='left')


window.mainloop()