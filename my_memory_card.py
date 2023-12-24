from random import shuffle, randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []

question_list.append(Question('Что находится под кроватью?', 'пол', 'бабайка', 'носок', 'у меня нет кровати'))

question_list.append(Question('Сколько планет в Солнечной системе?', '8', '6', '10','13'))

question_list.append(Question('Как поймать тигра в клетку?', 'тигров в клетку не бывает', 'заманить куском мяса', 'вежливо попросить', 'НИКАК'))

question_list.append(Question('Как пишется арабская цифра 5?', '5', 'V', '|||||X', '|||||'))

question_list.append(Question('Год выпуска игры Майнкрафт', '2009', '2010', '1999', '2022'))

question_list.append(Question('Какая длина у Великой Китайской стены?', '~9000км', '~9000м', '~5700км', '~12000км'))

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memo card')
window.cur_question = -1
window.resize(600, 400)
window.total = 1
window.score = 0

lb_Question = QLabel('Приблизительное значение числа П(до сотых)')
btn_OK = QPushButton('Ответить')

rbtn_1 = QRadioButton('3,14')
rbtn_2 = QRadioButton('Я низнаю што это такое')
rbtn_3 = QRadioButton('6,2')
rbtn_4 = QRadioButton('10,09')

RadioGroup = QGroupBox('ответы')

radio = QButtonGroup()
radio.addButton(rbtn_1)
radio.addButton(rbtn_2)
radio.addButton(rbtn_3)
radio.addButton(rbtn_4)

ansGroup = QGroupBox('Результат')
lb_result = QLabel('да/нет')

lb_correct = QLabel('3,14')

layout_res =QVBoxLayout()

layout_res.addWidget(lb_result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_correct, alignment = (Qt.AlignHCenter), stretch = 2)

ansGroup.setLayout(layout_res)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroup.setLayout(layout_ans1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroup)
layout_line2.addWidget(ansGroup)

ansGroup.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch = 2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch = 2)
layout_card.addLayout(layout_line2, stretch = 7)
layout_card.addLayout(layout_line3, stretch = 2)

layout_card.addSpacing(5)

window.setLayout(layout_card)

def show_result():
    RadioGroup.hide()
    ansGroup.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroup.show()
    ansGroup.hide()
    btn_OK.setText('Ответить')
    radio.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio.setExclusive(True)

'''def test():
    if 'Ответить' == btn_OK.text():
        show_result()

    else:
        show_question()'''

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Молодец!')
        window.score+=1
        print('Статистика - Всего вопросов', window.total, 'Правильных ответов', window.score)
        print('Рейтинг:', window.score/window.total*100, "%")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг:', window.score/window.total*100, "%")   

def next_question():
    window.total += 1
    print('Статистика - Всего вопросов', window.total, 'Правильных ответов', window.score)
    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()

btn_OK.clicked.connect(click_OK)

window.show()
app.exec()




