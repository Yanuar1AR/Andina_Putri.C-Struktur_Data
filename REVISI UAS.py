import os
from tabulate import tabulate

aksesoris = [
            { "ID" : "111", "Nama produk": "Gelang", "Harga": "Rp 10000", "Stok": "30"},
            { "ID" : "211", "Nama produk": "Cincin", "Harga": "Rp 8000", "Stok": "20"},
            { "ID" : "121", "Nama produk": "Jam Tangan", "Harga": "Rp 42000", "Stok": "20"},
            { "ID" : "231", "Nama produk": "Kacamata", "Harga": "Rp 7000", "Stok": "10"},
            { "ID" : "151", "Nama produk": "Bando", "Harga": "Rp 8000", "Stok": "25"},
            { "ID" : "241", "Nama produk": "Kucir Rambut", "Harga": "Rp 5000", "Stok": "10"},
            { "ID" : "252", "Nama produk": "Kalung", "Harga": "Rp 15000", "Stok": "15"},
            { "ID" : "145", "Nama produk": "Kotak Pensil", "Harga": "Rp 20000", "Stok": "35"},
            { "ID" : "232", "Nama produk": "Dompet", "Harga": "Rp 45000", "Stok": "27"},
            { "ID" : "243", "Nama produk": "Ikat Pinggang", "Harga": "Rp 65000", "Stok": "45"}
        ]

fashion = [ { "ID" : "341", "Nama produk": "Celana Jeans", "Harga": "Rp 105000", "Stok": "20"},
            { "ID" : "351", "Nama produk": "Kemeja Polos", "Harga": "Rp 80000", "Stok": "20"},
            { "ID" : "361", "Nama produk": "Sweater", "Harga": "Rp 75000", "Stok": "50"},
            { "ID" : "371", "Nama produk": "Cardigan", "Harga": "Rp 45000", "Stok": "40"},
            { "ID" : "381", "Nama produk": "Rok Payung", "Harga": "Rp 75000", "Stok": "50"},
            { "ID" : "391", "Nama produk": "Celana Cargo", "Harga": "Rp 90000", "Stok": "45"},
            { "ID" : "325", "Nama produk": "Tunik", "Harga": "Rp 72000", "Stok": "60"},
            { "ID" : "324", "Nama produk": "Midi Dress", "Harga": "Rp 98000", "Stok": "35"},
            { "ID" : "326", "Nama produk": "Rok Plisket", "Harga": "Rp 64000", "Stok": "21"},
            { "ID" : "327", "Nama produk": "Kemeja Kotak-Kotak", "Harga": "Rp 70000", "Stok": "43"}
        ]
produk_list = aksesoris + fashion
class Produk:
    def __init__(self, produk_list):
        self.produk_list = produk_list

    def Katalog_Produk(self):
        print("-"*50)
        print("DAFTAR PRODUK".center(50))
        print(tabulate(self.produk_list, headers="keys", tablefmt="grid"))

    def Search_Produk(self):
        while True:
            print("1. Cari Kategori Produk")
            print("2. Cari nama produk")
            print("0. Kembali ke menu utama")
            option = input("\nPilih sesuai keinginan Anda : ")

            if option == '1':
                kategori = input("Masukkan Kategori Produk yang Ingin Dicari (Aksesoris/Fashion) : ").lower()
                if kategori == 'aksesoris':
                    print("-"*45)
                    print("DAFTAR AKSESORIS".center(45))
                    print(tabulate(aksesoris, headers="keys", tablefmt="grid"))
                elif kategori == "fashion":
                    print("-"*50)
                    print("DAFTAR FASHION".center(50))
                    print(tabulate(fashion, headers="keys", tablefmt="grid"))
                else:
                    print("Kategori tidak ditemukan")

            elif option == '2':
                nama = input("Masukkan Nama Produk yang Ingin Dicari : ").lower()
                for index, produk in enumerate(self.produk_list):
                    if produk["Nama produk"].lower() == nama.lower():
                        print(f"Produk ditemukan di indeks {index}: ")
                        data = [
                            {
                                "ID": produk["ID"],
                                "Nama produk": produk["Nama produk"],
                                "Harga": produk["Harga"],
                                "Stok": produk["Stok"]
                            }
                        ]
                        print(tabulate(data, headers="keys", tablefmt="grid"))
            elif option == '0':
                break
            else:
                print("Pilihan tidak valid, coba lagi.")
    def urut_produk(self, key="Nama produk"): 
        n = len(self.produk_list)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if (key == "Nama produk" and self.produk_list[j][key] < self.produk_list[min_index][key]):
                    min_index = j
            self.produk_list[i], self.produk_list[min_index] = self.produk_list[min_index], self.produk_list[i]
        print("\n== Produk setelah pengurutan berdasarkan Abjad ==")
        print(tabulate(self.produk_list, headers="keys", tablefmt="grid"))  
  
class Node:
     def __init__(self, id, nama_produk, harga, stok):
        self.id = id
        self.nama_produk = nama_produk
        self.harga = harga 
        self.stok = stok
        self.next = None
     
