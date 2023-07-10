import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class MainWindow(qtw.QWidget):

	def __init__(self , *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.setWindowTitle('')
		self.uiCreateTable();
		self.show();

	def uiCreateMenu(self):
		pass

	def uiCreateTable(self):
		rows = 4
		cols = 3
		table = qtw.QTableWidget(self);
		table.setRowCount(rows);
		table.setColumnCount(cols);
		table.setHorizontalHeaderLabels(['Heading1', 'Heading2', 'Heading3']);
		table.setMinimumHeight(rows*20);
		table.setMinimumWidth(cols*100);


		# set table values
		for row in range(rows):
			for col in range(cols):
				table.setItem(row, col, qtw.QTableWidgetItem(f'Cell {row+1},{col+1}'))

		table.resizeColumnsToContents();
		table.resizeRowsToContents();

		table.show()


if __name__ == '__main__':
	app = qtw.QApplication(sys.argv);

	window = MainWindow()

	sys.exit(app.exec_())
