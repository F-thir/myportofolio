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

## == PERTANYAAN REFLEKTIF - TUGAS 3 ==
1. Jelaskan mengapa kita menggunakan ModelForm pada Django alih-alih membuat form HTML secara manual. Selain itu, jelaskan pula mengapa kita diwajibkan menambahkan {% csrf_token %} pada form tersebut!
2. Pada Tutorial 03, kita membahas format data JSON dan XML. Mengapa JSON lebih disukai dalam pengembangan aplikasi web modern dibandingkan XML?
3. Jelaskan alur yang terjadi saat kamu menggunakan fungsi view untuk mengembalikan data portofoliomu dalam bentuk JSON. Mengapa kita perlu melakukan proses serialization pada model Django sebelum datanya dikembalikan?


### Tugas 3
1. Di sini, kita lebih menggunakan ModelForm pada Django dibandingkan membuat form HTML secara manual dikarenakan beberapa alasan berikut: 
    - Mengotomatisasi proses pembuatan form, seperti field, choice, dan sebagainya (jadi tidak manual).
    - Langsung terintegrasi dengan model untuk masing-masing database sehingga model konsisten.
    - Memudahkan pembuatan fitur, seperti create, delete, dan update data.

Jika menggunakan form HTML secara manual, kita perlu membuat setiap field, menangani proses validasi, serta penyimpanan data secara lebih manual, seperti "<.input>", "<.textarea>", dan "<.select>" sendiri. Kemudian, untuk mengambil datanya menggunakan request.POST.get() dan melakukan validasi sebelum membuat object dengan Skill.objects.create(). Dengan ModelForm, proses tersebut dapat  menggunakan "form.is_valid()" dan "form.save()".

Alasan perlu menambahkan {% csrf_token %} pada form adalah untuk melindungi form dari serangan seperti Cross-Site Request Forgery (CSRF). Disini token memungkinkan Django memverifikasi bahwa request yang dikirim itu berasal dari form yang sah. Jika token tidak valid, request POST akan ditolak oleh Django (403 Forbidden).

2. Dari yang saya baca, JSON lebih disukai dalam pegembangan aplikasi web modern dibanding XML karena lebih sederhana dan mudah dipahami. 
    - Dari segi syntax, JSON menggunakan pasangan key-value dan struktur yang lebih mudah dibaca dibandingkan XML.
    - JSON dapat langsung digunakan dalam aplikasi web berbasis JavaScript.
    - JSON banyak digunakan untuk pertukaran data antara frontend dan backend, seperti dengan API.

Contoh:
JSON:
{
    "name": "Python",
    "category": "programming"
} 

XML:
    <.name>Python</.name>
    <.category>programming</.category>

3. Saat fungsi view digunakan untuk mengembalikan data portofolio dalam bentuk JSON, pertama Django menerima request dari user. Kemudian, view mengambil data dari database menggunakan model, misalnya dengan Project.objects.all(). Jika terdapat parameter pencarian, data dapat difilter terlebih dahulu berdasarkan parameter tersebut.

Setelah mendapatkan data dari database, dilakukan proses serialization menggunakan serializers.serialize("json", projects). Proses ini mengubah objek atau QuerySet Django menjadi format JSON yang dapat dikirim melalui HTTP response. Setelah itu, JSON tersebut dikembalikan menggunakan HttpResponse dengan content_type="application/json".

Intinya:
Model/QuerySet Django → Serialization → JSON → HTTP Response → Client

Di sini, proses serialization diperlukan karena data yang diperoleh dari model Django berupa object/queryset, bukan data JSON yang dapat langsung dikirim sebagai response. Dengan serialization, object/QuerySet Django berubah menjadi format JSON yang dapat dikirim melalui HTTP response.

## == AI Declaration ==

Note:
Pada tugas 3 ini saya tidak menggunakan AI untuk memberikan kode secara langsung / jiplak-menjiplak.

Strategi Prompting:
Saya menggunakan "ChatGPT" sebagai wadah untuk bertanya terkait hal-hal yang saya tidak bisa temukan lebih lanjut melalui W3School dan sumber lainnya.
Hal tersebut guna mempercepat dan memperjelas pencarian terkait apa yang saya perlukan, serta menghilangkan beberapa error yang terjadi.

Contoh:
1. Bisakah anda menjelaskan secara detail baris per baris maksud kegunaan dari kode berikut:

    ```def get_projects_json(request):```
        ```title_query = request.GET.get("title", "").strip()```
        ```projects = Project.objects.all() if title_query:``` 
        ```if title_query:```
            ```projects = projects.filter(title__icontains=title_query)```
        ```projects_json = serializers.serialize("json", projects)```
        ```return HttpResponse(projects_json, content_type="application/json")```

Disini AI menjawab dan menjelaskan baris per baris supaya saya dapat lebih memahami konsep yang dilakukan di sini:

Contoh hasil prompt:

    Bagian request.GET.get("title", "")
    Artinya: Ambil nilai dengan nama "title". Kalau tidak ada, gunakan "".
    Contoh 1:
    /projects/json/?title=django
    hasilnya: "django"

Sebagian besar kode saya terinspirasi dari W3School serta web-web yang berkaitan.