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
- Responsive CSS Style


== PERTANYAAN REFLEKTIF - TUGAS 1 ==
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?

### Tugas 1
1. Ya, pada tutorial saya menggunakan beberapa elemen semantik, seperti: <header>, <nav>, <main>, <section>, <footer>. Sedangkan, pada tugas 1 ini saya menambahkan elemen semantik, seperti <section> untuk membentuk bagian "experience". Elemen-elemen tersebut membantu dalam membentuk struktur website menjadi lebih terorganisasi, terbaca, dan jelas. 

<header> = Digunakan sebagai wadah meletakkan nama profil dan bagian navigasi.
<nav> = Digunakan sebagai wadah meletakkan fungsi navigasi yang membantu mengarahkan pengguna ke bagian tertentu.
<main> = Digunakan sebagai wadah meletakkan isi dari website itu sendiri (konten utama).
<section> = Digunakan sebagai wadah untuk memisahkan bagian tertentu, seperti "profile" dan "experience".
<footer> = Digunakan sebagai wadah meletakkan penjelasan atau kredit di bagian akhir

Intinya, penggunaan elemen-elemen semantik di HTML5 ini membantu membentuk website yang benar-benar terstruktur. 
Jadi, ketika ada perubahan yang ingin dilakukan, saya tidak akan lupa dan tahu bagian mana yang perlu ditambahkan suatu fungsi atau diubah.

2. Tantangan yang saya temukan ketika mengatur CSS supaya tetap responsif adalah bagaimana cara membuat struktur grid yang sesuai dengan informasi yang ingin ditampilkan. Saya perlu memastikan setiap elemen tidak memiliki ukuran yang terlalu besar atau terlalu kecil, serta tetap terlihat rapi ketika ukuran layar berubah. Pertama-tama, saya mencoba mengecilkan ukuran tampilan website untuk melihat bagian atau elemen mana yang terlihat bermasalah. Saya melihat elemen mana yang "out of place", terlalu lebar, terlalu sempit, atau memiliki jarak yang kurang sesuai ketika ukuran layar dikecilkan. Dari situ, saya mencoba menentukan grid yang sesuai untuk setiap bagian. Menurut saya, menentukan struktur grid ini sendiri menjadi salah satu tantangan karena perlu mencoba beberapa kali (trial and error) sampai menemukan posisi yang tepat dan terlihat baik di desktop maupun mobile.

Setelah menemukan struktur yang tepat, saya mencoba mengubah posisi dan ukuran beberapa elemen ketika layar diperkecil. Dengan hal tersebut, saya dapat menentukan elemen mana yang perlu diprioritaskan dan disesuaikan supaya informasi tetap mudah dibaca tanpa membuat tampilan website terlihat aneh atau berantakan.

3. Batasan yang paling berasa adalah bagaimana cara menyajikan informasi di website secara optimal. Informasi yang ditampilkan sekarang hanya sebatas informasi yang telah dibuat sebelumnya di HTML. Website belum dapat mengambil atau menambahkan informasi melalui database sehingga apabila saya ingin menambahkan banyak project atau experience, struktur HTML juga akan menjadi terlalu panjang (too much). Selain itu, bentuk interaksi yang dapat dilakukan pengguna di website masih terkesan sederhana.

Dari batasan tersebut, saya ingin mencoba mengimplementasikan sistem yang dapat menampilkan portofolio secara lebih fleksibel sehingga pengguna dapat melihat lebih banyak project dan experience yang telah saya lakukan. Salah satu fungsionalitas ingin saya tambahkan, seperti sistem simpel pengelolaan project dan experience yang terhubung dengan database sehingga saya dapat menambahkan, mengubah, atau menghapus informasi tanpa harus mengubah struktur HTML secara langsung (tidak panjang). Saya juga ingin menambahkan fitur seperti filter project sehingga pengguna dapat mencari jenis project apa yang ingin mereka lihat.

== AI Declaration ==
Note:
Pada tugas 1 ini saya tidak menggunakan AI untuk memberikan kode secara langsung / jiplak-menjiplak.

Strategi Prompting:
Saya menggunakan "ChatGPT" sebagai wadah untuk bertanya terkait hal-hal yang saya tidak bisa temukan lebih lanjut melalui W3School dan sumber lainnya.
Hal tersebut guna mempercepat dan memperjelas pencarian terkait apa yang saya perlukan, serta menghilangkan beberapa error yang terjadi.

Contoh:
1. Bagaimana cara saya membentuk animation, kenapa terjadi overlaying text?
Ref: https://www.w3schools.com/css/css3_animations.asp

Disini AI menjawab bahwa saya perlu memperhatikan penamaan dari HTML & CSS yang telah saya bentuk karena kemungkinan animation tidak terbaca oleh CSS Style.

Fiksasi yang saya lakukan:
-> Kode saya sebelumnya:
.caption-1 {
    animation-delay: 0s;
}

.caption-2 {
    animation-delay: 4s;
}

.caption-3 {
    animation-delay: 8s;
}

-> Kode saya setelah:
.experience-photo .caption-1 {
    animation-delay: 0s;
}

.experience-photo .caption-2 {
    animation-delay: 4s;
}

.experience-photo .caption-3 {
    animation-delay: 8s;
}

Sebagian besar kode saya terinspirasi dari W3School.