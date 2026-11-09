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

> Tutorial 7
- Implemented Django REST Framework (DRF) for Projects API
- Updated requirements.txt
- New Project Serializer
- New API Permission System
- New API Unit Testing
- Adjust Projects AJAX with DRF API
- Adjust with Previous Assignment
- Finished Tutorial 7

> Tugas 6 (Updated)
- Adjusting 'Experience' to match 'Tugas 6' requirements:
    - Implemented Django REST Framework (DRF)
    - New Delete Data with Modal
    - New Experience Serializer
    - New API Permission System
    - Adjust Experience AJAX with DRF API
    - New API Unit Testing
    - New "Finish" button to Mark Experience as Finished.
- Adjusting 'Projects' to match consistency:
    - New Update Data with Modal
    - New Delete Data with Modal
    - New "Edit" button
    - Adjust text, design, and script on HTML
    - Adjust API Unit Testing
- Adjusting 'Skill' to match 'Tugas 6' requirements and consistency:
    - Implemented Django REST Framework (DRF)
    - New Update Data with Modal
    - New Delete Data with Modal
    - New Skill Serializer
    - New API Permission System
    - Adjust Skill AJAX with DRF API
    - New API Unit Testing
- Pertanyaan Reflektif
- AI Declaration

## == PERTANYAAN REFLEKTIF - TUGAS 6 ==
1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!
2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?
3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?
4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?

### Tugas 6
1. Dari yang saya pahami, REST (Representational State Transfer) adalah sebuah gaya arsitektur untuk merancang web API. Lalu, REST menggunakan konsep resource di mana setiap data atau objek dalam sistem direpresentasikan melalui URL dan dapat dimanipulasi menggunakan HTTP methods, seperti GET, POST, PUT, PATCH, dan DELETE.

Mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful karena JSON hanyalah bentuk format data, bukan aturan API. Sebuah API perlu memperhatikan prinsip-prinsip REST (REST Constraints), seperti Client-Server Separation, Stateless, Cacheable, Uniform Interface, serta Layered System.

Client-Server Separation --> Memisahkan tanggung jawab tampilan antarmuka dengan pengelolaan data di server
Stateless --> Setiap request harus membawa informasi yang diperlukan supaya server dapat memprosesnya tanpa bergantung pada konteks request sebelumnya. 
Uniform Interface --> Mengatur bagaimana resource diidentifikasi dan dimanipulasi melalui representasi serta penggunaan HTTP methods yang sesuai. 
Cacheable --> Respons server harus memberikan informasi, apakah data boleh disimpan dalam cache atau tidak supaya mengurangi request berulang.
Layered System --> Memungkinkan adanya lapisan perantara, seperti proxy atau gateway, di antara client dan server tanpa harus diketahui oleh client.

Sebagai contoh, API yang mengembalikan JSON tetapi menggunakan satu URL untuk seluruh operasi tanpa memanfaatkan HTTP methods yang sesuai dengan fungsinya. Misalnya, menggunakan "/api?action=delete_experience" dengan method POST untuk menghapus data, padahal lebih tepat menggunakan method DELETE.

Perbedaan antara PUT dan PATCH:
- PUT mengganti seluruh resource, jadi semua field yang wajib harus dikirim. Jika ada yang kurang, request akan ditolak. Pada tests_api.py misalkan, PUT dengan {"title": "Incomplete"} menghasilkan (400). Sedangkan, PUT dengan payload (lengkap) menghasilkan (200). PUT akan lebih cocok ketika ingin mengirim seluruh isi data sekaligus.

- PATCH mengganti beberapa field yang dikirim dan field lain tidak berubah. Pada tests_api.py misalkan, PATCH dengan {"title": "Changed"} cukup mengubah judul saja. Sedangkan, field description dan lainnya tetap. PATCH akan lebih cocok ketika perubahan kecil, misalnya mengganti judul saja.

2. Serializer pada Django REST Framework berperan untuk mengubah data dari model Django yang sudah dibentuk di Models.py menjadi representasi yang dapat dikirimkan melalui API, misalkan dengan JSON. Serializer juga dapat mengubah data yang diterima dari client menjadi data Python yang dapat divalidasi dan disimpan ke dalam database.

Dibandingkan merakit dictionary secara manual menggunakan JsonResponse seperti pada Tutorial 05, serializer memberikan beberapa keuntungan. Pertama, serializer dapat melakukan validasi terhadap data yang dikirimkan client sebelum disimpan ke database, misalnya "validate_title" membersihkan tag HTML dengan "strip_tags". Kedua, serializer mempermudah proses konversi antara model Django dan JSON. Ketiga, kita dapat menentukan field apa saja yang boleh ditampilkan atau diubah melalui API, jadi struktur data menjadi lebih konsisten dan mudah dikelola, misalnya "star_count".

Misalkan, pada implementasi API Project, ProjectSerializer dapat mengubah objek Project dari Models menjadi JSON sekaligus memvalidasi data seperti title, description, dan tech_stack ketika client mengirimkan request.

3. Autentikasi memastikan identitas pengguna yang sedang mengakses (Siapa yang mengakses?). Sedangkan, otorisasi menentukan tindakan apa saja yang boleh dilakukan oleh pengguna tersebut (Apa yang diperbolehkan?).