class OrderQueue:
    def __init__(self):
        self.front = None   
        self.rear = None    
        self.size = 0

    def enqueue(self, item):
        new_node = Node(item['ID'], item['Nama produk'], item['Harga'], item['Stok'])
        
        if self.is_empty():
            self.front = self.rear = new_node 
        else:
            self.rear.next = new_node  
            self.rear = new_node       
        self.size += 1
        
    def dequeue(self):
        if self.is_empty():
            print("Queue kosong, tidak ada produk untuk dihapus.")
            return None
        
        dequeu_node = self.front
        self.front = self.front.next  
        if not self.front:  
            self.rear = None 
        self.size -= 1
        return dequeu_node

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        if not current:
            print("Daftar Produk Kosong.")
            return
        else:
            print("\n")
            print("-"*50)
            print("Daftar Produk Saat Ini".center(50))
            print("-"*50)
            while current:
                print(f"ID: {current.id}, Nama produk: {current.nama_produk}, Harga: {current.harga}, Stok: {current.stok}")
                current = current.next

class Graph:
    def __init__(self):
        self.graph = {}

    def add_product(self, product):
        product = product.lower()
        if product not in self.graph:
            self.graph[product] = []

    def add_relation(self, product1, product2):
        product1, product2 = product1.lower(), product2.lower()
        if product1 in self.graph and product2 in self.graph:
            self.graph[product1] = self.graph.get(product1, []) + [product2]
            self.graph[product2] = self.graph.get(product2, []) + [product1]

    def show_recommendations(self):
        product = input("Masukkan nama produk untuk mendapatkan rekomendasi: ").lower()
        found_product = next((p for p in self.graph if p.lower() == product), None)
        if found_product:
            rekomendasi = self.graph[found_product]
            if rekomendasi:
                print(f"Rekomendasi untuk produk {found_product}: {', '.join(rekomendasi)}")
            else:
                print(f"Tidak ada rekomendasi untuk produk '{found_product}'.")
        else:
            print(f"Produk {product} tidak ditemukan dalam graph.")

class DiscountTree:
    def __init__(self):
        self.root = {
            "Fashion": [],
            "Aksesoris": []
        }

    def add_discount(self, kategori, produk, diskon):
        if kategori not in self.root:
            print(f"Kategori {kategori} tidak ditemukan.")
            return

        product_node = {"Nama produk": produk, "Diskon": diskon}
        self.root[kategori].append(product_node)

    def display_discounts(self, node=None, level=0):
        if node is None:
            node = self.root
        indent = " " * (level * 6)
        for kategori, produk_list in node.items():
            print(f"\n{indent} Kategori {kategori}")
            for produk in produk_list:
                if "Diskon" in produk:
                    print(f"{indent}  - {produk['Nama produk']} (Diskon: {produk['Diskon']}%)")
                else:
                    print(f"{indent}  - {produk['Nama produk']}")

os.system("cls")   
class Onlineshop:
    def main():
        katalog = Produk(produk_list)
        order = OrderQueue()
        graph = Graph()
        discount_tree = DiscountTree()

        graph.add_product('Celana Jeans')
        graph.add_product('Tunik')
        graph.add_product('Gelang')
        graph.add_product('Celana Cargo')
        graph.add_product('Mini Dress')
        graph.add_product('Cincin')

        graph.add_relation('Celana Jeans', 'Celana Cargo')  
        graph.add_relation('Tunik', 'Mini Dress')  
        graph.add_relation('Gelang', 'Cincin')  

        
        discount_tree.add_discount("Fashion", "Celana Jeans", 20)
        discount_tree.add_discount("Fashion", "Kemeja Polos", 15)
        discount_tree.add_discount("Aksesoris", "Ikat Pinggang", 10)
        discount_tree.add_discount("Aksesoris", "Kalung", 25)
        
        while(True):
            print("\n")
            print("=" *30)
            print("SELAMAT DATANG DI ONLINE SHOP")
            print("=" *30)
            print("1. Lihat Katalog Produk")
            print("2. Cari Produk Berdasarkan Kategori")
            print("3. Urutkan Produk")
            print("4. Tambah Produk Baru") 
            print("5. Hapus Produk")
            print("6. Rekomendasi Produk Terkait")
            print("7. Lihat Semua Diskon")
            print("0. Keluar\n")

            option = input("Masukan Opsi : ")
            
            if option == "1":
                katalog.Katalog_Produk()
            elif option == "2":           
                katalog.Search_Produk()
            elif option == "3":
                katalog.urut_produk() 
            elif option == "4":
                while True:
                    id = input("Masukkan ID                 : ")
                    nama = input("Masukkan nama produk        : ")
                    harga = input("Masukkan harga produk       : ")
                    stok = input("Jumlah stok produk          : ")

                    new_produk = {'ID': id, 'Nama produk': nama, 'Harga': harga, 'Stok': stok}                   
                    order.enqueue(new_produk)
                    order.display()
                    lanjut = input("\nIngin Menambah Produk Lagi? (y/n): ").lower()
                    if lanjut == 'y':
                        continue  
                    elif lanjut == 'n':
                        break  
                    else:
                        print("Pilihan tidak valid. Program dihentikan.")
                        break                
            elif option == "5":
                    print("\nProduk dalam queue sebelum dihapus:")
                    order.display()
                    order.dequeue()
                    print("\nProduk dalam queue setelah dihapus:")
                    order.display()
            elif option == "6":
                graph.show_recommendations()
            elif option == "7":
                discount_tree.display_discounts()
            elif option == "0":
                quit()
                
            else:
                print("Angka Yang Anda Masukkan Tidak Valid. Silahkan Coba Lagi!")

    if __name__ == '__main__':
        main()