

# Cashier App with PyQt5 

## Problems 
Pendirian Supermarket terbaru mengusung konsep self-service sehingga diperlukan adanya sistem kasir yang dapat membantu pelanggan




## Requirements / Workflow 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/WorkFlow.png)
Main Screen 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/main_screen.PNG)
1. Input Transaksi 
   Detail yang diinput : 
   a. Item Name 
   b. Item Quantity 
   c. Item Price 
   ![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test1_a.PNG)

Jika terdapat transaksi yang ingin di ubah bisa ke Menu Update Item 
2. Update Item 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/update.png)
Jika akan mengupdate nama saja , cukup isi di bagian 1 kemudian update nama. 
Jika akan mengupdate quantity -> isi nama item, Update Jumlah di bagian 2 kemudian klik Update Qty 
Jika akan mengupdate price -> isi nama item, Update Harga di bagian 3 kemudian klik Update Price 

Jika terdapat item yang ingin di hapus bisa ke Menu Delete Item  
3. Delete Item 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/Delete%20Item.PNG)

Delete Salah Satu Item : Masukan Nama Item yang akan dihapus di kolom Item yang dihapus, kemudian klik Delete. 
Jika Ingin Menghapus semua Transaksi Klik Delete All 

Setelah tidak ada update / Delete Bisa ke Menu Check Order untuk mengecek apakah detail sudah benar 
4. Check Order 
Klik Show Order untuk memunculkan recap Order
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/Show%20Order%20Click.jpg)
Jika Order Terdapat Salah , akan muncul 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/CheckOrder_Salah.PNG)
Terdapat Kesalahan pada Item Ayam karena quantity diisi bukan dengan angka, melainkan 'satu', Klik Update Item untuk langsung ke page Update 
Kemudian setelah diperbaiki dan CheckOrder Ulang 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/CheckOrder_Benar.PNG)
5. Calculate Total Order
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/ShowTotal.jpg)
Klik Show Order , kemudian akan muncul total yang perlu dibayar : 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/assets/TotalOrder.PNG)



## Test Case 

### Test 1 
Add Item : item_name : Ayam Goreng , item_qty : 2 , price_per_item : 20000

![image](https://github.com/fakhrirobi/cashier_app/raw/main/test_result/Test1_a.PNG)
Result : 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test1_a_Result.PNG)


Add Item : item_name : Pasta Gigi , item_qty : 3, price_per_item : 15000

![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test1_b.PNG)
Result : 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test1_b_Result.PNG)


Add Item : item_name : Ayam Goreng , item_qty : 2 , price_per_item : 20000
### Test 2 
Delete Item : Pasta Gigi 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test2.PNG)
Result : 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test2_Result.PNG)

### Test 3 
Reset Transaction
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test3.PNG)
Result : 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test3_Result.PNG)

### Test 4 
Total Price

Result : 
![image](https://raw.githubusercontent.com/fakhrirobi/cashier_app/main/test_result/Test4_Result.PNG)


## Cara Menjalankan
1. Clone Project
```python
git clone https://github.com/fakhrirobi/cashier_app.git
```
2.ke folder clone
```python
cd cashier_app 
```
3. Jalankan src/interface.py
```python
python src/interface.py
```

## Presentation 
Youtube : 








