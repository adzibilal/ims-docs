import os
import json

base_dir = "/home/adzibilal/adzibilal/ims/ims-docs/content/docs"

docs = {
    "admin/meta.json": {
        "title": "Admin Guide",
        "pages": ["index", "master-data", "academic", "commerce", "finance", "settings"]
    },
    "admin/index.mdx": """---
title: Admin Dashboard
description: Panduan memulai menggunakan dashboard admin
---

# Getting Started: Admin Dashboard

Selamat datang di IMS Dashboard untuk Admin! Panduan ini akan membantu Anda memahami tampilan awal dan fitur utama di dalam dashboard admin.

## 1. Login ke Dashboard

1. Buka halaman login IMS Dashboard di browser Anda.
2. Masukkan **Email** dan **Password** admin Anda.
3. Klik tombol **Sign In**.

[Image desc: Halaman Login IMS]

## Alur Kerja Admin (Admin Workflow)

Berikut adalah gambaran besar bagaimana Admin mengelola sistem IMS:

```mermaid
flowchart TD
    A[Master Data Setup] --> B[Academic Setup]
    B --> C[Commerce & Transaksi]
    C --> D[Finance & Payroll]
    
    A1(Input Siswa & Guru) -.-> A
    A2(Input Instrumen & Ruangan) -.-> A
    
    B1(Buat Kursus) -.-> B
    B2(Buat Kelas & Jadwal) -.-> B
    B3(Daftarkan Siswa) -.-> B
    
    C1(Buat Paket Harga) -.-> C
    C2(Catat Pesanan) -.-> C
    C3(Catat Pembayaran) -.-> C
    
    D1(Hitung Kehadiran) -.-> D
    D2(Generate Payroll Guru) -.-> D
```

Pilih menu di sidebar untuk melihat panduan spesifik per modul.
""",
    "admin/master-data/meta.json": {
        "title": "Master Data",
        "pages": ["index", "students", "teachers", "instruments", "rooms"]
    },
    "admin/master-data/index.mdx": """---
title: Pendahuluan Master Data
description: Pengenalan modul Master Data
---

# Master Data

Modul **Master Data** merupakan fondasi sistem. Semua transaksi dan penjadwalan bergantung pada kelengkapan data di modul ini.

## Hubungan Antar Data

```mermaid
erDiagram
    STUDENT ||--o{ ENROLLMENT : has
    TEACHER ||--o{ CLASS : teaches
    INSTRUMENT ||--o{ COURSE : defines
    ROOM ||--o{ SCHEDULE : hosts
```

Silakan pilih sub-menu di samping untuk melihat panduan spesifik:
- [Siswa (Students)](/docs/admin/master-data/students)
- [Guru (Teachers)](/docs/admin/master-data/teachers)
- [Instrumen & Kategori](/docs/admin/master-data/instruments)
- [Ruangan (Rooms)](/docs/admin/master-data/rooms)
""",
    "admin/master-data/students.mdx": """---
title: Kelola Siswa
description: Panduan menambah, mengedit, dan menghapus siswa
---

# Mengelola Data Siswa

## 1. Menambahkan Siswa Baru
1. Buka menu **Master Data** > **Students**.
2. Klik tombol **+ Add New** atau **Tambah Siswa**.
3. Isi informasi pribadi siswa:
   - Nama lengkap
   - Email (digunakan untuk login siswa jika diaktifkan)
   - Nomor telepon
   - Tanggal lahir
   - Alamat
4. Klik **Save** untuk menyimpan data.

[Image desc: Form Tambah Siswa Baru]

## 2. Mengedit Data Siswa
Jika ada perubahan nomor telepon atau alamat:
1. Di halaman daftar siswa, cari nama siswa.
2. Klik ikon **Edit** (Pensil) pada baris nama siswa.
3. Perbarui datanya.
4. Klik **Save**.

[Image desc: Halaman Edit Siswa]

## 3. Menghapus Siswa
- Untuk menghapus, klik ikon **Delete** (Tempat Sampah). 
> **Perhatian**: Data siswa yang sudah memiliki riwayat pembayaran atau jadwal kelas aktif tidak dapat dihapus untuk menjaga integritas data keuangan.
""",
    "admin/master-data/teachers.mdx": """---
title: Kelola Guru
description: Panduan menambah guru dan mengatur status aktif
---

# Mengelola Data Guru

## 1. Menambahkan Guru Baru
1. Buka menu **Master Data** > **Teachers**.
2. Klik tombol **+ Add New**.
3. Lengkapi data guru, seperti nama, email, dan telepon.
4. Klik **Save**. Sistem akan membuatkan akun otomatis menggunakan email tersebut.

[Image desc: Form Tambah Guru]

## 2. Mengubah Status Aktif Guru
Jika ada guru yang sedang cuti panjang atau berhenti mengajar, Anda dapat menonaktifkan akun mereka:
1. Di daftar guru, cari nama guru.
2. Klik tombol **toggle** (saklar) pada kolom status (Active / Inactive).
3. Guru yang inaktif tidak dapat login ke aplikasi dan tidak akan muncul di pilihan pembuatan kelas baru.

[Image desc: Toggle Status Guru]

## 3. Reset Password Guru
Jika guru lupa kata sandinya:
1. Di baris nama guru, klik ikon **Reset Password** (Ikon Kunci).
2. Konfirmasi tindakan. Password akan direset menjadi password default aplikasi (misalnya: `password123` atau sesuai App Settings).
""",
    "admin/master-data/instruments.mdx": """---
title: Instrumen, Level, & Kategori
description: Mengelola data referensi untuk kursus
---

# Kelola Instrumen, Level, & Kategori

Data ini digunakan sebagai atribut ketika membuat Kursus (Course).

## Alur Pembuatan Atribut

```mermaid
graph LR
    A[Buat Kategori] --> B[Buat Level]
    B --> C[Buat Instrumen]
    C --> D[Gabungkan menjadi Kursus]
```

## 1. Menambah Instrumen
Misalnya "Piano", "Biola", atau "Gitar".
1. Buka menu **Master Data** > **Instruments**.
2. Klik **+ Add New**.
3. Masukkan nama instrumen dan simpan.

[Image desc: Halaman Tambah Instrumen]

## 2. Menambah Level
Misalnya "Beginner", "Intermediate", "Grade 1", "Grade 2".
1. Buka menu **Master Data** > **Levels**.
2. Klik **+ Add New**.
3. Masukkan nama level dan simpan.

## 3. Menambah Kategori
Kategori biasanya digunakan untuk membedakan genre atau departemen, misalnya "Klasik", "Pop", "Vokal".
1. Buka menu **Master Data** > **Categories**.
2. Tambahkan kategori baru dengan cara yang sama.
""",
    "admin/master-data/rooms.mdx": """---
title: Kelola Ruangan
description: Mengatur ruangan fisik yang digunakan untuk kelas
---

# Kelola Ruangan (Rooms)

Setiap jadwal kelas harus menempati ruangan tertentu untuk menghindari bentrok penggunaan ruang fisik.

## Menambah Ruangan
1. Buka menu **Master Data** > **Rooms**.
2. Klik **+ Add New**.
3. Masukkan rincian ruangan:
   - **Nama Ruangan**: Misal "Ruang Piano A"
   - **Kapasitas**: Misal "2" (untuk privat) atau "10" (untuk grup)
4. Klik **Save**.

[Image desc: Form Tambah Ruangan]

Ruangan ini nantinya akan dipilih saat Anda membuat **Schedules** di menu Academic.
""",
    "admin/academic/meta.json": {
        "title": "Academic",
        "pages": ["index", "courses", "classes", "enrollments", "schedules", "sessions"]
    },
    "admin/academic/index.mdx": """---
title: Pendahuluan Akademik
description: Alur kerja modul akademik
---

# Manajemen Akademik

Modul **Academic** mengelola seluruh siklus pembelajaran, mulai dari mendefinisikan kurikulum (Course) hingga menjadwalkan pertemuan rutin (Schedules) dan pertemuan aktual (Sessions).

## Siklus Akademik

```mermaid
stateDiagram-v2
    [*] --> Courses : 1. Buat Program Studi
    Courses --> Classes : 2. Buka Kelas Baru
    Classes --> Enrollments : 3. Masukkan Siswa
    Classes --> Schedules : 4. Atur Jadwal Rutin
    Schedules --> Sessions : 5. Generate Pertemuan Aktual
    Sessions --> Attendance : 6. Guru Isi Absensi
    Attendance --> [*]
```

Silakan navigasi melalui sub-menu:
- [Courses](/docs/admin/academic/courses)
- [Classes](/docs/admin/academic/classes)
- [Enrollments](/docs/admin/academic/enrollments)
- [Schedules](/docs/admin/academic/schedules)
- [Sessions & Attendance](/docs/admin/academic/sessions)
""",
    "admin/academic/courses.mdx": """---
title: Kelola Courses
description: Panduan membuat program studi atau kursus
---

# Kelola Courses (Kursus)

**Course** adalah cetak biru (blueprint) dari apa yang diajarkan. Contoh Course: "Piano Klasik Grade 1".

## Membuat Course Baru
1. Pastikan Anda sudah membuat **Instrumen**, **Level**, dan **Kategori** di Master Data.
2. Buka menu **Academic** > **Courses**.
3. Klik **+ Add New**.
4. Isi form:
   - **Nama Course**: (Contoh: Piano Klasik Grade 1)
   - **Pilih Instrumen**: Piano
   - **Pilih Level**: Grade 1
   - **Pilih Kategori**: Klasik
5. Klik **Save**.

[Image desc: Form Tambah Course]

Setelah Course dibuat, Anda belum bisa memasukkan siswa. Anda harus membuat "Wadah"-nya terlebih dahulu, yaitu **Classes**.
""",
    "admin/academic/classes.mdx": """---
title: Kelola Classes
description: Membuka kelas dari course yang tersedia
---

# Kelola Classes (Kelas)

**Class** adalah instansiasi nyata dari sebuah Course yang diampu oleh seorang Guru tertentu.
Contoh: Kelas "Piano Klasik Grade 1 - Kelas Kak Budi".

## Membuat Kelas Baru
1. Buka menu **Academic** > **Classes**.
2. Klik **+ Add New**.
3. Isi rincian kelas:
   - **Nama Kelas**: Berikan nama yang mudah dikenali.
   - **Course**: Pilih course yang relevan.
   - **Teacher**: Tentukan guru yang akan mengajar kelas ini.
   - **Tipe Kelas**: Pilih apakah ini kelas Private (1 Guru 1 Siswa) atau Group.
4. Klik **Save**.

[Image desc: Form Membuat Kelas]

Setelah kelas dibuat, Anda bisa mulai mendaftarkan siswa (*Enrollment*) dan membuat jadwal rutinnya (*Schedules*).
""",
    "admin/academic/enrollments.mdx": """---
title: Kelola Enrollments
description: Mendaftarkan siswa ke dalam kelas
---

# Enrollments (Pendaftaran)

Untuk menempatkan siswa ke dalam kelas yang sudah ada, Anda menggunakan fitur Enrollment.

## Cara Mendaftarkan Siswa
1. Buka menu **Academic** > **Enrollments**.
2. Klik **+ Add New**.
3. Pilih **Siswa** dari dropdown.
4. Pilih **Kelas** tujuan.
5. Tanggal Bergabung (Join Date) akan otomatis terisi hari ini, atau bisa disesuaikan.
6. Klik **Save**.

[Image desc: Halaman Enrollments]

Satu siswa dapat didaftarkan ke beberapa kelas yang berbeda secara bersamaan.
""",
    "admin/academic/schedules.mdx": """---
title: Kelola Schedules
description: Menentukan jadwal rutin mingguan kelas
---

# Schedules (Jadwal Rutin)

Schedules digunakan untuk mendefinisikan waktu rutin operasional kelas (misal: "Setiap Selasa jam 14.00 - 15.00").

## Membuat Jadwal Rutin
1. Buka menu **Academic** > **Schedules**.
2. Klik **+ Add New**.
3. Lengkapi form penjadwalan:
   - **Kelas**: Pilih kelas yang akan dijadwalkan.
   - **Hari (Day of Week)**: Pilih hari, misalnya Selasa.
   - **Start Time**: Jam mulai (misal 14:00).
   - **End Time**: Jam selesai (misal 15:00).
   - **Ruangan (Room)**: Pilih ruang yang akan digunakan.
4. Klik **Save**.

[Image desc: Form Tambah Jadwal Kelas]

> **Penting**: Pembuatan Schedule akan men-trigger sistem untuk **meng-generate Sessions (Sesi)** di masa depan secara otomatis.
""",
    "admin/academic/sessions.mdx": """---
title: Sessions & Makeup
description: Mengelola pertemuan aktual dan kelas pengganti
---

# Sessions & Makeup Class

Sesi adalah pertemuan tunggal yang memiliki tanggal pasti (misalnya sesi kelas untuk tanggal 10 Agustus 2026).

## 1. Manajemen Sessions
1. Buka menu **Academic** > **Sessions**.
2. Anda akan melihat daftar kelas yang akan berjalan hari ini, besok, atau yang sudah lalu.
3. Admin dapat **mengubah status sesi** menjadi:
   - **Scheduled**: Jadwal normal.
   - **Completed**: Sesi sudah selesai (terjadi setelah absensi diisi).
   - **Canceled**: Sesi dibatalkan.
   - **Rescheduled**: Sesi ditunda ke waktu lain.

[Image desc: Halaman Daftar Sesi dengan Status]

## 2. Kelas Pengganti (Makeup Class)
Jika sesi dibatalkan atau siswa sakit (status kehadiran *Excused*), Anda bisa membuat sesi pengganti:
1. Buka menu **Academic** > **Makeup**.
2. Sistem akan menampilkan daftar siswa/absensi yang berhak mendapat kelas pengganti.
3. Klik tombol aksi untuk membuat **Sesi Makeup**.
4. Tentukan **Tanggal**, **Jam**, dan **Ruangan** baru untuk sesi pengganti tersebut.

[Image desc: Proses Membuat Makeup Class]
""",
    "admin/commerce/meta.json": {
        "title": "Commerce",
        "pages": ["index", "packages", "orders", "payments"]
    },
    "admin/commerce/index.mdx": """---
title: Pendahuluan Commerce
description: Siklus Penjualan dan Tagihan
---

# Modul Commerce

Modul Commerce digunakan untuk mencatat penjualan paket belajar kepada siswa, mengeluarkan invoice, dan melacak pembayaran.

## Siklus Commerce

```mermaid
flowchart TD
    A[Buat Paket Belajar] --> B[Siswa Beli Paket (Order)]
    B --> C[Sistem Generate Invoice PDF]
    C --> D[Siswa Melakukan Pembayaran (Payment)]
    D --> E{Apakah Lunas?}
    E -- Ya --> F[Status Order: Paid]
    E -- Belum --> G[Status Order: Partial]
```
""",
    "admin/commerce/packages.mdx": """---
title: Kelola Packages
description: Menyiapkan paket harga
---

# Packages (Paket Harga)

Sebelum Anda bisa membuat tagihan, Anda harus mendefinisikan apa yang dijual.

## Membuat Paket
1. Buka menu **Commerce** > **Packages**.
2. Klik **+ Add New**.
3. Isi rincian:
   - **Nama Paket**: Misal "Paket 4 Pertemuan Piano Private".
   - **Harga**: Misal Rp 500.000.
   - **Kuota/Sesi**: Misal 4 sesi.
4. Klik **Save**.

[Image desc: Form Tambah Paket]
""",
    "admin/commerce/orders.mdx": """---
title: Orders & Invoices
description: Membuat tagihan untuk siswa
---

# Orders & Invoices

## 1. Membuat Pesanan (Order)
Ketika siswa mendaftar atau waktunya perpanjangan paket:
1. Buka menu **Commerce** > **Orders**.
2. Klik **+ Add New**.
3. Pilih **Siswa**.
4. Pilih **Package** yang ingin dibeli.
5. Klik **Save**. Order baru akan berstatus **Unpaid**.

[Image desc: Halaman Pembuatan Order]

## 2. Mengunduh Invoice PDF
Sistem akan otomatis merancang invoice PDF:
1. Di daftar Orders, cari pesanan yang baru dibuat.
2. Klik ikon aksi **Download Invoice**.
3. Berikan file PDF tersebut kepada siswa atau wali murid untuk ditagihkan.

[Image desc: Tampilan Invoice PDF]
""",
    "admin/commerce/payments.mdx": """---
title: Kelola Payments
description: Mencatat pembayaran yang masuk
---

# Payments (Pembayaran)

Ketika siswa sudah mentransfer atau membayar tunai, catat di sistem ini.

## Mencatat Pembayaran
1. Buka menu **Commerce** > **Payments**.
2. Klik **+ Add New**.
3. Pilih **Order/Invoice** mana yang sedang dibayar.
4. Masukkan **Nominal** (Amount).
   - Jika dibayar penuh, nominal samakan dengan harga paket.
   - Bisa juga dicicil (bayar sebagian).
5. Pilih **Metode Pembayaran** (Cash, Transfer BCA, dll).
6. Klik **Save**.

[Image desc: Form Input Pembayaran]

Jika nominal pembayaran memenuhi atau melebihi sisa tagihan, status Order otomatis berubah menjadi **Paid** (Lunas).
""",
    "admin/finance/meta.json": {
        "title": "Finance",
        "pages": ["index", "payroll", "reports"]
    },
    "admin/finance/index.mdx": """---
title: Pendahuluan Finance
description: Manajemen Penggajian dan Laporan Keuangan
---

# Finance & Reports

Modul Keuangan difokuskan pada pengelolaan **Payroll Guru** berdasarkan sesi mengajar dan pemantauan **Laporan Kinerja**.

## Alur Payroll Guru

```mermaid
stateDiagram-v2
    Draft: Generate Payroll
    Review: Verifikasi Absensi & Tarif
    Published: Slip Gaji Siap Dilihat Guru
    Paid: Dana Telah Ditransfer
    
    [*] --> Draft
    Draft --> Review
    Review --> Published
    Published --> Paid
    Paid --> [*]
```
""",
    "admin/finance/payroll.mdx": """---
title: Kelola Payroll
description: Menghitung dan menerbitkan gaji guru
---

# Payroll (Penggajian)

Payroll dihitung otomatis berdasarkan sesi kelas dengan status *Completed* dan tarif mengajar masing-masing guru.

## 1. Generate Payroll (Siklus Bulanan)
1. Buka menu **Finance** > **Payroll**.
2. Klik **+ Generate Payroll**.
3. Pilih Bulan dan Tahun (Periode).
4. Klik proses. Sistem akan mengagregasi semua sesi mengajar dari semua guru pada bulan tersebut.

[Image desc: Halaman Generate Payroll]

## 2. Review & Publish
1. Setelah draft terbuat, klik pada draft tersebut untuk melihat detail per guru.
2. Anda dapat melihat rincian seperti absensi spesifik mana saja yang masuk ke tagihan guru tersebut.
3. Jika sudah sesuai, Anda bisa mengubah statusnya menjadi **Published**.
   > *Catatan: Setelah Published, Guru dapat melihat rincian honor ini di dashboard mereka masing-masing.*

[Image desc: Rincian Slip Gaji per Guru]

## 3. Pembayaran (Mark as Paid)
Setelah Anda mentransfer dana ke rekening guru, klik tombol **Mark as Paid** agar status payroll selesai (Paid).

## 4. Ekspor Bulk Payroll
Jika Anda memiliki banyak guru dan ingin mencetak semua slip sekaligus, gunakan opsi **Export Bulk** pada periode payroll terkait untuk mengunduh semua PDF slip gaji dalam format ZIP atau gabungan.
""",
    "admin/finance/reports.mdx": """---
title: Reports & Laporan
description: Melihat analitik dan laporan kinerja
---

# Reports

Sistem IMS menyediakan beberapa report dasar untuk mengukur kinerja.

## 1. Attendance Report
Menampilkan metrik kehadiran. 
- Berapa persen siswa yang hadir bulan ini?
- Berapa banyak kelas yang terpaksa dijadwalkan ulang?

[Image desc: Grafik Attendance Report]

## 2. Teacher & Student Report
Menganalisis pertumbuhan jumlah pendaftaran siswa baru dan statistik beban mengajar per guru.

## 3. Finance (Ledger) Report
Rangkuman sederhana dari arus kas:
- **Pemasukan**: Berasal dari Payments (Pembayaran pesanan).
- **Pengeluaran**: Berasal dari Payroll (Gaji guru yang berstatus Paid).
- **Saldo Netto**: Selisih pemasukan dan pengeluaran.
""",
    "admin/settings/meta.json": {
        "title": "Settings",
        "pages": ["index", "app-settings", "users", "roles"]
    },
    "admin/settings/index.mdx": """---
title: Pendahuluan Settings
description: Pengaturan sistem
---

# Settings (Pengaturan)

Area Settings dikhususkan untuk Administrator Utama guna menjaga integritas sistem.

Di sini Anda dapat mengatur:
- [App Settings](/docs/admin/settings/app-settings) (Nilai bawaan aplikasi)
- [Users](/docs/admin/settings/users) (Akun Admin)
- [Roles & Permissions](/docs/admin/settings/roles) (Hak Akses)
""",
    "admin/settings/app-settings.mdx": """---
title: App Settings
description: Mengubah nilai bawaan sistem
---

# App Settings

Aplikasi memiliki beberapa nilai *default* yang bisa Anda ubah tanpa bantuan programmer.

1. Buka menu **Settings** > **App Settings**.
2. Anda akan menemukan konfigurasi seperti **Default Password**.
   - Ini adalah kata sandi yang otomatis digunakan ketika ada Guru atau Siswa baru yang ditambahkan, atau ketika fitur Reset Password digunakan.
3. Ubah nilainya sesuai kebutuhan, lalu klik **Save**.

[Image desc: Form App Settings]
""",
    "admin/settings/users.mdx": """---
title: Manajemen Admin Users
description: Mengelola akses staf administrasi
---

# Users (Pengguna Admin)

Modul ini khusus untuk mengelola akun staf sekolah (Admin/Finance), **bukan** untuk mengelola siswa atau guru (Siswa dikelola di menu Students, Guru di menu Teachers).

## Menambah Admin Baru
1. Buka **Settings** > **Users**.
2. Klik **+ Add New**.
3. Masukkan nama, email, dan password awal.
4. Pilih **Role** yang sesuai (Misal: Admin Utama atau Staf Finance).
5. Klik **Save**.

[Image desc: Form Tambah User Admin]
""",
    "admin/settings/roles.mdx": """---
title: Roles & Permissions
description: Konfigurasi hak akses
---

# Roles & Permissions

Hak akses mengatur siapa yang boleh melihat menu tertentu.

```mermaid
pie title Distribusi Akses Menu Default
    "Admin Utama" : 100
    "Teacher" : 20
    "Student" : 10
```

- **Roles**: Adalah jabatan (Admin, Teacher, Student).
- **Permissions**: Adalah perizinan spesifik (Lihat Data Siswa, Edit Keuangan, dll).

Sebaiknya konfigurasi ini tidak diubah secara sembarangan, kecuali jika Anda mengerti struktur RBAC (Role-Based Access Control) di dalam sistem Laravel.
""",
    "teacher/meta.json": {
        "title": "Teacher Guide",
        "pages": ["index", "classes", "attendance", "payroll"]
    },
    "teacher/index.mdx": """---
title: Teacher Dashboard
description: Panduan dasar untuk masuk dan bernavigasi bagi Guru
---

# Getting Started: Teacher Dashboard

Selamat datang di IMS Dashboard! Sebagai pengajar, Anda menggunakan aplikasi ini untuk mengatur operasional mengajar sehari-hari.

## Alur Kerja Utama Guru

Sebagai guru, tugas administratif Anda di sistem ini sangat sederhana:

```mermaid
flowchart LR
    A[Cek Jadwal Hari Ini] --> B[Ajar Siswa di Kelas]
    B --> C[Isi Absensi & Catatan]
    C --> D[Ubah Status Sesi ke Completed]
    D -. Akhir Bulan .-> E[Lihat Slip Gaji (Payroll)]
```

## 1. Cara Login

1. Buka tautan IMS Dashboard.
2. Masukkan **Email** dan **Password** Anda. (Minta password ke admin jika lupa).
3. Klik **Sign In**.

[Image desc: Halaman Login Teacher]

## 2. Navigasi Dashboard

- **Dashboard**: Ringkasan kelas hari ini.
- **My Classes**: Daftar kelas reguler.
- **My Schedules**: Kalender mengajar rutin.
- **My Sessions**: Detail pertemuan aktual.
- **Payroll**: Slip honor.

[Image desc: Tampilan Dashboard Utama Guru]
""",
    "teacher/classes.mdx": """---
title: Melihat Kelas & Jadwal
description: Panduan memeriksa jadwal mengajar
---

# Melihat Kelas & Jadwal

## 1. My Classes
Melihat daftar program yang Anda pegang.
- Buka **My Classes**.
- Anda dapat melihat semua kelas aktif Anda.
- Klik nama kelas untuk melihat daftar nama siswa (Enrollment) di dalam kelas tersebut.

## 2. My Schedules
- Buka menu **My Schedules** untuk melihat pola jadwal mingguan Anda (misalnya setiap Selasa dan Kamis jam 15.00).

## 3. My Sessions
Sesi adalah pertemuan aktual.
- Buka **My Sessions**.
- Anda dapat mencari tanggal tertentu untuk melihat jam berapa saja Anda harus mengajar pada tanggal tersebut.
- Sesi berstatus *Scheduled* artinya belum terlaksana. Sesi *Completed* artinya sudah selesai dan absensinya sudah dicatat.
""",
    "teacher/attendance.mdx": """---
title: Input Attendance
description: Panduan mengisi kehadiran siswa
---

# Mengisi Daftar Hadir (Attendance)

Ini adalah tugas terpenting guru di aplikasi. Tanpa absensi dan status *Completed*, sesi mengajar tidak akan dihitung dalam pembayaran honor akhir bulan.

## Cara Mengisi Absensi

1. Buka menu **My Sessions**.
2. Cari kelas yang baru saja selesai diajarkan.
3. Klik tombol **Attendance** (atau dari menu aksi).
4. Di daftar siswa, ubah status kehadiran:
   - **Present**: Hadir
   - **Absent**: Tidak hadir (alfa)
   - **Excused**: Izin/Sakit (Admin dapat membuatkan kelas ganti nantinya).
5. Isi **Notes** (Catatan) untuk mencatat progres materi yang diajarkan hari ini. Catatan ini penting untuk pelacakan perkembangan siswa.
6. Klik **Save Attendance**.

[Image desc: Form Input Attendance]

## Menyelesaikan Sesi
Setelah absensi tersimpan:
1. Kembali ke daftar **My Sessions**.
2. Klik tombol untuk **Mark as Completed** pada sesi tersebut.

```mermaid
stateDiagram-v2
    Scheduled --> FormAbsensi : Guru Klik Attendance
    FormAbsensi --> Scheduled : Simpan Hadir/Sakit/Alfa
    Scheduled --> Completed : Guru Klik Mark as Completed
    Completed --> Payroll : Masuk ke Hitungan Gaji
```
""",
    "teacher/payroll.mdx": """---
title: Payroll & Slips
description: Cara mengunduh slip gaji guru
---

# Payroll & Honor Mengajar

Sistem secara transparan mencatat honor mengajar Anda berdasarkan sesi kelas berstatus *Completed*.

## Cara Mengecek dan Unduh Slip

1. Buka menu **Payroll**.
2. Anda akan melihat daftar bulan.
3. Jika statusnya **Published** atau **Paid**, artinya perhitungan sudah final.
4. Klik pada baris periode untuk melihat rincian sesi mengajar apa saja yang dibayar bulan ini.
5. Klik **Download Slip** untuk mendapatkan file PDF resmi.

[Image desc: Preview Slip Gaji PDF]
"""
}

# Clear existing files first to avoid conflicts
os.system("rm -rf /home/adzibilal/adzibilal/ims/ims-docs/content/docs/*")

for filepath, content in docs.items():
    full_path = os.path.join(base_dir, filepath)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    
    if filepath.endswith('.json'):
        with open(full_path, 'w') as f:
            json.dump(content, f, indent=2)
    else:
        with open(full_path, 'w') as f:
            f.write(content)

print("Documentation successfully generated.")
