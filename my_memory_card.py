from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, \
    QRadioButton, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(
self, question, right_answer,
wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


questions_list = []
questions_list.append(Question('Кто наряжается всего раз в год?', 'Новогодняя ёлка', 'Дед мороз', 'Снегурочка', 'Баба яга'))
questions_list.append(Question('Какой стандартный наряд деда мароза?', 'Красный', 'Зелёный', 'Белый', 'Синий'))
questions_list.append(Question('Когда можно найти прошлогодний снег?', '1 января',  '30 декабря', '31 декабря', '10 января'))
questions_list.append(Question('Стоит в углу, а не наказан,И Путин по нему показан.', 'телевизор',  'Московский Кремль', 'стол', 'елка',))
questions_list.append(Question('Без нее Новый год просто немыслим. И это не елка!', 'водка',  'бингальские огни', 'хлопушка', 'курица'))
questions_list.append(Question('Откуда снежная баба родом?', 'из зимбабве', 'нигерия', 'париж', 'нидерланды'))
questions_list.append(Question('Красавица, не дурочка – Ну, ясень пень', 'снегурочка', 'снежная баба', 'Lina', 'Venomancer'))


app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('')
layout_main = QVBoxLayout()
ans = QLabel('Вопрос')
res = QLabel('Правильный ответ')
res_ind = QLabel('ok')

button = QPushButton('Ответить')
AnsGroupBox = QGroupBox('Правильный ответ')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Шведы')
rbtn_2 = QRadioButton('Американцы')
rbtn_3 = QRadioButton('Русские')
rbtn_4 = QRadioButton('Смурфы')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_res = QVBoxLayout()

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_res = QVBoxLayout()
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    button.setText("Следующий вопрос")


def show_question():
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    AnsGroupBox.hide()
    RadioGroupBox.show()
    button.setText("Ответить")


answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def show_correct(ind):
    res_ind.setText(ind)
    show_result()

def check_answer():
    if answers[0].isChecked():
        # правильный ответ!
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            # неправильный ответ!
            show_correct('Неверно!')

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    ans.setText(q.question)
    res.setText("Ответ:" + q.right_answer)
    show_question()

def next_question():
    ''' задает следующий вопрос из списка '''
    # этой функции нужна переменная, в которой будет указываться номер текущего вопроса
    # эту переменную можно сделать глобальной, либо же сделать свойством "глобального объекта" (app или window)
    # мы заведем (ниже) свойство window.cur_question.
    main_win.total += 1
    print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
    main_win.cur_question = main_win.cur_question + 1  # переходим к следующему вопросу
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0  # если список вопросов закончился - идем сначала
    q = questions_list[main_win.cur_question]  # взяли вопрос
    ask(q)  # спросили


def click_OK():
    ''' определяет, надо ли показывать другой вопрос либо проверить ответ на этот '''
    if button.text() == 'Ответить':
        check_answer()  # проверка ответа
        main_win.score += 1
        print('Статистика\n-Всего вопросов: ', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score / main_win.total * 100), '%')
    else:
        next_question()  # следующий вопрос
        print('Рейтинг: ', (main_win.score / main_win.total * 100), '%')

main_win.cur_question = -1
main_win.score = 0
main_win.total = 0

button.clicked.connect(click_OK)

AnsGroupBox.setLayout(layout_res)
RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox.hide()
layout_main.addWidget(RadioGroupBox)
layout_main.addWidget(AnsGroupBox)

layout_main.addWidget(button)
main_win.setLayout(layout_main)

next_question()

main_win.show()
app.exec_()










































































































































































































































































































































































































































































































































































































































































































































































































































































































































































