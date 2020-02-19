from django.test import TestCase
from .models import Profile,Projects


class ProfileTestClass(TestCase):
    def setUp(self):
        self.Loise = Profile(profile_photo='default.jpg',bio='Junior Software Developer', phone_number='0796579620')

    def test_instance(self):
        self.assertTrue(isinstance(self.Loise,Profile))

    def test_save(self):
        self.Loise.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
 

class ProjectsTestClass(TestCase):
    def setUp(self):
        self.Loise = Profile()
        self.Loise.save_profile()

        self.new_project =Projects(description="testing testing 1,2",profile=self.Loise)
        self.new_project.save()

    def tearDown(self):
        Profile.objects.all().delete()
        Projects.objects.all().delete()    

    def test_projects(self):
        projects = Projects.objects.all()
        self.assertTrue(len(projects)>0)
# Create your tests here.
