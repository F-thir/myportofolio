from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Skill


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Staff - Pengabdian Masyarakat BEM Fasilkom",
            description="Person in Charge (PIC) of Dorakula (Donor Darah Abis Kuliah), a blood donation program held twice. Managed various aspects of event preparation and coordination, including documentation, media requests, and financial administration such as preparing budget proposals (RAB). Additionally, served as a mentor for Interkom, an educational event involving members of the Fasilkom UI community.",
            category="part-time",
        )

        self.skill = Skill.objects.create(
            title="Python",
            description="Bahasa pemrograman yang saya gunakan untuk mempelajari konsep dasar pemrograman dan Object-Oriented Programming.",
            category="programming",
            image="https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg",
            details="Di sini, saya mempelajari dasar-dasar pemrograman Python, mulai dari konsep dasar hingga Object-Oriented Programming (OOP), seperti class, object, inheritance, dan berbagai konsep lainnya. Python mulai saya pelajari sejak semester 1 melalui DDP-0 dan DDP-1, ketika saya pertama kali menjadi mahasiswa Fasilkom UI pada tahun 2025."
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertNotContains(response, self.skill.title)
        self.assertContains(response, f'href="{reverse("main:show_skill")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Staff - Pengabdian Masyarakat BEM Fasilkom")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_skill_model(self):
        self.assertEqual(str(self.skill), "Python")
        self.assertEqual(self.skill.category, "programming")
        self.assertEqual(self.skill.description, "Bahasa pemrograman yang saya gunakan untuk mempelajari konsep dasar pemrograman dan Object-Oriented Programming.")
        self.assertEqual(self.skill.image, "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg")
        self.assertEqual(self.skill.details, "Di sini, saya mempelajari dasar-dasar pemrograman Python, mulai dari konsep dasar hingga Object-Oriented Programming (OOP), seperti class, object, inheritance, dan berbagai konsep lainnya. Python mulai saya pelajari sejak semester 1 melalui DDP-0 dan DDP-1, ketika saya pertama kali menjadi mahasiswa Fasilkom UI pada tahun 2025.")

    def test_skill_page(self):
        response = self.client.get(reverse("main:show_skill"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "skill.html")
        self.assertContains(response, self.skill.title)
        self.assertContains(response, self.skill.description)
        self.assertContains(response, "Programming")
        self.assertContains(response, "Bahasa pemrograman yang saya gunakan untuk mempelajari konsep dasar pemrograman dan Object-Oriented Programming.")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_skill_page(self):
        Skill.objects.all().delete()
        response = self.client.get(reverse("main:show_skill"))
        self.assertContains(response, "Belum ada skill yang ditambahkan.")