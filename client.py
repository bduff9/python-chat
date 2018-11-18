from PySide2.QtCore import *
from PySide2.QtWidgets import *

import requests

name = 'Duff' # Enter your name here!
chat_url = 'https://build-system.fman.io/chat'

# GUI:
app = QApplication([])
text_area = QTextEdit()
text_area.setFocusPolicy(Qt.NoFocus)
message = QLineEdit()
layout = QVBoxLayout()
layout.addWidget(text_area)
layout.addWidget(message)
window = QWidget()
window.setLayout(layout)
window.show()

# Event handlers:
def refresh_messages():
    """ Testing doc string """
    text_area.setHtml(requests.get(chat_url).text)

def send_message():
    requests.post(chat_url, {'name': name, 'message': message.text()})
    message.clear()

# Signals:
message.returnPressed.connect(send_message)
timer = QTimer()
timer.timeout.connect(refresh_messages)
timer.start(1000)

app.exec_()