Pada Django REST Framework, autentikasi dilakukan menggunakan SessionAuthentication yang membaca session login Django untuk mengenali pengguna. Setelah identitas pengguna diketahui, dilakukan ototorisasi, di mana permission class (IsPortfolioOwnerOrEditorOrReadOnly) digunakan untuk memeriksa apakah pengguna tersebut memiliki akses untuk melakukan tindakan tertentu.

Misalkan, pada tugas ini, Superuser memiliki permission untuk menambah, mengubah, dan menghapus data. Sedangkan, Editor hanya mengubah data. Lalu, Pengguna biasa hanya dapat melihat data.

Pemeriksaan hak akses harus dilakukan melalui permission class di server karena tampilan tidak memastikan keamanan. Menyembunyikan tombol Add, Edit, atau Delete di template hanya memengaruhi tampilan yang dilihat pengguna. Masalahnya, pengguna dapat mengirimkan request secara langsung melalui browser atau tools lainnya. Makanya, server harus tetap memvalidasi setiap request menggunakan permission class supaya pengguna tidak dapat melakukan tindakan di luar hak aksesnya. Misalkan, Editor yang mengirim POST atau DELETE langsung ke API akan ditolak (403).

4. Jadi, ketika API menggunakan SessionAuthentication, identitas pengguna dikenali melalui session yang tersimpan di cookie browser. Cookie tersebut dapat dikirimkan secara otomatis oleh browser ketika pengguna mengakses suatu website. Hal ini dapat memberikan risiko serangan CSRF (Cross-Site Request Forgery), yaitu serangan yang memanfaatkan session pengguna untuk mengirimkan request.

Makanya, request yang mengubah data, seperti POST, PUT, PATCH, dan DELETE, memerlukan token CSRF. Token ini digunakan untuk memastikan bahwa request yang dikirim itu benar-benar dari sumber yang memiliki token yang valid supaya mengurangi risiko request palsu dari website lain. 

Test yang menggunakan force_authenticate() tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan karena metode tersebut secara langsung menetapkan pengguna sudah login tanpa menjalankan proses autentikasi (SessionAuthentication). Dari situ, pemeriksaan CSRF dari SessionAuthentication tidak dijalankan.

Dalam menguji perlindungan CSRF, kita perlu menggunakan test client dengan pemeriksaan CSRF yang diaktifkan, misalkan "client = APIClient(enforce_csrf_checks=True)". Dengan itu, POST tanpa token akan ditolak (403). Sedangkan, POST dengan token yang valid berhasil (201).

## == AI Declaration ==

Note:
Pada tugas 6 ini saya tidak menggunakan AI untuk memberikan kode secara langsung / jiplak-menjiplak.

Strategi Prompting:
Saya menggunakan "ChatGPT" sebagai wadah untuk bertanya terkait hal-hal yang saya tidak bisa temukan lebih lanjut melalui W3School dan sumber lainnya.
Hal tersebut guna mempercepat dan memperjelas pencarian terkait apa yang saya perlukan, serta menghilangkan beberapa error yang terjadi.

Contoh:
Sebagian besar prompting adalah pertanyaan tentang kode pada bagian Tutorial 7.
1. Bisakah Anda menjelaskan bagian program ini dari awal sampai akhir:
```
class ProjectSerializer(serializers.ModelSerializer):
    star_count = serializers.SerializerMethodField()
    is_starred = serializers.SerializerMethodField()
    starred_by_names = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = [
            "id", "title", "description", "tech_stack",
            "project_url", "project_image_url",
            "star_count", "is_starred", "starred_by_names",
        ]
        read_only_fields = ["id"]

    def validate_title(self, value):
        value = strip_tags(value).strip()
        if not value:
            raise serializers.ValidationError("Title cannot be empty.")
        return value

    def validate_description(self, value):
        return strip_tags(value)

    def validate_tech_stack(self, value):
        return strip_tags(value)

    def get_star_count(self, obj):
        return obj.starred_by.count()

    def get_is_starred(self, obj):
        request = self.context.get("request")
        if request is None or not request.user.is_authenticated:
            return False
        return request.user in obj.starred_by.all()

    def get_starred_by_names(self, obj):
        return ", ".join(user.username for user in obj.starred_by.all())
```

Contoh output:
```
Perhatikan tiga baris ini:
star_count = serializers.SerializerMethodField()
is_starred = serializers.SerializerMethodField()
starred_by_names = serializers.SerializerMethodField()

SerializerMethodField adalah field khusus yang nilainya diperoleh dari sebuah method di dalam serializer. Artinya, nilainya tidak harus berasal dari field database.

DRF akan mencari method:
def get_star_count(self, obj):
    return obj.starred_by.count()

obj merupakan object model yang sedang diproses oleh serializer.
Seperti: 
project = Project.objects.get(id=1)

Ketika serializer memproses project tersebut, obj akan merujuk pada project yang sedang diproses.
obj.starred_by.count() menghitung jumlah user yang memberikan star pada project tersebut.

Perhatikan baris fields ini:
fields = [
    "id", "title", "description", "tech_stack",
    "project_url", "project_image_url",
    "star_count", "is_starred", "starred_by_names",
]

Baris tersebut menentukan field mana saja yang boleh muncul dalam serializer.

read_only_fields = ["id"]
Baris tersebut menyatakan bahwa id hanya bisa dibaca, tidak bisa diubah melalui input serializer.
```

Sebagian besar kode saya terinspirasi dari W3School, Django Documentation, serta web-web yang berkaitan.