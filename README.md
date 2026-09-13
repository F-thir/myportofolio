== IDENTITAS ==
Name : Fathir

NPM : 2506539523

Class : PBP F

== UPDATED ==
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
    - Used in experience and skill tab.

== PERTANYAAN REFLEKTIF - TUGAS 2 ==
1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.
2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.
3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.

### Tugas 2
1. ...
2. ...
3. ...

== AI Declaration ==
Note:
Pada tugas 2 ini saya tidak menggunakan AI untuk memberikan kode secara langsung / jiplak-menjiplak.

Strategi Prompting:
Saya menggunakan "ChatGPT" sebagai wadah untuk bertanya terkait hal-hal yang saya tidak bisa temukan lebih lanjut melalui W3School dan sumber lainnya.
Hal tersebut guna mempercepat dan memperjelas pencarian terkait apa yang saya perlukan, serta menghilangkan beberapa error yang terjadi.

Contoh:
1. Bagaimana cara saya membuat "check full description" supaya ketika di-klik dia dapat turun ke-bawah?

Disini AI menjawab bahwa saya perlu menggunakan konsep order
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