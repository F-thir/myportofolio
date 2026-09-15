== IDENTITAS ==
Name : Fathir

NPM : 2506539523

Class : PBP F

## == UPDATE ==
> Tugas 1 (Updated)
- New Navigation (Experience)
    - New Hover effect on each option
- New Section (Experience)
    - Contains three personal experience sections
    - Experience information: Title, Description, Year, Photo, and Documentation Description
    - New Animation (Style): Image changes every 4 seconds
    - New Hover effect on each personal experience
- Better Responsive CSS Style

> Tutorial 2 
- Finished Tutorial 2

> Tugas 2 (Updated)
- New Navigation (Skill)
- New Tab/Url (Skill)
    - Contains few personal skill sections
    - Skill information: Title, Image, Category, Description, and Details (Field)
    - New button to expand description (to see details)
- New Hover effect
    - Used in experience and skill tab (Glowing orange outline)
    - Expand description button
- Adjusted a few thing
- Finished unit testing

> Tutorial 3
- New Tab (Projects)
    - Contain few project cards
    - New Add Project Feature
    - New Delete Project Feature
- Finished Tutorial 3

## == PERTANYAAN REFLEKTIF - TUGAS 2 ==
1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

### Tugas 2
1. Ketika pengguna membuka halaman portofolio baru, misalnya halaman Skill (URL /skill/), terjadi beberapa proses yang saling berhubungan.

<!-- Kode diambil dari masing-masing file di sini-->
Pertama, request dari browser diterima oleh urls.py proyek. 
Pada bagian: *path("", include("main.urls"))*
request yang masuk akan diarahkan ke urls.py aplikasi main.

Kemudian, urls.py aplikasi main menentukan view yang akan menangani URL tersebut. 
Pada bagian: *path("skill/", show_skill, name="show_skill")*
URL /skill/ akan diarahkan ke fungsi show_skill yang terdapat di views.py.

Selanjutnya, view show_skill mengambil data dari model Skill.
Model disini berfungsi sebagai penentu struktur data skill dan penghubung dengan database. 
Pada bagian: *"skill_list": Skill.objects.all()*

Data (Skill) tersebut kemudian dimasukkan ke dalam variable context dan dikirim ke template skill.html.
Pada bagian: *return render(request, "skill.html", context)*

Setelah itu, template skill.html menerima data skill_list dan menggunakan Django Template Language, seperti *for loop* untuk menampilkan seluruh data skill. Setelah template diproses oleh Django, hasilnya (HTML) yang akan dikirim kembali ke browser dan ditampilkan kepada pengguna.

Intinya, alurnya:
Browser → urls.py proyek → urls.py aplikasi main → show_skill (view) → Skill (model) → database → view → skill.html (template) → HTML → Browser.

Maka: 
--> urls.py proyek mengarahkan request ke aplikasi
--> urls.py aplikasi menentukan view
--> view mengambil dan mengatur data
--> model menentukan struktur data 
--> template menampilkan data tersebut kepada pengguna.

2.  Dengan menggunakan model, proses pengelolaan dan penyimpanan data akan menjadi lebih mudah. Seperti yang sempat saya jelaskan pada Tugas 1, jika data dituliskan secara langsung pada template, tampilan HTML akan menjadi sangat panjang ketika ingin menambahkan data baru. Selain itu, ketika ingin mengubah suatu data, kita mungkin perlu mengubah kode HTML secara manual. Apabila jumlah data semakin banyak, proses tersebut akan semakin lama dan sulit dilakukan.

Jika menggunakan model, perubahan data tidak perlu dilakukan dengan mengubah kode HTML secara langsung. Pada template HTML, kita dapat menggunakan for loop untuk menampilkan data yang baru saja ditambahkan. Misalnya:

{% for skill in skill_list %} <!-- Data bebas -->
    <!-- Isi data sesuai konfigurasi -->
{% endfor %} <!-- End loop -->

Dengan cara ini, kode template tidak perlu diubah setiap kali terdapat data baru sehingga aplikasi menjadi lebih mudah untuk dipelihara dan dikembangkan. Data baru tidak perlu ditambahkan secara langsung ke dalam HTML, tetapi cukup ditambahkan ke database. Dengan demikian, data menjadi lebih terstruktur dan aplikasi menjadi lebih fleksibel.

3. Perbedaan fungsi makemigrations dan migrate:
--> *makemigrations* dipakai untuk membuat file migration baru berdasarkan perubahan yang dilakukan pada models.py. Disini, Django mencatat perubahan model yang nantinya akan diterapkan ke sistem database.

--> *migrate* digunakan untuk menerapkan *migration* tersebut ke database sehingga struktur database berubah sesuai dengan model terbaru.

Misalnya:
Awalnya, saya punya class Skill dengan 2 field (title dan description)
class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

Lalu, saya ingin menambahkan field baru, yaitu image.
class Skill(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.URLField()

Nah, dikarenakan ada field baru, Django tidak bisa langsung menerapkan perubahan tersebut. Digunakanlah *makemigrations* untuk mencatat perubahan model baru tersebut. Supaya bisa diterapkan, dilakukan *migrate* sehingga database benar-benar berubah dan tersimpan sesuai model.

Dalam tugas 2 ini, terdapat file migration baru yaitu 0002_skill.py (Salah satu contohnya)


## == AI Declaration ==

Note:
Pada tugas 2 ini saya tidak menggunakan AI untuk memberikan kode secara langsung / jiplak-menjiplak.

Strategi Prompting:
Saya menggunakan "ChatGPT" sebagai wadah untuk bertanya terkait hal-hal yang saya tidak bisa temukan lebih lanjut melalui W3School dan sumber lainnya.
Hal tersebut guna mempercepat dan memperjelas pencarian terkait apa yang saya perlukan, serta menghilangkan beberapa error yang terjadi.

Contoh:
1. Bagaimana cara saya membuat "check full description" supaya ketika di-klik posisi button dapat turun ke-bawah?

Disini AI menjawab bahwa saya perlu menggunakan konsep "order"
Fiksasi yang saya lakukan:
-> Kode saya sebelumnya:

.skill-details {
    font-size: 1.1rem;
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--line);
    color: var(--text-muted);
}

.skill-button {    
    font-family: "Space Grotesk", -apple-system, sans-serif;
    background-color: var(--paper);
    font-size: 1rem;
    border-radius: var(--radius);
    width: 12rem;
    height: 2rem;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
}

-> Kode saya setelah:
.skill-toggle {
    display: flex;
    flex-direction: column;
}

.skill-details {
    order: 1;
    font-size: 1.1rem;
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--line);
    color: var(--text-muted);
}

.skill-button {    
    order: 2;
    font-family: "Space Grotesk", -apple-system, sans-serif;
    background-color: var(--paper);
    font-size: 1rem;
    border-radius: var(--radius);
    width: 12rem;
    height: 2rem;
    margin-top: 1rem;
    margin-bottom: 0.5rem;
    box-shadow: 0 0 5px rgba(0, 0, 0, 0.2);
    display: flex;
    align-items: center;
    justify-content: center;
}

Sebagian besar kode saya terinspirasi dari W3School dan Web-Web yang membahas tentang animasi dan sebagainya.