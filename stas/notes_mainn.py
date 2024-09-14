# - Підключаємо бібліотеки
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import json
from PyQt5.QtGui import QKeySequence  # запрограмувати клавішу на вихід

# -------------------------- [Створюємо структуру заміток ідентичну json файлу] ------------------------------------------

#  Фукнція для запису заміток до json файлу   
def writeToFile():
    with open('notes.json','w',encoding='utf8') as file:
        json.dump(notes,file,sort_keys=True)

# --------------------------------------------------------------------


'''Інтерфейс програми'''
# ---------------------------
#   Вікно програми
# ---------------------------
app = QApplication([])
window = QWidget()
main_width, main_height = 800, 600  # початкові розміри головного вікна
window.setWindowTitle("Smart Notes - by stas")
window.resize(main_width,main_height)
window.move(0,0)
window.setStyleSheet('background-color: lightgreen;font-size:15px')

# ---------------------------
#     Eлементи інтерфейсу
# ---------------------------
text_editor = QTextEdit()                                           # Введення тексту замітки
text_editor.setStyleSheet(' background-color:lightblue;')
text_editor.setPlaceholderText('Введіть текст...')

list_widget_1 = QListWidget()                                       # Список заміток
list_widget_1.setStyleSheet('background-color:lightblue')

list_widget_2 = QListWidget()                                       # Список (Контактні дані)
list_widget_2.setStyleSheet('background-color:lightblue')

text_searcher = QLineEdit()                                         # Пошук  по тексту
text_searcher.setPlaceholderText('Введіть текст...')

tag_searcher = QLineEdit()
tag_searcher.setPlaceholderText('Введіть тег...')                   # Пошук  по тегу

# ---------------------------
#      Створення кнопок
# ---------------------------
make_note = QPushButton()
make_note.setStyleSheet('background-color: red; color: blue;')
make_note.setText("Створити замітку")                   

delete_note = QPushButton()
delete_note.setStyleSheet('background-color: red; color: blue;')
delete_note.setText("Видалити замітку")                  

save_note = QPushButton()
save_note.setStyleSheet('background-color: red; color: blue;')
save_note.setText("Зберегти замітку")                  

search_for_text = QPushButton()
search_for_text.setStyleSheet('background-color: yellow; color: red;')
search_for_text.setText("Шукати замітку за текстом")         

search_for_tag = QPushButton()
search_for_tag.setStyleSheet('background-color: yellow; color: red;')
search_for_tag.setText("Шукати замітку за тегом")           

add_to_note = QPushButton()
add_to_note.setStyleSheet('background-color: blue; color: yellow;')
add_to_note.setText("Додати тег до замітки")                   

unpin_to_note = QPushButton()
unpin_to_note.setStyleSheet('background-color: blue; color: yellow;')
unpin_to_note.setText("Відкріпити тег від замітки")


convert_to_txt = QPushButton()
convert_to_txt.setStyleSheet('background-color: green;')
convert_to_txt.setText("Конвертувати до txt-формату")

action_theme_btn = QPushButton()
action_theme_btn.setStyleSheet('background-color: green;')
action_theme_btn.setText("Змінити тему на чорну")

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
col2.addWidget(QLabel("Пошук данних:"))
col2.addWidget(tag_searcher)
col2.addWidget(text_searcher)
col2.addLayout(row2)

# Нижні 3 кнопки
col2.addWidget(search_for_tag)
col2.addWidget(search_for_text)
col2.addWidget(convert_to_txt)
col2.addWidget(action_theme_btn)

# Злиття
layout_note = QHBoxLayout()
layout_note.addLayout(col1)
layout_note.addLayout(col2)

# Макет на екран
window.setLayout(layout_note) 

# ---------------------------------------------------------[ Функціонал програми ]---------------------------------------------------------------------


# ------------------- [ Замітки ] -------------------

#  отримуємо текст із замітки з виділеною назвою та відображаємо його в полі редагування
def show_notes():
    global key                                        # зберігати текст замітки
    key = list_widget_1.selectedItems()[0].text()     # дізнаємось на яку замітку клікнули
    list_widget_2.clear()                             # очищаємо поле із тегами
    text_editor.setText(notes[key]["text"])           # відобразили текст замітки
    list_widget_2.addItems(notes[key]["tag"])         # відобразили теги замітки

#  додаємо нову замітку 
def add_notes():
    note_name,ok = QInputDialog.getText(window,'Додати замітку',"Назва замітки")    # - Створити вікно QInputDialog з назвою note_name і зчитати текст
    if note_name and ok:
        list_widget_1.addItem(note_name)                                            # - Додає замітку до віджету (списку заміток)
        notes[note_name] = {"text":"","tag":[]}                                     # - Додає до списку notes новий обєкт - але з  пустими поки полями
    writeToFile()                                                                   # - Викликаємо фукнцію для запису в Json фалу нові замітки

