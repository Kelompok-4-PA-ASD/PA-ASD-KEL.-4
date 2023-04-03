import os
import math
import time
from prettytable import PrettyTable
os.system('cls')

tabel = PrettyTable()
tabel.field_names = ["No.","Jam","Tujuan","Nomor Kereta","Penumpang"]

class Node:
    def __init__(self,jam,tujuan,nomor,penumpang, nextNode = None, prevNode = None):
        self.next = nextNode
        self.prev = prevNode
        self.jam = jam
        self.tujuan = tujuan
        self.nomor = nomor
        self.penumpang = penumpang

class linkedList:
    def __init__(self):
        self.head = None
        self.history = []
    
    def length(self):
        length = 0
        pointer = self.head
        while pointer is not None:
            length += 1
            pointer = pointer.next
        return length

    
    def view(self):
        if self.head == None:
            print('+-----------------------------------------------------+')
            print('|                    JADWAL KOSONG                    |')
            print('+-----------------------------------------------------+')
            Q()
        else:
            kolom = mylist.head
            tabel.clear_rows()
            num = 1
            while kolom:
                tabel.add_row([num,kolom.jam,kolom.tujuan,kolom.nomor,kolom.penumpang])
                kolom = kolom.next
                num += 1
            print(tabel.get_string())

    def viewHistory(self):
        if self.history == []:
            print("\n    HISTORI KOSONG\n\n")
        else:
            h = self.head
            histori = PrettyTable()
            histori.field_names = ["No.","Riwayat"]
            for i,riwayat in enumerate(self.history):
                histori.add_row([i+1,riwayat])
            histori.align = "l"
            print(histori)

    def addFirst(self, jam,tujuan,nomor,penumpang):
        self.history.append(f'Menambah | {jam} | {tujuan} | {nomor} | {penumpang} | di awal list')
        newNode = Node(jam,tujuan,nomor,penumpang)
        if self.head == None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def addEnd(self,jam,tujuan,nomor,penumpang):
        self.history.append(f'Menambah | {jam} | {tujuan} | {nomor} | {penumpang} | di akhir list')
        newNode = Node(jam,tujuan,nomor,penumpang)
        if self.head == None:
            self.head = newNode
        else:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = newNode
            newNode.prev = pointer

    def Update(self,position,newValue,elemen):
        pointer = self.head
        if position >= 1:
            for i in range(1, position):
                if pointer is None:
                    break
                pointer = pointer.next
            if pointer is None:
                print(f'Nomor urut {position} tidak ditemukan. Silahkan coba lagi')
                return 0
            if elemen == 1:
                pointer.jam = newValue
                self.history.append(f'Mengubah nomor kereta | {pointer.jam} | menjadi | {newValue} |')
            elif elemen == 2:
                pointer.tujuan = newValue
                self.history.append(f'Mengubah nomor kereta | {pointer.tujuan} | menjadi | {newValue} |')
            elif elemen == 3:
                pointer.nomor = newValue
                self.history.append(f'Mengubah nomor kereta | {pointer.nomor} | menjadi | {newValue} |')
            elif elemen == 4:
                pointer.penumpang = newValue
                self.history.append(f'Mengubah nomor kereta | {pointer.penumpang} | menjadi | {newValue} |')
            print("Jadwal telah diperbarui")
            return 1
        else:
            print(f'Nomor urut {position} tidak ditemukan. Silahkan coba lagi')
            return 0
        
    def delete(self, position):
            if self.head is None:
                print('+-----------------------------------------------------+')
                print('|                    JADWAL KOSONG                    |')
                print('+-----------------------------------------------------+')
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
            time.sleep(0.5)
            return 1

    
    def mergeSort(self, head,elemen):
        if not head or not head.next:
            return head
        mid = self.getMiddle(head)
        next_to_mid = mid.next
        mid.next = None
        left = self.mergeSort(head,elemen)
        right = self.mergeSort(next_to_mid,elemen)
        sorted_lst = self.merge(left, right,elemen)
        return sorted_lst
        
    def getMiddle(self, head):
        if not head:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    def merge(self, left, right,elemen):
        if not left:
            return right
        if not right:
            return left
        if elemen ==1 :
            x = left.jam
            y = right.jam
        elif elemen == 2:
            x = left.tujuan
            y = right.tujuan
        elif elemen == 3:
            x = left.nomor
            y = right.nomor
        elif elemen == 4:
            x = left.penumpang
            y = right.penumpang
        if x <= y:
            result = left
            result.next = self.merge(left.next, right,elemen)
        else:
            result = right
            result.next = self.merge(left, right.next,elemen)
        return result
    
    def jump_search_task(self, description):
        n = 0
        current = self.head
        while current:
            n += 1
            current = current.next

        step = int(math.sqrt(n))
        prev = None
        current = self.head
        while current and current.tujuan < description:
            prev = current
            for i in range(step):
                current = current.next
                if not current:
                    break

        if prev and prev.tujuan == description:
            print(prev.jam, prev.tujuan, prev.nomor, prev.penumpang)
            # return prev
            
        elif current and current.tujuan == description:
            print(current.jam, current.tujuan, current.nomor, current.penumpang)
            # return current
        else:
            return None
        
        
