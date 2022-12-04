from PyQt5 import QtCore
from PyQt5.QtCore import Qt
import pandas as pd

class PandasModel(QtCore.QAbstractTableModel): 
    """
    Class to Moddel TableView of Pandas dictionary 

    Args:
        QtCore (_type_): _description_
    """
    def __init__(self, df = pd.DataFrame(), parent=None): 
        """_summary_

        Args:
            df (pd.DataFrame, optional): datafrane to show . Defaults to pd.DataFrame().
            parent (_type_, optional): widget . Defaults to None.
        """
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df
        
    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        """_
        Function to create header 
        """
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.iloc[index.row(), index.column()]))

    def setData(self, index, value, role):
        """_function to set values based of index and columns 
        """
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        """Function to return row count of a table from dataframe

        Args:
            parent (_type_, optional): _description_. Defaults to QtCore.QModelIndex().

        Returns:
            int: row count
        """
        return self._df.shape[0]

    def columnCount(self, parent=QtCore.QModelIndex()): 
        """Function to return column count of a table from dataframe

        Args:
            parent (_type_, optional): _description_. Defaults to QtCore.QModelIndex().

        Returns:
            int: columncount
        """
        return self._df.shape[1]

    def sort(self, column, order):
        """Sorting Function """
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()
        
        
class DictionaryTableModel(QtCore.QAbstractTableModel):
    """
    Class to Model Dictionary as TableView


    """
    def __init__(self, data, headers):
        """_summary_

        Args:
            data (_type_): list of dictionary (transaction_dict)
            headers (_type_): ['item_name','item_amount','price_per_item']
        """
        super(DictionaryTableModel, self).__init__()
        self._data = data
        self._headers = headers

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # Look up the key by header index.
            column = index.column()
            column_key = self._headers[column]
            return self._data[index.row()][column_key]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The length of our headers.
        return len(self._headers)

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._headers[section])

            if orientation == Qt.Vertical:
                return str(section)