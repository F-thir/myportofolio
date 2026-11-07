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

> Tugas 6
- Adjusting 'Experience' to match 'Tugas 6' requirements:
    - Implemented Django REST Framework (DRF) for Experience API
    - New Experience Serializer
    - New API Permission System
    - Adjust Experience AJAX with DRF API
- Adjusting 'Projects' to match consistency:
    - New Update Data with Modal
    - New "Edit" button
    - Adjust text, design, and script on HTML


## == PERTANYAAN REFLEKTIF - TUGAS 6 ==
1. Jelaskan apa yang dimaksud dengan REST dan mengapa mengembalikan JSON saja belum cukup untuk menyebut sebuah API sebagai RESTful! Jelaskan pula perbedaan PUT dan PATCH beserta contoh kapan masing-masing sebaiknya digunakan!
2. Jelaskan peran serializer pada Django REST Framework! Apa keuntungannya dibandingkan merakit dictionary secara manual dengan JsonResponse seperti pada Tutorial 05?
3. Jelaskan perbedaan autentikasi dan otorisasi pada Django REST Framework! Mengapa hak akses harus diperiksa dengan permission class di server, bukan hanya dengan menyembunyikan tombol di template?
4. Jelaskan mengapa permintaan yang mengubah data tetap memerlukan token CSRF ketika API memakai SessionAuthentication! Mengapa test yang memakai force_authenticate tidak cukup untuk membuktikan bahwa perlindungan CSRF berjalan?

### Tugas 6
1. 
2. 
3. 
4. 

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