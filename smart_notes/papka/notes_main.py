# --------------------------- Підключаємо бібліотеки
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json

# -----------------------------------------------------------------
'''Замітки в json'''

notes = {
    "Ласкаво просимо!" : {                                          #Назва               
        "text" : "Це найкращий додаток для заміток у світі",        
        "tag" : ["добро", "інструкція"]
    }
}

def writeToFile():
    with open("notes_data.json", "w") as file:
        json.dump(notes, file, sort_keys=True)

'''Інтерфейс програми'''
# ---------------------------
#   Вікно програми
# ---------------------------
app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600  # початкові розміри головного вікна
window.setWindowTitle("Smart Notes")
window.resize(main_width,main_height)
window.setStyleSheet('background-color:rgb(235, 231, 255);font-size:15px')

# ---------------------------
#     Eлементи інтерфейсу
# ---------------------------
text_editor = QTextEdit()                                           # Введення тексту замітки
text_editor.setStyleSheet(' background-color:#CCFFFF;')
text_editor.setPlaceholderText('Введіть текст...')

list_widget_1 = QListWidget()                                       # Список заміток
list_widget_1.setStyleSheet('background-color:#CCFFFF;')

list_widget_2 = QListWidget()                                       # Список (Контактні дані)
list_widget_2.setStyleSheet('background-color:#CCFFFF;')

text_searcher = QLineEdit()                                         # Пошук  по тексту
text_searcher.setPlaceholderText('Введіть текст...')

tag_searcher = QLineEdit()
tag_searcher.setPlaceholderText('Введіть тег...')                   # Пошук  по тегу

# ---------------------------
#      Створення кнопок
# ---------------------------
make_note = QPushButton()
make_note.setStyleSheet('background-color: orange;')
make_note.setText("Створити замітку")                   

delete_note = QPushButton()
delete_note.setStyleSheet('background-color: orange;')
delete_note.setText("Видалити замітку")                  

save_note = QPushButton()
save_note.setStyleSheet('background-color: orange;')
save_note.setText("Зберегти замітку")                  

search_for_text = QPushButton()
search_for_text.setStyleSheet('background-color: orange;')
search_for_text.setText("Шукати замітку за текстом")         

search_for_tag = QPushButton()
search_for_tag.setStyleSheet('background-color: orange;')
search_for_tag.setText("Шукати замітку за тегом")           

add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: rgb(152, 157, 249);')
add_to_note.setText("Додати до замітки")                   

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: rgb(152, 157, 249);')
unpin_to_note.setText("Відкріпити від замітки")

action_theme_btn = QPushButton()
action_theme_btn.setStyleSheet('background-color: rgb(231, 188, 249);')
action_theme_btn.setText("Змінити тему")

# ---------------------------
#   Розміщення на макет
# ---------------------------
row1 = QHBoxLayout()              # - гориз додати і видалити замітку
row1.addWidget(make_note)
row1.addWidget(delete_note)

row2 = QHBoxLayout()              # - гориз дод. до замітки та відкріпити від замітки
row2.addWidget(add_to_note)
row2.addWidget(unpin_to_note)

col1 = QVBoxLayout()              # - вер. ввести текст
col1.addWidget(text_editor)

col2 = QVBoxLayout()
col2.addWidget(QLabel("Список заміток:"))
col2.addWidget(list_widget_1)
col2.addLayout(row1)
col2.addWidget(save_note)
   
col2.addWidget(QLabel("Список тегів:"))
col2.addWidget(list_widget_2)
col2.addWidget(QLabel("Ввід данних:"))
col2.addWidget(tag_searcher)
col2.addWidget(text_searcher)
col2.addLayout(row2)

# Нижні 3 кнопки
col2.addWidget(search_for_tag)
col2.addWidget(search_for_text)
col2.addWidget(action_theme_btn)

# Злиття
layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

# Макет на екран
window.setLayout(layout_note) 

# --------------------------------------------------------------------

'''Функціонал програми'''
# -------------------- [ Замітки ]  ---------------------------------

def show_notes():
    global key
    key = list_widget_1.selectedItems()[0].text()
    list_widget_2.clear()
    text_editor.setText(notes[key]["text"])
    list_widget_2.addItems(notes[key]["tag"])

def add_notes():
    note_name, ok = QInputDialog.getText(window, 'Додати замітку', "Назва замітки")
    if note_name and ok:
        list_widget_1.addItem(note_name)
        notes[note_name] = {"text":"","tag":[]}
    writeToFile()

def delete_notes():
    if list_widget_1.currentItem():
        if key in notes:
            notes.pop(key)

            text_editor.clear()
            list_widget_2.clear()
            list_widget_1.clear()
            list_widget_1.addItem(notes)
            writeToFile()

def save_notes():
    if list_widget_1.currentItem():
        key = list_widget_1.currentItem().text()
        notes[key]["text"] = text_editor.toPlainText()
        writeToFile()

save_note.itemClicked.connect(save_notes)
list_widget_1.itemClicked.connect(show_notes)


with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_widget_1.addItems(notes)



# --------------------------- Закриття програми та показ
window.show()
app.exec_()