#  видалити вибрану замітку 
def delete_notes():
    if list_widget_1.currentItem():          # - якщо вибрана замітка
        if key in notes:                     # - і є така замітка в словнику notes (за ключем)
            notes.pop(key)                   # - pop видаляє з словника
            
            text_editor.clear()              # - очищаємо віджети
            list_widget_2.clear()
            list_widget_1.clear()
            list_widget_1.addItems(notes)    # - оновлюємо віджет списку заміток
            writeToFile()                    # - перезаписуємо файл

#  зберегти замітку 
def save_notes():
    if list_widget_1.currentItem():                       # - якщо вибрана замітка
        key = list_widget_1.currentItem().text()          # - отримати назву вибраної замітки
        notes[key]['text'] = text_editor.toPlainText()   # - записати у словник notes з текстом з віджену
        writeToFile()                                     # - перезаписати файл

# шукати по замітці
def search_for_note():

    text_to_search = text_searcher.text()
    if search_for_text.text() == 'Шукати замітку за текстом':
        filtered_notes = {}
        for key, note_data in notes.items():
            if text_to_search in note_data['text']:
                filtered_notes[key] = note_data

        search_for_text.setText('Скинути пошук')
        list_widget_1.clear()
        list_widget_1.addItems(filtered_notes.keys())
        list_widget_2.clear()
        text_editor.clear()

    elif search_for_text.text() == 'Скинути пошук':
        search_for_text.setText('Шукати замітку за текстом')
        list_widget_1.clear()
        list_widget_1.addItems(notes.keys())
        list_widget_2.clear()
        text_editor.clear()

 
# ------------------- [ Теги ] -------------------

# додати тег до нотатки
def add_tag():
    key = list_widget_1.selectedItems()[0].text()                               # Якщо в list_notes обрана замітка

    if key in notes:                                                            # І вона існує в notes
        tag_name, ok= QInputDialog.getText(window,'Додати тег', 'Назва тегу')   # Зчитує тег з поля field_tag
        if tag_name and ok:
            notes[key]["tag"].append(tag_name)                                 # додати тег в notes
            writeToFile()                                                      # перезаписати в файл 

        tag_searcher.clear()                                                   # очистити поле введення тега
        list_widget_2.addItems(notes[key]["tag"])                              # перевивести знову теги

# видалити тег з нотатки
def delete_tag():
    if key in notes:                                                      # Якщо в list_notes обрана замітка
        current_item = list_widget_2.currentItem()                        
        if current_item:
            tag_name = current_item.text()                                # беремо назву тегу
            notes[key]["tag"].remove(tag_name)                            # видаляємо з notes
            list_widget_2.takeItem(list_widget_2.row(current_item))       # видалити цей тег зі списку тегів поточної замітки notes
            writeToFile()                                                 # перезаписуємо в файл 

# пошук по тегу
def search_note_for_tag():

    tag = tag_searcher.text()                                               # Отримуємо текст, введений у поле пошуку тегів
    if search_for_tag.text() == 'Шукати замітку за тегом':                  # Перевіряємо, чи кнопка пошуку по тегу має текст 'Шукати замітку за тегом'
        filtered_notes = {}                                                     # Створюємо словник для збереження відфільтрованих заміток
        for key in notes:                                                       # Перебираємо всі замітки в словнику notes
            if tag in notes[key]['tag']:                                        # Якщо введений тег є в списку тегів замітки
                filtered_notes[key] = notes[key]                                    # Додаємо замітку до відфільтрованих
        search_for_tag.setText('Скинути пошук')                                 # Змінюємо текст кнопки на 'Скинути пошук'

        list_widget_1.clear()
        list_widget_1.addItems(filtered_notes)                              # Додаємо відфільтровані замітки у віджет
        list_widget_2.clear()
        text_editor.clear()

    elif search_for_tag.text() == 'Скинути пошук':                          # Якщо кнопка має текст 'Скинути пошук'
            search_for_tag.setText('Шукати замітку за тегом')               # Змінюємо текст кнопки на 'Шукати замітку за тегом'
            list_widget_1.clear()
            list_widget_1.addItems(notes.keys())                            # Додаємо всі замітки у відже
            list_widget_2.clear()
            text_editor.clear()

# -------------[ Зміна теми та експорт в txt формат ] -------------------

