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

## == PERTANYAAN REFLEKTIF - TUGAS 4 ==
Pada tugas 4, tidak ada pertanyaan reflektif.

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