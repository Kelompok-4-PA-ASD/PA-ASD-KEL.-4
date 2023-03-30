import os
import time
import json
from prettytable import PrettyTable
os.system('cls')

# with open('log.json') as file:
#     data_login = json.load(file)
data_login = {
    "nabil1": {
      "nama": "Nabil",
      "pin": "09876"
    }
  }

tabel = PrettyTable()
tabel.field_names = ["No.","Jam","Tujuan","Nomor Kereta"]
class linkedList:
    class Node:
        def __init__(self,jam,tujuan,nomor, nextNode = None, prevNode = None):
            self.next = nextNode
            self.prev = prevNode
            self.jam = jam
            self.tujuan = tujuan
            self.nomor = nomor

    def __init__(self):
        self.head = None
        self.history = []
    
    def length(self):
        pointer = self.head
        length = 0
        while pointer is not None:
            length += 1
            pointer = pointer.next
        return length

    def view(self):
        if self.head == None:
            print("\nJADWAL KOSONG\n")
            Q()
        else:
            kolom = mylist.head
            tabel.clear_rows()
            num = 1
            while kolom:
                tabel.add_row([num,kolom.jam,kolom.tujuan,kolom.nomor])
                kolom = kolom.next
                num += 1
            print(tabel.get_string())

    def viewHistory(self):
        if self.history == []:
            print("\nHISTORI KOSONG\n")
        else:
            h = self.head
            histori = PrettyTable()
            histori.field_names = ["No.","Riwayat"]
            for i,riwayat in enumerate(self.history):
                histori.add_row([i+1,riwayat])
            histori.align = "l"
            print(histori)

    def addFirst(self, jam,tujuan,nomor):
        self.history.append(f'Menambah | {jam} | {tujuan} | {nomor} | di awal list')
        newNode = self.Node(jam,tujuan,nomor)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def addEnd(self,jam,tujuan,nomor):
        self.history.append(f'Menambah | {jam} | {tujuan} | {nomor} | di akhir list')
        newNode = self.Node(jam,tujuan,nomor)
        if self.head == None:
            self.addFirst(jam,tujuan,nomor)
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = newNode
            newNode.prev = pointer

    def UpdateJam(self,position,newValue):
        pointer = self.head
        for i in range(1, position):
            if pointer is None:
                break
            pointer = pointer.next
        if pointer is None:
            print(f'Nomor urut {position} tidak ditemukan. Silahkan coba lagi')
            return 0
        self.history.append(f'Mengubah jam | {pointer.jam} | menjadi | {newValue} |')
        pointer.jam = newValue
        print("Jadwal telah diperbarui")
        return 1

    def UpdateTujuan(self,position,newValue):
        pointer = self.head
        for i in range(1, position):
            if pointer is None:
                break
            pointer = pointer.next
        if pointer is None:
            print(f'Nomor urut {position} tidak ditemukan. Silahkan coba lagi')
            return 0
        self.history.append(f'Mengubah tujuan | {pointer.tujuan} | menjadi | {newValue} |')
        pointer.tujuan = newValue
        print("Jadwal telah diperbarui")
        return 1

    def UpdateNomor(self,position,newValue):
        pointer = self.head
        for i in range(1, position):
            if pointer is None:
                break
            pointer = pointer.next
        if pointer is None:
            print(f'Nomor urut {position} tidak ditemukan. Silahkan coba lagi')
            return 0
        self.history.append(f'Mengubah nomor kereta | {pointer.nomor} | menjadi | {newValue} |')
        pointer.nomor = newValue
        print("Jadwal telah diperbarui")
        return 1
        

    def delete(self, position):
        if self.head is None:
            print('\n JADWAL KOSONG \n')
        temp = self.head
        if position == 1:
            self.head = temp.next
            if self.head is not None:
                self.head.prev = None
            temp = None
            return 1 
 
        for i in range(1, position):
            if temp is None:
                break
            temp = temp.next

        self.history.append(f'Mengahapus | {temp.jam} | {temp.tujuan} | {temp.nomor} | dari tabel')
        print(f'Menghapus | {temp.jam} | {temp.tujuan} | {temp.nomor} | \n')
        if temp is None:
            return 0
        if temp.next is not None:
            temp.next.prev = temp.prev
        if temp.prev is not None:
            temp.prev.next = temp.next
        temp = None
    
        time.sleep(1)
        return 1         

mylist = linkedList()
mylist.addFirst('08:00','JAKARTA','KA123')
mylist.addEnd('09:30','SURABAYA','KA456')
mylist.addEnd('10:45','YOGYAKARTA','KA789')
mylist.addEnd('12:15','BANDUNG','KA321')
mylist.addEnd('13:30','SOLO','KA654')
mylist.addEnd('14:45','MALANG','KA987')
mylist.addEnd('16:00','SURABAYA','KA135')
mylist.addEnd('18:00','BANDUNG','KA468')
mylist.addEnd('19:30','JAKARTA','KA246')
mylist.addEnd('21:00','BANDUNG','KA753')

def Q():
    tanya = input('\nKe menu utama? [y/t]: ').lower()
    while tanya not in ["y","t"]:
        print("Pilih jawaban yang tersedia")
        tanya = input('[y/t]: ').lower()
    if tanya == 'y':
        main()
    elif tanya == 't':
        print("\n    TERIMA KASIH\n\n")
        exit()

