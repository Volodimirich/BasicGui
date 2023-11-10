from PyQt5.QtWidgets import QMessageBox
from datetime import datetime

def invalid_win():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Current option doesn't implemented just now.")
    msg.setInformativeText('Just now you can use VGG16 approach.')
    msg.setWindowTitle("Not implemented option")
    msg.exec_()


def message_window(window_title, main_message, sup_message=None, msg_icon='Warning'):
    msg_icon_dict = {'Warning': QMessageBox.Warning, 'Critical': QMessageBox.Critical, 'Info': QMessageBox.Information}

    msg = QMessageBox()
    msg.setIcon(msg_icon_dict[msg_icon])

    msg.setText(main_message)
    msg.setWindowTitle(window_title)
    if sup_message:
        msg.setInformativeText(sup_message)

    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()
    
def save_reaction(self):
    if self.style_changed:
        time_stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        np.save(f'{self.pathw.text()}/result_{time_stamp}.npy', self.img3)
        self.style_changed = False

        main_message = "File saved successfully"
        title = 'File Saved'
        message_window(title, main_message, sup_message=None, msg_icon='Info')
    else:
        main_message = "File doesn't created or current file already saved"
        title = 'Save error'
        message_window(title, main_message, sup_message=None, msg_icon='Warning')