import datetime
from PyQt5 import QtCore,QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QStyledItemDelegate
from PyQt5.QtGui import QColor, QBrush

#--- DOC
# self.table_view.currentIndex() - currect cell
#-------------------------------------------------- TableModel
class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data, columns):
        super().__init__()
        self._data = data
        self.headers=columns

    def data(self, index, role):                    
        val = self._data[index.row()][index.column()+1] # +1 - skip id
        if role == Qt.DisplayRole:                              # Get FORMATTED data
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list

            # Perform per-type checks and render accordingly.
            if isinstance(val, datetime.datetime):  # Render date-time
                return val.strftime("%Y-%m-%d %H:%M:%S")
            if isinstance(val, datetime.date):      # Render date
                return val.strftime("%Y-%m-%d")
            elif isinstance(val, float):            # Render float to 2 dp
                #return "%.2f" % val
                return ("%.2f" % val)+"%"
            elif isinstance(val, str):              # Render strings with quotes
                return val # '"%s"' % val
            return val # Default
        
        # if role == Qt.BackgroundRole and index.column() == 2:   # PAINT grid
        # # See below for the data structure.
        #     return QtGui.QColor('blue')
        
    def getId(self,row):
        return self._data[row][0] if len(self._data)>0 else -1
    
    def getData(self,row,col):
        return self._data[row][col]
       
    def setData(self, index, value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self._data[index.row()][index.column()+1] = value
            self.dataChanged.emit(index, index)
            return True
        return False
        
    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:          # column header
            if orientation == Qt.Horizontal:
                return str(self.headers[section])

            if orientation == Qt.Vertical:  # row header
                return str(self.headers.index[section])

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        if len(self._data)==0:
            return 0
        return len(self.headers)
        #return len(self._data[0])-1

class GenderDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        # Return "♂" for True (male) and "♀" for False (female)
        return "♂" if value else "♀"

    def paint(self, painter, option, index):
        value = index.data()
        # Colors are switched: blue for male (True), pink for female (False)
        bright_blue_color = QColor(135, 206, 250)  # LightSkyBlue
        pink_color = QColor(255, 182, 193)  # LightPink
        brush = QBrush(bright_blue_color if value else pink_color)
        painter.fillRect(option.rect, brush)
        super().paint(painter, option, index)

class ResultDelegate(QStyledItemDelegate):
    def displayText(self, value, locale):
        return "yes" if value else "no"

    def paint(self, painter, option, index):
        value = index.data()
        # Custom RGB color for brighter blue
        pink_color = QColor(255, 182, 193)  # LightPink
        bright_blue_color = QColor(154,240,105)  # LightGreen
        brush = QBrush(pink_color if value else bright_blue_color)
        painter.fillRect(option.rect, brush)
        super().paint(painter, option, index)
