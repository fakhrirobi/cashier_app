import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog, QVBoxLayout, QWidget,QPushButton
from datetime import datetime
from PyQt5 import *
from PyQt5 import QtCore

from src.table_model import PandasModel,DictionaryTableModel
from src.transaction import Transaction
transaction_details = Transaction()

class Functionality : 
    """
        Class to inherit Functionality for creating QTableView Data in QDialog Class
    """ 
    def generate_data(self,transaction_details=transaction_details) : 
        data = [transaction_details.transaction_dict[x] for x in transaction_details.transaction_dict.keys()]
        headers = ['item_name','item_amt','price_per_item']
        return [data,headers]
    
class MainScreen(QDialog,Functionality):
    """
    Main Menu Screen 
    """
    def __init__(self):
        super(MainScreen, self).__init__()
        # Load Ui File from QtDesigner
        loadUi("ui_file/main_menu.ui",self)
        # Routing from each Button Clicked to Other Screen  to Know Object Button Name , need to open *.ui file and inspect with pyqtdesigner
        self.InputItem.clicked.connect(self.InputItemTrigger) # Input Item Screen 
        self.UpdateItem.clicked.connect(self.UpdateItemTrigger) # UpdateItem Screen 
        self.DeleteItem.clicked.connect(self.DeleteItemTrigger)# Delete Item Screen 
        self.CheckOrder.clicked.connect(self.CheckOrderTrigger)# CheckOrder Screen 
        self.CalculateOrder.clicked.connect(self.CalculateOrderTrigger) # Calculate Order Screen 
    

        
    def InputItemTrigger(self):
        """
        Function that was triggereed from button click from main screen , to init Input Screen 
        """
        inputitemscreen = InputItemScreen()
        widget.addWidget(inputitemscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def DeleteItemTrigger(self):
        """
        Function that was triggereed from button click from main screen , to init Delete Screen 
        """
        deletescreen = DeleteItemScreen()
        widget.addWidget(deletescreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def UpdateItemTrigger(self):
        """
        Function that was triggereed from button click from main screen , to init Update Screen 
        """
        update = UpdateItemScreen()
        widget.addWidget(update)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def CheckOrderTrigger(self):
        """
        Function that was triggereed from button click from main screen , to init CheckOrder Screen 
        """
        checkorderscreen = CheckOrderScreen()
        widget.addWidget(checkorderscreen)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def CalculateOrderTrigger(self):
        """
        Function that was triggereed from button click from main screen , to init CalculateOrder Screen 
        """
        calculateorder = CalculateTotalOrderScreen()
        widget.addWidget(calculateorder)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
class InputItemScreen(QDialog,Functionality) : 
    
    def __init__(self):
        super(InputItemScreen, self).__init__()
        loadUi("ui_file/InputItem.ui",self)
        self.toMainMenu.clicked.connect(self.backtomenu)
        self.SaveInput.clicked.connect(self.save_input)
    

                    



    def backtomenu(self) : 
        main_menu = MainScreen()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
    def save_input(self) : 
        try : 
            item_name = self.ItemNameBox.text()
            item_qty = self.ItemQtyBox.text()
            item_price = self.ItemPriceBox.text()
            
            # self.ItemNameBox.editingFinished.connect(self.process_item_name.checkstatus)
            # self.ItemQtyBox.editingFinished.connect(self.process_item_qty.checkstatus)
            # self.ItemPriceBox.editingFinished.connect(self.process_item_price.checkstatus)
            if (item_name != '') & (item_qty != '') & (item_price != '') : 
                transaction_details.add_item(item_name=item_name,
                                            item_amount=item_qty,
                                            price_per_item=item_price)
                self.ItemNameBox.clear()
                self.ItemQtyBox.clear()
                self.ItemPriceBox.clear()
                self.Status.setText(f'Berhasil Menambahkan Item {transaction_details.transaction_dict.get(item_name)}')
            
                
                
            else : 
                raise ValueError('Nama Barang/Jumlah Item/Harga tidak boleh kosong')

            
            

            
            
        except BaseException as error : 
            self.Status.setText(str(error))
        

            
        # empty the boxes 
        # self.ItemNameBox.clear()
        # self.ItemQtyBox.clear()
        # self.ItemPriceBox.clear()
        # self.Status.clear()
        
class UpdateItemScreen(QDialog,Functionality) : 
    def __init__(self):
        super(UpdateItemScreen, self).__init__()
        loadUi("ui_file/UpdateItem.ui",self)
        #on Click Command
        self.toMainMenu.clicked.connect(self.backtomenu)
        self.SaveUpdateName.clicked.connect(self.save_item_name)
        self.SaveUpdateQty.clicked.connect(self.save_item_qty)
        self.SaveUpdatePrice.clicked.connect(self.save_item_price)

        self.model = DictionaryTableModel(*self.generate_data())
        self.ItemTable.setModel(self.model)

    #on Click Function 
    def backtomenu(self) : 
        main_menu = MainScreen()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
    def save_item_name(self) : 
        try : 
            item_name = self.ItemNameBox.text()
            new_name = self.ItemNameBoxUpdate.text()
            if (item_name!='') & (new_name!=''): 
                transaction_details.update_item_name(old_name=item_name,new_name=new_name)
                self.Status.setText('Berhasil Mengubah Nama Item, dari {} menjadi {}'.format(item_name,new_name))


                self.model = DictionaryTableModel(*self.generate_data())
                self.ItemTable.setModel(self.model)
            else : 
                raise ValueError('Nama Item Lama / Baru tidak boleh kosong')
            
        except BaseException as error : 
            self.Status.setText(str(error))
        finally : 

            self.Status.clear()
            self.ItemNameBox.clear()
            self.ItemNameBoxUpdate.clear()
    
    def save_item_qty(self) : 
        try : 
            item_name = self.ItemNamePriceQtyBox.text()
            new_qty = self.ItemQtyBox.text()
            if (item_name!='') & (new_qty!='') : 
                #save update 
                
                transaction_details.update_item_qty(item_name=item_name,new_qty=new_qty)
                self.model = DictionaryTableModel(*self.generate_data())
                self.ItemTable.setModel(self.model)
                self.Status.setText(f'Berhasil Mengupdate  Quantity Item, {item_name}')

            else : 
                raise ValueError('Nama Item/Quantity Tidak Boleh Kosong')
            
        except BaseException as error : 
            self.Status.setText(str(error))
        
        self.Status.clear()
        self.ItemNamePriceQtyBox.clear()
    
    def save_item_price(self) : 
        
        try : 
            item_name = self.ItemNamePriceQtyBox.text()
            new_price = self.ItemPriceBox.text()
            
            #check if item


            
            if (item_name!='') & (new_price!='')   : 
                
                transaction_details.update_item_price(item_name=item_name,new_price=new_price)
                self.model = DictionaryTableModel(*self.generate_data())
                self.ItemTable.setModel(self.model)

                self.Status.setText(f'Berhasil Mengupdate Harga Item {item_name}')
                
                
                
            else : 
                    raise ValueError('Nama Item/Quantity Tidak Boleh Kosong')
                

        except BaseException as error : 
            self.Status.setText(str(error))
            
        self.Status.clear()
        self.ItemPriceBox.clear()
        # empty the boxes 

        
class DeleteItemScreen(QDialog,Functionality) : 
    def __init__(self):
        super(DeleteItemScreen, self).__init__()
        loadUi("ui_file/DeleteItem.ui",self)
        self.toMainMenu.clicked.connect(self.backtomenu)
        self.DeleteSingleItem.clicked.connect(self.delete_single)
        self.DeleteAll.clicked.connect(self.delete_all)
        self.model = DictionaryTableModel(*self.generate_data())
        self.ItemTable.setModel(self.model)
    def backtomenu(self) : 
        main_menu = MainScreen()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
    def delete_single(self) : 

        try : 
            item_name = self.ItemNameBox.text()
            if item_name != '' : 
                transaction_details.delete_item(item_name=item_name)
                self.Status.setText('Berhasil Menghapus Item {}'.format(item_name))
                self.model = DictionaryTableModel(*self.generate_data())
                self.ItemTable.setModel(self.model)
            else : 
                raise ValueError('Item yang akan dihapus tidak boleh kosong')
            
        except BaseException as error : 
            self.Status.setText(str(error))
        # empty the boxes 
        self.ItemNameBox.clear()
            
            
    def delete_all(self) : 
        try : 
            transaction_details.delete_all()
            self.model = DictionaryTableModel(*self.generate_data())
            self.ItemTable.setModel(self.model)
            self.Status.setText('Berhasil Menghapus Semua Transaksi ')
        except BaseException as error : 
            self.Status.setText(str(error))
        

            
class CheckOrderScreen(QDialog,Functionality) : 
    def __init__(self):
        super(CheckOrderScreen, self).__init__()
        loadUi("ui_file/CheckOrder.ui",self)
        self.toMainMenu.clicked.connect(self.backtomenu)
        self.ShowOrder.clicked.connect(self.order_recap)
    def backtomenu(self) : 
        main_menu = MainScreen()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
    def goToUpdateItem(self) : 
        update_screen = UpdateItemScreen()
        widget.addWidget(update_screen)
        widget.setCurrentIndex(widget.currentIndex()+1) 
        
    def order_recap(self) : 
        #run order check , validate data type 
        try : 


            self.model = DictionaryTableModel(*self.generate_data())
            self.ItemTable.setModel(self.model)

            transaction_details.check_order()
            self.Status.setText('Pesanan Sudah Benar')
            
            self.model = PandasModel(transaction_details.total_df)
            self.ItemTable.setModel(self.model)
        except BaseException as error : 
            self.Status.setText(str(error))
                        
            
            self.to_update_screen_btn = QPushButton('Update Item')
            self.to_update_screen_btn.move(120,400)
            style_sheet = '''
            
                            QPushButton::active {
                            background-color :  #85eda1;
                            border-radius : 25px;
                            }
                            QPushButton::hover{
                            background-color : #85c5ed;
                            }

                            QPushButton::pressed{
                            background-color : #85c5ed;
                            }
            '''
            self.to_update_screen_btn.setStyleSheet(style_sheet)
            self.to_update_screen_btn.setFixedSize(171,51)
            self.to_update_screen_btn.clicked.connect(self.goToUpdateItem)
            self.gridLayout.addWidget(self.to_update_screen_btn)

            
class CalculateTotalOrderScreen(QDialog,Functionality) : 
    def __init__(self):
        super(CalculateTotalOrderScreen, self).__init__()
        loadUi("ui_file/TotalOrder.ui",self)
        self.toMainMenu.clicked.connect(self.backtomenu)
        self.ShowOrder.clicked.connect(self.order_recap)
    def backtomenu(self) : 
        main_menu = MainScreen()
        widget.addWidget(main_menu)
        widget.setCurrentIndex(widget.currentIndex()+1) 
    def order_recap(self) : 
        model = PandasModel(transaction_details.total_df)
        self.dataframeView.setModel(model)
        price,discount = transaction_details.total_price()
        text = 'Total Pembayaran : Rp{:,.2f}, Selamat anda mendapatkan diskon sebesar {}%'.format(price,round(discount*100,2))
        self.OrderRecap.setText(text)


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    welcome = MainScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(1000)
    widget.setFixedWidth(800)
    widget.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")