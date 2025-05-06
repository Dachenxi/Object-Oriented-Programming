from abc import ABC, abstractmethod
from rich.table import Table
from rich import print

class Karyawan(ABC):
    kode = 0
    def __init__(self, nama_karyawan, masa_kerja, gender, divisi):
        Karyawan.kode += 1
        self.kode_karyawan = f"K{Karyawan.kode:02d}"
        self.nama_karyawan = nama_karyawan
        self.masa_kerja = masa_kerja
        self.gender = gender
        self.divisi = divisi
        
    @abstractmethod
    def hitungGaji(self):
        pass

class Ceo(Karyawan):
    def __init__(self, nama_karyawan, masa_kerja, gender, divisi):
        super().__init__(nama_karyawan, masa_kerja, gender, divisi)
        self.gaji_pokok = 15000000
        self.posisi = "CEO"
    
    def hitungGaji(self):
        if self.gender == "L":
                return self.gaji_pokok + (self.gaji_pokok * 10 / 100)
        else:
                return self.gaji_pokok

class Bendahara(Karyawan):
    def __init__(self, nama_karyawan, masa_kerja, gender, divisi):
        super().__init__(nama_karyawan, masa_kerja, gender, divisi)
        self.gaji_pokok = 10000000
        self.posisi = "Bendahara"
    
    def hitungGaji(self):
        if self.gender == "L":
            if self.masa_kerja < 10:
                return self.gaji_pokok + (self.gaji_pokok * 10 / 100) + (self.gaji_pokok * 20 / 100)
            else:
                return self.gaji_pokok + (self.gaji_pokok * 10 / 100) + (self.gaji_pokok * 40 / 100)
        else:
            if self.masa_kerja < 10:
                return self.gaji_pokok + (self.gaji_pokok * 20 / 100)
            else:
                return self.gaji_pokok + (self.gaji_pokok * 40 / 100)

class Kepaladivisi(Karyawan):
    def __init__(self, nama_karyawan, masa_kerja, gender, divisi):
        super().__init__(nama_karyawan, masa_kerja, gender, divisi)
        self.gaji_pokok = 8000000
        self.posisi = "Kepala posisi"
        
    def hitungGaji(self):
        if self.gender == "L":
            if self.masa_kerja < 10:
                return self.gaji_pokok + (self.gaji_pokok * 10 / 100) + (self.gaji_pokok * 20 / 100)
            else:
                return self.gaji_pokok + (self.gaji_pokok * 10 / 100) + (self.gaji_pokok * 40 / 100)
        else:
            if self.masa_kerja < 10:
                return self.gaji_pokok + (self.gaji_pokok * 20 / 100)
            else:
                return self.gaji_pokok + (self.gaji_pokok * 40 / 100)

class Staff(Karyawan):
    def __init__(self, nama_karyawan, masa_kerja, gender, divisi):
        super().__init__(nama_karyawan, masa_kerja, gender, divisi)
        self.gaji_pokok = 6000000
        self.posisi = "Staff"
        
    def hitungGaji(self):
        if self.gender == "L":
            if self.masa_kerja < 10:
                return self.gaji_pokok + (self.gaji_pokok * 10 / 100) + (self.gaji_pokok * 20 / 100)
            else:
                return self.gaji_pokok + (self.gaji_pokok * 10 / 100) + (self.gaji_pokok * 40 / 100)
        else:
            if self.masa_kerja < 10:
                return self.gaji_pokok + (self.gaji_pokok * 20 / 100)
            else:
                return self.gaji_pokok + (self.gaji_pokok * 40 / 100)
            

def show_data(list_karyawan):
    tabel_karyawan = Table(title="Data Karyawan")
    tabel_karyawan.add_column("Kode Karyawan")
    tabel_karyawan.add_column("Nama Karyawan")
    tabel_karyawan.add_column("Posisi")
    tabel_karyawan.add_column("Masa Kerja (th)")
    tabel_karyawan.add_column("Gender")
    tabel_karyawan.add_column("Nama divisi")
    tabel_karyawan.add_column("Gaji", justify="right")
    
    for data in list_karyawan:
        tabel_karyawan.add_row(f"{data.kode_karyawan}", f"{data.nama_karyawan}", f"{data.posisi}",
                               f"{data.masa_kerja}", f"{data.gender}",
                               f"{data.divisi}" if data.divisi else "-", f"Rp. {data.hitungGaji():,.2f}")

    print(tabel_karyawan)


ceo = Ceo("Mr. A", 12, "L", None)
bendahara = Bendahara("Mrs. B", 15, "P", None)
kadiv = Kepaladivisi("Mr. C", 17, "L", "SDM")
staff = Staff("Mrs. D", 8, "P", "Software Dev")
staff2 = Staff("Mr. E", 6, "L", "Software Dev")
staff3 = Staff("Mr. F", 9, "L", "Software Dev")
staff4 = Staff("Mrs. G", 10, "P", "Software Dev")
staff5 = Staff("Mrs. H", 12, "P", "Software Dev")

list_karyawan = [ceo, bendahara, kadiv, staff, staff2, staff3, staff4, staff5]

show_data(list_karyawan=list_karyawan)