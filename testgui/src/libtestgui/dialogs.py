

from PyQt6.QtWidgets import QMessageBox


def warn_msg_ok(parent, msg, title=None):
	# dialogs.warn_msg_ok(parent, msg, 'title')
	msg_box = QMessageBox(parent)
	msg_box.setIcon(QMessageBox.Icon.Warning)
	msg_box.setWindowTitle(title)
	msg_box.setText(msg)
	msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
	msg_box.exec()


def error_msg_ok(parent, msg, title=None): # plain error message
	# dialogs.error_msg_ok(msg, 'title')
	msg_box = QMessageBox(parent)
	msg_box.setIcon(QMessageBox.Icon.Warning)
	msg_box.setWindowTitle(title)
	msg_box.setText(msg)
	msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
	msg_box.exec()

def confirm_msg_ok_cancel(parent, msg, title=None):
	# dialogs.confirm_msg_ok_cancle(msg, 'title')
	msg_box = QMessageBox(parent)
	msg_box.setIcon(QMessageBox.Icon.Question)
	msg_box.setWindowTitle(title)
	msg_box.setText(msg)
	msg_box.setStandardButtons(QMessageBox.StandardButton.Ok |
	QMessageBox.StandardButton.Cancel)

	returnValue = msg_box.exec()
	if returnValue == QMessageBox.StandardButton.Ok:
		return True
	else:
		return False


