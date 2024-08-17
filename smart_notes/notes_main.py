from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

# ----------------------- Вікно програми 

app = QApplication([])
window = QWidget()
main_widht, main_height = 800, 600
window.setWindowTitle("Smart notes")
window.resize(main_widht, main_height)
window.setStyleSheet('bacground-color:rgb(235, 231, 255); font-size:15px')

# ------------------------
    #Елементи інтерфейсу
# ------------------------
text_editor = QTextEdit()                                       #Введення тексту замітки
text_editor.setPlaceholderText('Введіть текст....')
text_editor.setStyleSheet(' background-color:#CCFFFF;')

list_widget1 = QListWidget()                                    #список заміток                    
list_widget1.setStyleSheet(' background-color:#CCFFFF;')

list_widget2 = QListWidget()                                    #список тегів
list_widget2.setStyleSheet(' background-color:#CCFFFF;')

text_searcher = QLineEdit()                                     #пошук по тексту
text_searcher.setPlaceholderText('Введіть текст...')

teg_searcher = QLineEdit()                                      #пошук по тегу
teg_searcher.setPlaceholderText('Введіть тег...')

make_note = QPushButton()
make_note.setText('Створити замітку')

delete_note = QPushButton()
delete_note.setText('Видалити замітку')

save_note = QPushButton()
save_note.setText('Зберегти замітку')

add_to_note = QPushButton()
add_to_note.setText('Додати до замітки')

unpin_to_note = QPushButton()
unpin_to_note.setText('Відкріпити від замітки')

search_for_text = QPushButton()
search_for_text.setText('Шукати замітку за текстом')

search_for_teg = QPushButton()
search_for_teg.setText('Шукати замітку за тегом')

action_theme_btn = QPushButton()
action_theme_btn.setText('Змінити тему')

# ----------------------------
    #Розміщення на макет
# ----------------------------

row1 = QHBoxLayout()
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget1)
col2.addLayout(row1)
col2.addWidget(save_note)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список тегів:"))
col2.addWidget(list_widget2)
col2.addWidget(QLabel("Ввід даних:"))
col2.addWidget(teg_searcher)
col2.addWidget(text_searcher)
col2.addLayout(row2)
col2.addWidget(search_for_teg)
col2.addWidget(search_for_text)
col2.addWidget(action_theme_btn)


#Злиття макетів
layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

#Макет на екран
window.setLayout(layout_note)

# -------------------------------
window.show()
app.exec_()