## == IDENTITAS ==

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

> Tugas 3 (Updated)
- Updates on Tab (Skill)
    - Searching Skill bar
    - Create Skill using Form (Add)
    - Delete Skill button
    - Redirect Tab (Skill Form)
    - New Edit/Update button

- Updates on Tab (Experience)
    - Searching Experience bar
    - Create Experience using Form (Add)
    - Delete Experience button
    - Redirect Tab (Experience Form)
    - New Edit/Update button
    
- Implementing the same on Tab (Project)
- New searching by category on Tab (Experience & Skill)
- Adjustment & Few Unit Testing
- Adjust Responsive

> Tutorial 4
- New Login, Register, Logout system
- New Cookie & Session system
- New star feature in Tab (Projects)
- Finished Tutorial 4

> Tugas 4 
- Adjust superuser on each Tab (Experience, Skill)
- Added Editor permission & authorization
- New star feature in Tab (Experience)
- New star effect:
    - If star clicked/hold, floating star fading animation
    - If card is starred, highlight with yellow border
- Adjust CSS & Responsive

> Tutorial 5
- New Toast Notification
- New Search Debouncing
- New form in the same tab (Project)
- New XSS protection system
- Adjust with Previous Assignment
- Finished Tutorial 5

> Tugas 5
- Adjusting the 'Experience' and 'Skill' tab to match 'Tugas 5' requirements:
    - View Data with AJAX
    - Search with Debouncing
    - Add Data with Modal & AJAX
    - Toast Notification
    - XSS protection system
- Adjust & Unit Testing
- New Update Data with Modal & AJAX on tab (Experience)

## == PERTANYAAN REFLEKTIF - TUGAS 5 ==
1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!
2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!

### Tugas 5

1. Teknik debouncing adalah teknik untuk memberikan jeda sebelum menjalankan suatu fungsi. Pada fitur pencarian menggunakan AJAX, debouncing digunakan supaya request ke server tidak dikirim setiap kali pengguna mengetik satu karakter.

Misalnya, ketika pengguna ingin mencari kata "Python", tanpa debouncing, perubahan input seperti "P", "Py", "Pyt", "Pyth", "Pytho", hingga "Python" dapat menyebabkan request AJAX dikirim ke server. Hal tersebut membuat request yang dikirim menjadi lebih banyak padahal masih dalam proses mengetik.

Dengan debouncing, request hanya akan dijalankan setelah pengguna berhenti mengetik selama waktu tertentu (sesuai yang di set). Pada program saya, waktu tersebut selama 300 ms. Jika pengguna kembali mengetik sebelum 300 ms selesai, timer sebelumnya akan dibatalkan dan timer baru akan dimulai.

Menurut saya, teknik ini penting diterapkan karena dapat mengurangi request AJAX yang tidak diperlukan sehingga penggunaan resource server menjadi lebih efisien dan fitur pencarian dapat berjalan dengan baik.

2. Penggunaan 'await' berfungsi untuk membuat program menunggu sampai proses yang bersifat asynchronous selesai sebelum melanjutkan ke proses berikutnya. Pada kode saya, await digunakan ketika mengambil data menggunakan fetch() dan ketika mengubah response menjadi JSON.

Misalnya:
const response = await fetch(url);
const projectData = await response.json();

Saat melakukan fetch(), diperlukan waktu untuk mendapatkan data dari server. Dengan menggunakan await, program akan menunggu sampai response dari server diterima terlebih dahulu. Setelah itu, response tersebut dapat diubah menjadi data JSON dan digunakan untuk menampilkan project.

Jika await tidak digunakan, program tidak langsung mendapatkan hasil dari fetch(), tetapi mendapatkan sebuah Promise. Hal tersebut dapat menyebabkan program lanjut ke kode berikutnya sebelum data dari server selesai diterima. Ini dapat menyebabkan data yang ingin digunakan belum tersedia ketika kode tersebut dijalankan.