mylist = linkedList()
mylist.addFirst('18:00','JAKARTA','KA123',221)
mylist.addEnd('09:30','SURABAYA','KA456',142)
mylist.addEnd('14:45','YOGYAKARTA','KA789',52)
mylist.addEnd('12:15','BANDUNG','KA321',341)
mylist.addEnd('18:30','SOLO','KA654',122)
mylist.addEnd('10:45','MALANG','KA987',194)
mylist.addEnd('16:00','SURABAYA','KA135',123)
mylist.addEnd('11:00','SEMARANG','KA468',342)
mylist.addEnd('19:30','JAKARTA','KA246',129)
mylist.addEnd('13:00','BANDUNG','KA753',172)

def Q():
    tanya = input('\nKe menu utama? [y/t]: ').lower()
    while tanya not in ["y","t"]:
        print("Pilih jawaban yang tersedia")
        tanya = input('[y/t]: ').lower()
    if tanya == 'y':
        main()
    elif tanya == 't':
        x = 50*"-"
        print(x,"TERIMA KASIH",x)
        exit()

def main():
    os.system('cls')
    print('\n+-----------------------------------+')
    print('| JADWAL KEBERANGKATAN STASIUN TUGU |')
    print('+-----------------------------------+')
    print('|     [1] Tampilkan Jadwal          |')
    print('|     [2] Mengurutkan Jadwal        |')
    print('|     [3] Tambahkan Data Di Awal    |')
    print('|     [4] Tambahkan Data Di Akhir   |')
    print('|     [5] Perbarui Data             |')
    print('|     [6] Hapus data                |')
    print('|     [7] Histori                   |')
    print('+-----------------------------------+')

    ask = input('Pilih: ')
    while ask not in ['1','2','3','4','5','6','7','8']:
        print('Pilih dari pilihan yang tersedia')
        ask = input('Pilih: ')
        
    if ask == '1':
        print("Memproses...")
        time.sleep(0.5)
        os.system('cls')
        print('+-----------------------------------------------------+')
        print('|            JADWAL KEBERANGKATAN KERETA              |')
        print('+-----------------------------------------------------+')
        mylist.view()

    elif ask == '2':
        print("Memproses...")
        time.sleep(0.5)
        os.system('cls')
        print('+---------------------------------------+')
        print('|       MENGURUTKAN JADWAL KERETA       |')
        print('+---------------------------------------+')
        print('|    Jadwal Diurutkan berdasarkan :     |')
        print('|    [1] Jam Keberangkatan              |')
        print('|    [2] Tujuan Keberangkatan           |')
        print('|    [3] Nomor Kereta                   |')
        print('|    [4] Jumlah Penumpang               |')
        print('+---------------------------------------+')
        print
        ask = input("Pilih: ")
        while ask not in ['1','2','3','4']:
            print("Pilih dari pilihan yang tersedia, mohon coba lagi")
            ask = input(": ")
        if ask == '1':
            print('+-----------------------------------------------------+')
            print('|             MENGURUTKAN BERDASARKAN JAM             |')
            print('+-----------------------------------------------------+')
            mylist.head = mylist.mergeSort(mylist.head,1)
        if ask == '2':
            print('+-----------------------------------------------------+')
            print('|           MENGURUTKAN BERDASARKAN TUJUAN            |') 
            print('+-----------------------------------------------------+')
            mylist.head = mylist.mergeSort(mylist.head,2)
        if ask == '3':
            print('+-----------------------------------------------------+')
            print('|         MENGURUTKAN BERDASARKAN NOMOR KERETA        |')
            print('+-----------------------------------------------------+')
            mylist.head = mylist.mergeSort(mylist.head,3)
        if ask == '4': 
            print('+-----------------------------------------------------+')
            print('|          MENGURUTKAN BERDASARKAN PENUMPANG          |')
            print('+-----------------------------------------------------+')
            mylist.head = mylist.mergeSort(mylist.head,4)
        mylist.view()

    elif ask == '3':
        print("Memproses...")
        time.sleep(0.5)
        os.system('cls')
        print('+-----------------------------------------------------+')
        print('|       MENAMBAH JADWAL KEBERANGKATAN DI AWAL         |')
        print('+-----------------------------------------------------+')
        mylist.view()
        print('\nData akan ditambahkan pada No.1')
        arv = input('Jam Keberangkatan\t: ')
        des = input('Tujuan\t\t\t: ').upper()
        num = input('Nomor Kereta\t\t: ').upper()
        sum = input('Jumlah Penumpang\t: ').upper()
        mylist.addFirst(arv,des,num,sum)
        print('Data telah ditambahkan\n')
        mylist.view()

    elif ask == '4':
        print("Memproses...")
        time.sleep(0.5)
        os.system('cls')
        print('+-----------------------------------------------------+')
        print('|       MENAMBAH JADWAL KEBERANGKATAN DI AKHIR        |')
        print('+-----------------------------------------------------+')
        mylist.view()
        print(f'\nData akan ditambahkan pada No.{mylist.length()+1}')
        arv = input('Jam Keberangkatan\t: ')
        des = input('Tujuan\t\t\t: ').upper()
        num = input('Nomor Kereta\t\t: ').upper()
        sum = input('Jumlah Penumpang\t: ').upper()
        mylist.addEnd(arv,des,num,sum)
        print('Data telah ditambahkan\n')
        mylist.view()

    elif ask == '5':
        print("Memproses...")
        time.sleep(0.5)
        os.system('cls')
        print('+---------------------------------------+')
        print('| MEMPERBARUI DATA JADWAL KEBERANGKATAN |')
        print('+---------------------------------------+')
        print('|      Data yang ingin perbarui :       |')
        print('|    [1] Jam Keberangkatan              |')
        print('|    [2] Tujuan Keberangkatan           |')
        print('|    [3] Nomor Kereta                   |')
        print('|    [4] Jumlah Penumpang               |')
        print('+---------------------------------------+')
        
        tanya = input('Pilih: ')
        while tanya not in ['1','2','3','4']:
            print('Pilih dari pilihan yang tersedia')
            tanya = input('Pilih: ')
        if tanya == '1':
            print("Memproses...")
            time.sleep(0.5)
            os.system('cls')
            print('+-----------------------------------------------------+')
            print('|            MEMPERBARUI JAM KEBERANGKATAN            |')
            print('+-----------------------------------------------------+')
            mylist.view()
            while True:
                while True:
                    try:
                        pos = int(input('\nNo. Urut\t: '))
                        break
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")
                new = input('Jam Baru\t: ').upper()
                if mylist.Update(pos,new,1) == 1:
                    break
            print('')
            mylist.view()

        elif tanya == '2':
            print("Memproses...")
            time.sleep(0.5)
            os.system('cls')
            print('+-----------------------------------------------------+')
            print('|              MEMPERBARUI TUJUAN KERETA              |')
            print('+-----------------------------------------------------+')
            mylist.view()
            while True:
                while True:
                    try:
                        pos = int(input('\nNo. Urut\t: '))
                        break
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")
                new = input('Tujuan Baru\t: ').upper()
                if mylist.Update(pos,new,2) == 1:
                    break
            print('')
            mylist.view()

        elif tanya == '3':
            print("Memproses...")
            time.sleep(0.5)
            os.system('cls')
            print('+-----------------------------------------------------+')
            print('|           MEMPERBARUI NOMOR KEBERANGKATAN           |')
            print('+-----------------------------------------------------+')
            mylist.view()
            while True:
                while True:
                    try:
                        pos = int(input('\nNo. Urut\t: '))
                        break
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")
                new = input('Nomor Baru\t: ').upper()
                if mylist.Update(pos,new,3) == 1:
                    break
            print('')
            mylist.view()

        elif tanya == '4':
            print("Memproses...")
            time.sleep(0.5)
            os.system('cls')
            print('        MEMPERBARUI JUMLAH PENUMPANG')
            mylist.view()
            while True:
                while True:
                    try:
                        pos = int(input('\nNo. Urut\t: '))
                        new = int(input('Jumlah Baru\t: '))
                        break
                    except ValueError:
                        print("Input harus berupa angka. Silakan coba lagi.")
                if mylist.Update(pos,new,4) == 1:
                    break
            print('')
            mylist.view()

    elif ask == '6':
        print("Memproses...")
        time.sleep(0.5)
        os.system('cls')
        print('+-----------------------------------------------------+')
        print('|           MENGHAPUS JADWAL KEBERANGKATAN            |')
        print('+-----------------------------------------------------+')
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
                
    elif ask == '7':
        print("Memproses...")
        time.sleep(0.5)
        os.system('cls')
        print('+------------------------------------------------------------------+')
        print('|                       RIWAYAT PERUBAHAN                          |')
        print('+------------------------------------------------------------------+')
        mylist.viewHistory()
    
    elif ask == '8':
        tujuan = input("Tujuan: ")
        mylist.jump_search_task(tujuan)
        


    
    Q()

main()
