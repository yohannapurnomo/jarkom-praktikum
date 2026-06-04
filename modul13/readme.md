# Laporan Praktikum Jaringan Komputer - Modul 13

## Analisis Ethernet dan Address Resolution Protocol (ARP) Menggunakan Wireshark

### Identitas Praktikan

| Item      | Keterangan |
| --------- | ---------- |
| **Nama**  |    YOHANNA PURNOMO  |
| **NIM**   |    103072400127     |
| **Kelas** |   IF 04-01          |

---

# Pendahuluan

Ethernet merupakan teknologi jaringan yang bekerja pada layer Data Link dalam model OSI. Ethernet bertugas mengirimkan data dalam bentuk frame antar perangkat yang terhubung dalam jaringan lokal (LAN).

Selain Ethernet, terdapat Address Resolution Protocol (ARP) yang berfungsi untuk menerjemahkan alamat IP menjadi MAC Address. Protokol ini memungkinkan perangkat dalam jaringan lokal mengetahui alamat fisik perangkat tujuan sebelum proses komunikasi dilakukan.

Pada praktikum ini dilakukan pengamatan terhadap frame Ethernet dan proses ARP menggunakan aplikasi Wireshark. Selain itu dilakukan pemeriksaan ARP Cache menggunakan Command Prompt untuk melihat hubungan antara alamat IP dan MAC Address yang tersimpan pada komputer.

---

# Tujuan Praktikum

1. Memahami konsep dasar Ethernet.
2. Memahami fungsi dan cara kerja ARP.
3. Menggunakan Wireshark untuk menangkap dan menganalisis frame Ethernet.
4. Mengamati isi ARP Cache pada komputer.
5. Menganalisis proses ARP yang terjadi dalam jaringan.

---

# Tools yang Digunakan

| Tools                  | Fungsi                                        |
| ---------------------- | --------------------------------------------- |
| Wireshark              | Melakukan capture dan analisis paket jaringan |
| Command Prompt         | Menjalankan perintah ARP                      |
| Sistem Operasi Windows | Lingkungan praktikum                          |

---

# Langkah-Langkah Praktikum

## 1. Menangkap dan Menganalisis Frame Ethernet

Langkah pertama dilakukan dengan membuka aplikasi Wireshark dan memilih interface jaringan yang aktif. Setelah proses capture berjalan, dilakukan aktivitas jaringan sehingga Wireshark dapat menangkap frame Ethernet yang melewati interface tersebut.

Selanjutnya salah satu frame Ethernet dipilih untuk dianalisis. Pada bagian detail paket dapat dilihat informasi seperti Source MAC Address, Destination MAC Address, dan EtherType yang menunjukkan jenis protokol yang dibawa oleh frame tersebut.
Masukkan URL berikut ke dalam Browser Anda
[](http://gaia.cs.umass.edu/wireshark-labs/HTTP-ethereal-lab-file3.html)

![alt text](<gambar1.png>)

> *Gambar 1. Hasil URL dan menjalankan di wireshark.*


### Screenshot Hasil Analisis Frame Ethernet

!![alt text](<gambar2.png>)

> *Gambar 2. Hasil analisis frame Ethernet pada Wireshark.*

---

## 2. Melihat Isi ARP Cache

Untuk melihat daftar alamat IP dan MAC Address yang tersimpan pada komputer, dibuka Command Prompt kemudian menjalankan perintah berikut:

```bash
arp -a
```

Perintah tersebut digunakan untuk menampilkan ARP Cache yang berisi hasil pemetaan alamat IP dengan MAC Address yang telah diketahui oleh komputer.

### Screenshot Hasil Perintah ARP

![alt text](<gambar3.png>)

> *Gambar 3. Hasil perintah `arp -a` pada Command Prompt.*

---

## 3. Mengamati Paket ARP Menggunakan Wireshark

Setelah melihat ARP Cache, dilakukan pengamatan terhadap paket ARP yang tertangkap pada Wireshark.

Pada hasil capture dapat diamati proses ARP Request dan ARP Reply yang digunakan perangkat untuk mencari MAC Address dari suatu alamat IP dalam jaringan lokal.

### Screenshot Capture Paket ARP

![alt text](<gambar4.png>)

> *Gambar 4. Hasil capture paket ARP pada Wireshark.*

---

# Hasil dan Analisis

## 1. Analisis Frame Ethernet

Berdasarkan hasil pengamatan pada Wireshark, frame Ethernet memiliki beberapa informasi penting yaitu:

* Destination MAC Address
* Source MAC Address
* EtherType

Destination MAC Address menunjukkan alamat fisik tujuan pengiriman data, sedangkan Source MAC Address menunjukkan alamat fisik pengirim. EtherType digunakan untuk menunjukkan protokol yang dibawa oleh frame, misalnya IPv4, IPv6, atau ARP.

Frame Ethernet merupakan unit data utama pada layer Data Link yang digunakan untuk mengirimkan informasi antar perangkat dalam jaringan lokal.

---

## 2. Analisis ARP Cache

Hasil perintah `arp -a` menunjukkan daftar pasangan alamat IP dan MAC Address yang tersimpan pada komputer.

ARP Cache berfungsi sebagai penyimpanan sementara hasil proses ARP sehingga komputer tidak perlu terus-menerus mengirim ARP Request untuk perangkat yang sama. Dengan adanya cache ini, proses komunikasi menjadi lebih cepat dan efisien.

---

## 3. Analisis Paket ARP

Dari hasil capture Wireshark terlihat bahwa ARP bekerja melalui dua jenis pesan utama:

### ARP Request

ARP Request dikirim secara broadcast ke seluruh jaringan untuk mencari MAC Address dari alamat IP tertentu.

Tujuan dari pesan ini adalah menanyakan perangkat mana yang memiliki alamat IP yang dicari.

### ARP Reply

ARP Reply dikirim oleh perangkat yang memiliki alamat IP tersebut sebagai balasan atas ARP Request.

Pesan ini berisi informasi MAC Address yang dimiliki oleh perangkat tersebut sehingga pengirim dapat melakukan komunikasi secara langsung.

Setelah menerima ARP Reply, komputer akan menyimpan hasil pemetaan tersebut ke dalam ARP Cache untuk digunakan pada komunikasi berikutnya.

---

# Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa Ethernet merupakan protokol pada layer Data Link yang digunakan untuk mengirimkan data dalam bentuk frame antar perangkat pada jaringan lokal.

Selain itu, ARP berfungsi untuk menerjemahkan alamat IP menjadi MAC Address sehingga perangkat dapat mengetahui alamat fisik tujuan sebelum mengirimkan data.

Dengan menggunakan Wireshark, proses pengiriman frame Ethernet dan pertukaran pesan ARP dapat diamati secara langsung. Praktikum ini membantu memahami bagaimana komunikasi pada layer Data Link berlangsung dan bagaimana ARP mendukung proses komunikasi dalam jaringan komputer.

---
