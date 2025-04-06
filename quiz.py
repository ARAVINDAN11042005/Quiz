import tkinter as tk

root = tk.Tk()
root.title("Python Quiz App")
root.geometry('1300x800')

score = 0
username = ""
q_widgets = []  


label_t = tk.Label(root, text="QUIZ", font=("arial", 50))
label_t.place(x=600, y=50)


label_u = tk.Label(root, text="Username", font=("arial", 30))
label_u.place(x=250, y=250)
entry = tk.Entry(root, font=("arial", 30))
entry.place(x=500, y=250)

def increase():
    global score
    score += 1

def clear_widgets(widgets):
    for w in widgets:
        w.destroy()


def question1():
    global q_widgets
    clear_widgets([label_t, label_u, entry, enter_button])
    label_q = tk.Label(root, text="Question 1", font=("Arial", 35))
    label_q.place(x=550, y=50)
    label = tk.Label(root, text="Which of them is a Keyword in Python?", font=("Arial", 30))
    label.place(x=300, y=100)

    b1 = tk.Button(root, text="range", font=("Arial", 20), command=lambda: question2())
    b2 = tk.Button(root, text="def", font=("Arial", 20), command=lambda: [increase(), question2()])
    b3 = tk.Button(root, text="Val", font=("Arial", 20), command=lambda: question2())
    b4 = tk.Button(root, text="to", font=("Arial", 20), command=lambda: question2())

    b1.place(x=400, y=200)
    b2.place(x=800, y=200)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

    q_widgets = [label_q, label, b1, b2, b3, b4]

def question2():
    global q_widgets
    clear_widgets(q_widgets)
    label_q = tk.Label(root, text="Question 2", font=("Arial", 35))
    label_q.place(x=550, y=50)
    label = tk.Label(root, text="Which is a built-in function in Python?", font=("Arial", 30))
    label.place(x=300, y=100)

    b1 = tk.Button(root, text="factorial()", font=("Arial", 20), command=lambda: question3())
    b2 = tk.Button(root, text="print()", font=("Arial", 20), command=lambda: [increase(), question3()])
    b3 = tk.Button(root, text="seed()", font=("Arial", 20), command=lambda: question3())
    b4 = tk.Button(root, text="sqrt()", font=("Arial", 20), command=lambda: question3())

    b1.place(x=400, y=200)
    b2.place(x=800, y=200)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

    q_widgets = [label_q, label, b1, b2, b3, b4]

def question3():
    global q_widgets
    clear_widgets(q_widgets)
    label_q = tk.Label(root, text="Question 3", font=("Arial", 35))
    label_q.place(x=550, y=50)
    label = tk.Label(root, text="Which of these is not a core data type in Python?", font=("Arial", 30))
    label.place(x=250, y=100)

    b1 = tk.Button(root, text="Tuple", font=("Arial", 20), command=lambda: question4())
    b2 = tk.Button(root, text="Dictionary", font=("Arial", 20), command=lambda: question4())
    b3 = tk.Button(root, text="Lists", font=("Arial", 20), command=lambda: question4())
    b4 = tk.Button(root, text="Class", font=("Arial", 20), command=lambda: [increase(), question4()])

    b1.place(x=400, y=200)
    b2.place(x=800, y=200)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

    q_widgets = [label_q, label, b1, b2, b3, b4]

def question4():
    global q_widgets
    clear_widgets(q_widgets)
    label_q = tk.Label(root, text="Question 4", font=("Arial", 35))
    label_q.place(x=550, y=50)
    label = tk.Label(root, text="Who developed Python?", font=("Arial", 30))
    label.place(x=400, y=100)

    b1 = tk.Button(root, text="Wick Van Rossum", font=("Arial", 20), command=lambda: question5())
    b2 = tk.Button(root, text="Rasmus Lerdorf", font=("Arial", 20), command=lambda: question5())
    b3 = tk.Button(root, text="Guido Van Rossum", font=("Arial", 20), command=lambda: [increase(), question5()])
    b4 = tk.Button(root, text="Niene Stom", font=("Arial", 20), command=lambda: question5())

    b1.place(x=400, y=200)
    b2.place(x=800, y=200)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

    q_widgets = [label_q, label, b1, b2, b3, b4]

def question5():
    global q_widgets
    clear_widgets(q_widgets)
    label_q = tk.Label(root, text="Question 5", font=("Arial", 35))
    label_q.place(x=550, y=50)
    label = tk.Label(root, text="Extension of Python file is?", font=("Arial", 30))
    label.place(x=400, y=100)

    b1 = tk.Button(root, text=".python", font=("Arial", 20), command=lambda: show_result())
    b2 = tk.Button(root, text=".p", font=("Arial", 20), command=lambda: show_result())
    b3 = tk.Button(root, text=".pl", font=("Arial", 20), command=lambda: show_result())
    b4 = tk.Button(root, text=".py", font=("Arial", 20), command=lambda: [increase(), show_result()])

    b1.place(x=400, y=200)
    b2.place(x=800, y=200)
    b3.place(x=400, y=300)
    b4.place(x=800, y=300)

    q_widgets = [label_q, label, b1, b2, b3, b4]

def show_result():
    global q_widgets
    clear_widgets(q_widgets)
    label_q = tk.Label(root, text="RESULT", font=("Arial", 40))
    label_q.place(x=550, y=50)

    name_label = tk.Label(root, text=username, font=("Arial", 30))
    name_label.place(x=200, y=200)

    score_label = tk.Label(root, text=f"Your score is: {score}/5", font=("Arial", 30))
    score_label.place(x=500, y=200)

    q_widgets = [label_q, name_label, score_label]


def start_quiz():
    global username
    username = entry.get()
    question1()

enter_button = tk.Button(root, text="ENTER", font=("arial", 30), command=start_quiz)
enter_button.place(x=600, y=350)

root.mainloop()
