# Laporan Praktikum Jaringan Komputer - Modul 11
## Analisis Protokol DHCP Menggunakan Wireshark

### Identitas Praktikan

| Item | Keterangan |
|------|------------|
| **Nama** | YOHANNA PURNOMO |
| **NIM** | 103072400127 |
| **Kelas** | IF-04-01 |

---

# Pendahuluan

Dynamic Host Configuration Protocol (DHCP) merupakan salah satu protokol penting dalam jaringan komputer yang digunakan untuk memberikan konfigurasi IP Address secara otomatis kepada client. Dengan adanya DHCP, administrator jaringan tidak perlu lagi melakukan konfigurasi IP secara manual pada setiap perangkat yang terhubung ke jaringan.

Pada praktikum ini dilakukan pengamatan terhadap proses kerja DHCP menggunakan aplikasi Wireshark. Wireshark digunakan untuk melakukan packet capture sehingga proses komunikasi antara client dan DHCP Server dapat diamati secara langsung. Proses utama pada DHCP terdiri dari empat tahap yaitu DHCP Discover, DHCP Offer, DHCP Request, dan DHCP ACK.

Melalui praktikum ini mahasiswa dapat memahami bagaimana sebuah perangkat memperoleh alamat IP secara otomatis ketika terhubung ke jaringan.

---

# Tujuan Praktikum

1. Memahami konsep dasar protokol DHCP.
2. Mengetahui proses pemberian IP Address secara otomatis.
3. Menggunakan Wireshark untuk menangkap paket DHCP.
4. Menganalisis paket DHCP Discover, Offer, Request, dan ACK.
5. Memahami proses komunikasi antara client dan DHCP Server.

---

# Tools yang Digunakan

Berikut tools yang digunakan selama praktikum:

| Tools | Fungsi |
|------|------|
| Wireshark | Melakukan capture dan analisis paket jaringan |
| Command Prompt | Menjalankan perintah jaringan |
| Sistem Operasi Windows | Lingkungan praktikum |

---

# Langkah-Langkah Praktikum

## 1. Melepaskan IP Address dari Client

Langkah pertama yang dilakukan adalah membuka Command Prompt kemudian menjalankan perintah berikut:

```bash
ipconfig /release
```

Perintah tersebut digunakan untuk melepaskan atau menghapus alamat IP yang sedang digunakan oleh komputer. Setelah perintah dijalankan, komputer tidak lagi memiliki IP Address aktif sehingga koneksi jaringan sementara akan terputus.

Tahapan ini penting dilakukan agar client dapat meminta alamat IP baru dari DHCP Server pada proses berikutnya.


![alt text](<gambar1.png>)


> *Gambar 1  menunjukkan hasil perintah `ipconfig /release.*

---

## 2. Menjalankan Wireshark

Setelah IP Address dilepaskan, langkah berikutnya adalah membuka aplikasi Wireshark. Selanjutnya dipilih interface jaringan yang sedang aktif untuk melakukan packet capture.

Wireshark akan menangkap seluruh paket jaringan yang melewati interface tersebut, termasuk paket DHCP yang nantinya digunakan dalam proses analisis.

Pada tahap ini proses capture harus sudah berjalan sebelum client meminta IP baru agar seluruh paket DHCP dapat terekam dengan lengkap.

---

## 3. Meminta IP Address Baru

Setelah Wireshark berjalan, kembali ke Command Prompt kemudian jalankan perintah berikut:

```bash
ipconfig /renew
```

Perintah ini digunakan untuk meminta IP Address baru kepada DHCP Server. Ketika perintah dijalankan, komputer akan memulai proses DHCP yang terdiri dari:

1. DHCP Discover
2. DHCP Offer
3. DHCP Request
4. DHCP ACK

Seluruh proses tersebut akan direkam oleh Wireshark sehingga dapat dianalisis lebih lanjut.


![alt text](<gambar2.png>)

> *Gambar 2  menunjukkan hasil perintah `ipconfig /renew`*

---

## 4. Menghentikan Capture dan Analisis Paket

Setelah beberapa detik, proses capture pada Wireshark dihentikan. Selanjutnya dilakukan filtering paket menggunakan filter berikut:

```bash
dhcp
```

Filter tersebut digunakan agar Wireshark hanya menampilkan paket DHCP sehingga proses analisis menjadi lebih mudah.

Dari hasil capture dapat diamati beberapa jenis paket DHCP seperti Discover, Offer, Request, dan ACK.

> Tambahkan screenshot hasil capture DHCP pada Wireshark

![alt text](<gambar3.png>)
![alt text](<gambar4.png>)

*Gambar 3,4  menunjukkan hasil capture DHCP pada Wireshark*
---

# Hasil dan Analisis

Berdasarkan hasil praktikum, proses komunikasi DHCP dapat diamati dengan jelas pada Wireshark. Berikut penjelasan masing-masing proses:

---

## 1. DHCP Discover

Tahap pertama dimulai ketika client mengirimkan paket broadcast ke jaringan untuk mencari DHCP Server yang tersedia.

Pada tahap ini client belum memiliki IP Address sehingga paket dikirim menggunakan alamat broadcast.

Fungsi utama DHCP Discover adalah mencari server yang dapat memberikan konfigurasi jaringan.

---

## 2. DHCP Offer

Setelah menerima paket Discover, DHCP Server akan membalas dengan paket DHCP Offer.

Paket ini berisi penawaran alamat IP yang dapat digunakan oleh client beserta informasi tambahan seperti:

- Subnet Mask
- Default Gateway
- DNS Server
- Lease Time

Tahapan ini menunjukkan bahwa server siap memberikan IP kepada client.

---

## 3. DHCP Request

Setelah menerima penawaran IP dari server, client akan mengirim DHCP Request.

Paket ini berfungsi untuk memberi tahu server bahwa client menerima dan meminta penggunaan IP yang ditawarkan sebelumnya.

Tahap ini juga memastikan bahwa tidak terjadi konflik IP dengan perangkat lain.

---

## 4. DHCP ACK

Tahap terakhir adalah DHCP ACK (Acknowledgement).

Pada tahap ini server memberikan konfirmasi bahwa alamat IP resmi telah diberikan kepada client. Setelah menerima DHCP ACK, client dapat menggunakan IP tersebut untuk terhubung ke jaringan.

Proses DHCP pun selesai dilakukan.

---

# Kesimpulan

Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa DHCP merupakan protokol yang sangat membantu dalam proses konfigurasi jaringan karena mampu memberikan IP Address secara otomatis kepada client.

Dengan menggunakan Wireshark, proses komunikasi DHCP dapat diamati secara detail mulai dari DHCP Discover hingga DHCP ACK. Praktikum ini membantu memahami bagaimana perangkat memperoleh alamat IP dan bagaimana server memberikan konfigurasi jaringan secara otomatis.

Selain itu, penggunaan Wireshark juga mempermudah analisis lalu lintas jaringan sehingga sangat berguna dalam proses troubleshooting jaringan komputer.

---