Maka, await di sini membantu mengatur urutan proses asynchronous supaya data dari server sudah tersedia sebelum digunakan oleh program.

3. XSS (Cross-Site Scripting) adalah serangan ketika seseorang memasukkan kode atau script berbahaya ke dalam website. Jika kode tersebut tidak ditangani dengan baik, kode tersebut dapat dijalankan oleh browser ketika ditampilkan kepada pengguna.

Misalnya, seseorang memasukkan kode atau script berbahaya melalui form seperti "Tambah Project" atau form lainnya. Jika input tersebut langsung ditampilkan tanpa pengamanan, kode tersebut dapat ikut dijalankan oleh browser.

Sepemahaman saya, XSS perlu diperhatikan ketika menggunakan AJAX/JavaScript karena data yang didapat dari server akan dimasukkan kembali ke halaman menggunakan JavaScript. Jika data tersebut langsung dimasukkan menggunakan innerHTML tanpa dilakukan escaping (mengubah karakter), data yang seharusnya hanya berupa teks bisa dianggap sebagai kode HTML oleh browser.

Sedangkan, jika menggunakan template Django seperti: {{ project.title }}
Django secara default melakukan autoescaping terhadap data yang ditampilkan. Jadi, karakter tertentu seperti < dan > akan diubah sehingga tidak langsung dianggap sebagai HTML.

## == AI Declaration ==

Note:
Pada tugas 5 ini saya tidak menggunakan AI untuk memberikan kode secara langsung / jiplak-menjiplak.

Strategi Prompting:
Saya menggunakan "ChatGPT" sebagai wadah untuk bertanya terkait hal-hal yang saya tidak bisa temukan lebih lanjut melalui W3School dan sumber lainnya.
Hal tersebut guna mempercepat dan memperjelas pencarian terkait apa yang saya perlukan, serta menghilangkan beberapa error yang terjadi.

Contoh:
1. Bisakah anda menjelaskan konsep fungsi dari kode program bagian ini?
```
async function fetchProjects(searchQuery = "") {
    if (projectsAbortController) projectsAbortController.abort();
    projectsAbortController = new AbortController();

    try {
        displayPageSection({ showLoading: true });
        
        const url = searchQuery
            ? `${BASE_PROJECTS_ENDPOINT}?title=${encodeURIComponent(searchQuery)}`
            : BASE_PROJECTS_ENDPOINT;
        
        const response = await fetch(url, {
            headers: { 'Accept': 'application/json' },
            signal: projectsAbortController.signal,
        });

        if (!response.ok) throw new Error('Failed to fetch data');

        const projectData = await response.json();

        if (projectData.length === 0) {
            displayPageSection({ showEmpty: true });
        } else {
            gridContainer.innerHTML = '';
            projectData.forEach(item => {
                gridContainer.appendChild(buildProjectCardElement(item));
            });
            displayPageSection({ showGrid: true });
        }
    } catch (error) {
        if (error.name === 'AbortError') return;
        console.error('Error loading projects:', error);
        displayPageSection({ showError: true });
    }
}
```

Contoh hasil prompt:
```
AI menjelaskan bahwa fungsi fetchProjects() digunakan untuk mengambil data project dari endpoint menggunakan fetch(). Parameter searchQuery digunakan untuk melakukan pencarian berdasarkan judul project. AbortController digunakan untuk membatalkan request sebelumnya apabila terdapat request baru, sedangkan response.json() digunakan untuk mengubah response dari server menjadi data JSON yang dapat diproses oleh JavaScript.

AI juga menjelaskan bahwa kode tersebut memiliki beberapa kondisi tampilan, yaitu loading ketika request sedang berlangsung, empty ketika tidak terdapat data, grid ketika data berhasil diperoleh, dan error ketika terjadi kegagalan dalam proses request.
```

Sebagian besar kode saya terinspirasi dari W3School, Django Documentation, serta web-web yang berkaitan.