def change_theme():
   
    if action_theme_btn.text() == 'Змінити тему на чорну':

        action_theme_btn.setText('Змінити тему на білу')
        window.setStyleSheet(' background-color:black;color:white;font-size:20px; border: 1px solid white;')
        text_editor.setStyleSheet('background-color:black; color:white;')

        list_widget_1.setStyleSheet(' background-color:black; color:white;')
        list_widget_2.setStyleSheet(' background-color:black; color:white;')
        text_editor.setStyleSheet('background-color:black; color:white;')

        text_searcher.setStyleSheet('background-color:black; color:white;')
        tag_searcher.setStyleSheet('background-color:black; color:white;')

        make_note.setStyleSheet('background-color:black; color:white;')
        delete_note.setStyleSheet('background-color:black; color:white;')
        save_note.setStyleSheet('background-color:black; color:white;')

        search_for_text.setStyleSheet('background-color:black; color:white;')
        search_for_tag.setStyleSheet('background-color:black color:white;')

        add_to_note.setStyleSheet('background-color:black; color:white;')
        unpin_to_note.setStyleSheet('background-color:black; color:white;')
        convert_to_txt.setStyleSheet('background-color:black; color:white;')

        action_theme_btn.setStyleSheet('background-color:black; color:white;')

  

    elif action_theme_btn.text() == 'Змінити тему на білу':

        action_theme_btn.setText('Змінити тему на чорну')
        window.setStyleSheet(' background-color:black;color:white;font-size:20px; border: 1px solid black;')
        text_editor.setStyleSheet('background-color:black; color:black;')


        list_widget_1.setStyleSheet('background-color:white; color:black;')
        list_widget_2.setStyleSheet('background-color:white; color:black;')
        text_editor.setStyleSheet('background-color:white; color:black;')

        text_searcher.setStyleSheet('background-color:white; color:black;')
        tag_searcher.setStyleSheet('background-color:white; color:black;')

        make_note.setStyleSheet('background-color:white; color:black;')
        delete_note.setStyleSheet('background-color:white; color:black;')
        save_note.setStyleSheet('background-color:white; color:black;')

        search_for_text.setStyleSheet('background-color:white; color:black;')
        search_for_tag.setStyleSheet('background-color:white; color:black;')

        add_to_note.setStyleSheet('background-color:white; color:black;')
        unpin_to_note.setStyleSheet('background-color:white; color:black;')
        convert_to_txt.setStyleSheet('background-color:white; color:black;')

        action_theme_btn.setStyleSheet('background-color:white; color:black;')

def export_to_txt():
    if list_widget_1.currentItem():                                                                       # Перевіряємо, чи вибрана замітка у списку
        key = list_widget_1.currentItem().text()                                                          # Витягуємо дані замітки з словника notes за отриманою назвою
        note_data = notes[key]                                                                            # Витягуємо текст з неї
        note_text = note_data['text']                                                                     # Отримуємо текст замітки
        file_dialog = QFileDialog()                                                                       # Викликаємо діалогове вікно для вибору шляху збереження файлу
        file_path, _ = file_dialog.getSaveFileName(window, "Зберегти як .txt", "", "Text Files (*.txt)")

        if file_path:                                                                                      # Якщо шлях збереження був обраний (не пустий)
            with open(file_path, 'w', encoding='utf-8') as txt_file:                                       # Відкриваємо файл для запису в текстовому режимі з кодуванням UTF-8
                txt_file.write("Назва замітки: " )
                txt_file.write(key)
                txt_file.write("\n")
                txt_file.write("Текст замітки: " )
                txt_file.write("\n")
                txt_file.write(note_text)                                                                  # Записуємо текст замітки у файл


# ------------------[ Функція для виходу з програми та зуму ]----------------------

def exit_program():
    app.quit()

def zoom():
    window.resize(1920,1080)

def move_left():
    window.move(500,0)

def move_right():
    window.move(0,0)


# -------------------- [ Скорочення клавіші для виходу ] -----------------
exit_shortcut1 = QShortcut(QKeySequence("Ctrl+Y"), window)
exit_shortcut1.activated.connect(exit_program)



exit_shortcut2 = QShortcut(QKeySequence("Ctrl+E"), window)
exit_shortcut2.activated.connect(zoom)

# ---------------------------------------------------------[ Запуск програми ]---------------------------------------------------------------------

#  підключення обробки подій

make_note.clicked.connect(add_notes)
delete_note.clicked.connect(delete_notes)
save_note.clicked.connect(save_notes)


add_to_note.clicked.connect(add_tag)
unpin_to_note.clicked.connect(delete_tag)
search_for_tag.clicked.connect(search_note_for_tag)
search_for_text.clicked.connect(search_for_note)
convert_to_txt.clicked.connect(export_to_txt)
action_theme_btn.clicked.connect(change_theme)

list_widget_1.itemClicked.connect(show_notes)


# Зчитати файл
with open("notes.json", "r") as file:
    notes = json.load(file)
list_widget_1.addItems(notes) # - відобразити зчитані замітки на віджеті

# --------------------------- Закриття програми та показ
window.show()
app.exec_()
