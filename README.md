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

## == PERTANYAAN REFLEKTIF - TUGAS 5 ==
1. Jelaskan apa itu debouncing dan mengapa teknik ini penting diterapkan pada fitur pencarian yang menggunakan AJAX!
2. Jelaskan fungsi dari penggunaan await ketika kita menggunakan fetch()! Apa yang akan terjadi jika kita tidak menggunakan await?
3. Jelaskan apa itu serangan XSS (Cross-Site Scripting) dan mengapa data yang ditampilkan melalui AJAX/JavaScript lebih rentan terhadap serangan ini daripada data yang ditampilkan langsung melalui template Django!

## == AI Declaration ==

Note:
Pada tugas 5 ini saya tidak menggunakan AI untuk memberikan kode secara langsung / jiplak-menjiplak.

Strategi Prompting:
Saya menggunakan "ChatGPT" sebagai wadah untuk bertanya terkait hal-hal yang saya tidak bisa temukan lebih lanjut melalui W3School dan sumber lainnya.
Hal tersebut guna mempercepat dan memperjelas pencarian terkait apa yang saya perlukan, serta menghilangkan beberapa error yang terjadi.

Contoh:
1. Bisakah anda menjelaskan konsep Django Admin untuk permission?
Disini AI menjawab dan menjelaskan konsep User dan Group:

Contoh hasil prompt:
    Pada model Electronics
    class Electronics(models.Model):
        name = models.CharField(max_length=...)
        ...

    Django otomatis membuat permission:
    add_electronics
    change_electronics
    delete_electronics
    view_electronics

    Pada Django Admin, Anda bisa membuat group yang menggunakan beberapa permission tersebut.

Sebagian besar kode saya terinspirasi dari W3School, Django Documentation, serta web-web yang berkaitan.