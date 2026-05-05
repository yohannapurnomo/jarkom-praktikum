# Laporan Praktikum Jaringan Komputer - Modul 9

## Web Server Multithreaded & HTTP Client

---

## Identitas Praktikan

| Item      | Keterangan      |
| --------- | --------------- |
| **Nama**  | YOHANNA PURNOMO |
| **NIM**   | 103072400127    |
| **Kelas** | IF-04-01        |

---

## 9.1 Tujuan Praktikum

1. Membuat web server sederhana menggunakan socket
2. Mengimplementasikan multithreading pada server
3. Memahami cara kerja HTTP request dan response
4. Membuat HTTP client tanpa menggunakan browser
5. Menguji komunikasi client-server menggunakan TCP

---

## 9.2 Implementasi Web Server Multithreaded

### 9.2.1 Kode Program Server

**File:** `server.py`

```python
from socket import *
import threading

def handle_client(connectionSocket):
    try:
        message = connectionSocket.recv(1024).decode()
        filename = message.split()[1]

        f = open(filename[1:])
        outputdata = f.read()

        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        connectionSocket.send(outputdata.encode())

        connectionSocket.close()

    except:
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()

def main():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', 6789))
    serverSocket.listen(5)

    print("Server siap di port 6789...")

    while True:
        connectionSocket, addr = serverSocket.accept()
        print("Terhubung dengan:", addr)

        thread = threading.Thread(target=handle_client, args=(connectionSocket,))
        thread.start()

if __name__ == "__main__":
    main()
```

**Penjelasan:**

* Server menggunakan `SOCK_STREAM` (TCP)
* `listen(5)` memungkinkan beberapa koneksi masuk
* `accept()` menerima koneksi client
* Setiap client diproses dalam thread berbeda (`threading`)
* Server membaca file dan mengirim response HTTP

---

### 9.2.2 Hasil Eksekusi Server

#### Step 1 — Menjalankan Server

```
python server.py
```

![alt text](<gambar1.png>)

> *Screenshot menampilkan server berjalan dan listening pada port 6789 serta siap menerima koneksi dari client*

---

## 9.3 Implementasi HTTP Client

### 9.3.1 Kode Program Client

**File:** `client.py`

```python
import sys
from socket import *

server_host = sys.argv[1]
server_port = int(sys.argv[2])
filename = sys.argv[3]

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((server_host, server_port))

request = f"GET /{filename} HTTP/1.1\r\nHost: {server_host}\r\n\r\n"
clientSocket.send(request.encode())

print("Response dari server:")

while True:
    data = clientSocket.recv(4096)
    if not data:
        break
    print(data.decode(), end="")

clientSocket.close()
```

**Penjelasan:**

* Client menggunakan socket TCP (`SOCK_STREAM`)
* `connect()` untuk terhubung ke server
* Mengirim HTTP GET request
* Menggunakan loop `recv()` agar seluruh response diterima
* Menampilkan response dari server

---

### 9.3.2 Hasil Eksekusi Client

#### Step 2 — Menjalankan Client

```
python client.py localhost 6789 index.html
```

![alt text](<gambar2.png>)

> *Screenshot menampilkan client mengirim HTTP GET request dan menerima response dari server berupa status 200 OK serta isi file HTML*

---

## 9.4 File HTML yang Digunakan

**File:** `index.html`

```html
<html>
<body>
<h1>Hello Server!</h1>
</body>
</html>
```

![alt text](<gambar3.png>)

> *Screenshot menampilkan isi file HTML yang diminta oleh client dari server*

---

## 9.5 Analisis Praktikum

### 9.5.1 Analisis Web Server Multithreaded

**Hasil Pengamatan:**

* Server dapat menerima banyak client secara bersamaan
* Setiap request diproses dalam thread berbeda
* Tidak terjadi blocking saat banyak client terhubung

**Keunggulan:**

* Meningkatkan performa server
* Respons lebih cepat untuk banyak client

**Keterbatasan:**

* Penggunaan resource lebih besar
* Perlu manajemen thread yang baik

---

### 9.5.2 Analisis HTTP Client

**Hasil Pengamatan:**

* Client berhasil mengirim HTTP GET request
* Response server terdiri dari:

  * Header (HTTP/1.1 200 OK)
  * Body (isi file HTML)
* Data diterima menggunakan TCP

---

## 9.6 Testing Tambahan

### 9.6.1 Multiple Client

**Percobaan:**
Menjalankan beberapa client secara bersamaan

**Hasil:**

* Server tetap berjalan tanpa crash
* Semua client mendapatkan response
* Thread berjalan secara parallel

![alt text](<gambar4.png>)

> *Screenshot menampilkan beberapa client terhubung ke server secara bersamaan*

---

## 9.7 Kesimpulan

1. Web server berhasil dibuat menggunakan socket TCP
2. Implementasi multithreading memungkinkan server melayani banyak client
3. HTTP client berhasil mengirim request tanpa browser
4. Response server terdiri dari header dan body
5. Konsep client-server berbasis TCP berhasil diimplementasikan

---