def main():
    os.system('cls')
    print('\nJADWAL KEBERANGKATAN STASIUN TUGU')
    print('[1] Tampilkan Jadwal')
    print('[2] Tambahkan Data Di Awal')
    print('[3] Tambahkan Data Di Akhir')
    print('[4] Perbarui Data')
    print('[5] Hapus data')
    print('[6] Histori')

    ask = input('Pilih: ')
    while ask not in ['1','2','3','4','5','6']:
        print('Pilih dari pilihan yang tersedia')
        ask = input('Pilih: ')
        
    if ask == '1':
        print("Memproses...")
        time.sleep(1)
        os.system('cls')
        print('        JADWAL KEBERANGKATAN KERETA')
        mylist.view()

    elif ask == '2':
        print("Memproses...")
        time.sleep(1)
        os.system('cls')
        print('      MENAMBAHKAN JADWAL KEBERANGKATAN')
        mylist.view()
        print('\nData akan ditambahkan pada No.1')
        arv = input('Jam Keberangkatan\t: ')
        des = input('Tujuan\t\t\t: ').upper()
        num = input('Nomor Kereta\t\t: ').upper()
        mylist.addFirst(arv,des,num)
        print('Data telah ditambahkan\n')
        mylist.view()

    elif ask == '3':
        print("Memproses...")
        time.sleep(1)
        os.system('cls')
        print('      MENAMBAHKAN JADWAL KEBERANGKATAN')
        mylist.view()
        print(f'\nData akan ditambahkan pada No.{mylist.length()+1}')
        arv = input('Jam Keberangkatan\t: ')
        des = input('Tujuan\t\t\t: ').upper()
        num = input('Nomor Kereta\t\t: ').upper()
        mylist.addEnd(arv,des,num)
        print('Data telah ditambahkan\n')
        mylist.view()

    elif ask == '4':
        print("Memproses...")
        time.sleep(1)
        os.system('cls')
        print('MEMPERBARUI JADWAL KEBERANGKATAN')
        print('\nData yang ingin perbarui')
        print('[1] Jam Keberangkatan')
        print('[2] Tujuan Keberangkatan')
        print('[3] Nomor Kereta')
        
        tanya = input('Pilih: ')
        while tanya not in ['1','2','3']:
            print('Pilih dari pilihan yang tersedia')
            tanya = input('Pilih: ')

        if tanya == '1':
            print("Memproses...")
            time.sleep(1)
            os.system('cls')
            print('        MEMPERBARUI JAM KEBERANGKATAN')
            mylist.view()
            while True:
                while True:
                    try:
                        pos = int(input('\nNo. Urut\t: '))
                        break
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")

                new = input('Jam Baru\t: ').upper()
                if mylist.UpdateJam(pos,new) == 1:
                    break
            print('')
            mylist.view()

        elif tanya == '2':
            print("Memproses...")
            time.sleep(1)
            os.system('cls')
            print('        MEMPERBARUI TUJUAN KERETA')
            mylist.view()
            while True:
                while True:
                    try:
                        pos = int(input('\nNo. Urut\t: '))
                        break
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")

                new = input('Tujuan Baru\t: ').upper()
                if mylist.UpdateTujuan(pos,new) == 1:
                    break
            print('')
            mylist.view()


        elif tanya == '3':
            print("Memproses...")
            time.sleep(1)
            os.system('cls')
            print('        MEMPERBARUI NOMOR KERETA')
            mylist.view()
            while True:
                while True:
                    try:
                        pos = int(input('\nNo. Urut\t: '))
                        break
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")
                new = input('Nomor Baru\t: ').upper()
                if mylist.UpdateNomor(pos,new) == 1:
                    break
            print('')
            mylist.view()

    elif ask == '5':
        print("Memproses...")
        time.sleep(1)
        os.system('cls')
        print("       MENGHAPUS JADWAL KEBERANGKATAN")
        mylist.view()
        while True:
            while True:
                try:
                    x = int(input('\nData yang ingin dihapus: '))
                    break
                except ValueError:
                    print("Input harus berupa angka. Silakan coba lagi.")
            if mylist.delete(x) == 1 :
                print('Data telah dihapus')
                mylist.view()
                break
            else:
                print(f'Nomor urut {x} tidak ditemukan. Silahkan coba lagi')
                
    elif ask == '6':
        print("Memproses...")
        time.sleep(1)
        os.system('cls')
        print("HISTORI PERUBAHAN TERHADAP JADWAL")
        mylist.viewHistory()
    Q()

def aks():
    tany = input("Kembali ke menu utama? [y/t]").lower()
    while tany not in ["y","t"]:
        print("Pilihan tidak tersedia, mohon coba lagi")
        tany = input("Kembali ke menu utama? [y/t]").lower()
    if tany == "y":
        start()
    else:
        exit()

def login():
    usr = input('Masukkan username: ')
    pin = input('Masukkan PIN: ')

    if usr in data_login and data_login[usr]["pin"] == pin:
        print("Log-In Berhasil")
        print("Selamat Datang", data_login[usr]["nama"])
        return 1
    else:
        print("Username dan Password salah, Mohon coba lagi")
        aks()

def addUsr():
    name = input('\nNama anda: ')
    username = input('Username baru: ')
    pin = input('PIN baru: ')
    data_login[username] = {"nama": name, "pin": pin}

    with open('log.json', 'w') as file:
        json.dump(data_login, file,indent = 2)

    print('Akun', username, 'telah berhasil ditambahkan.')
    return


def start():
    print("[1] Log-In")
    print("[2] Buat Akun")
    
    ask = input("Pilih: ")
    while ask not in ["1","2"]:
        print("Pilihan tidak tersedia, mohon coba lagi")
        ask = input("Pilih: ")

    if ask == "1":
        if login() == 1:
            main()

    if ask == "2":
        addUsr()
        aks()

start()
