from django.test import TestCase
from .models import SuperHero, Publisher, Team

# Create your tests here.


def CreateTeam(name, desc):
    # team = Team(name=name, description=desc)
    # team.save()
    # data = Team.objects.all()
    # # for d in data:
    # #     print(d.name)
    # #     print(d.description)
    # # print(data)
    # return data
    return Team.objects.create(name=name, description=desc) # simply create one object and return it, aboove method returns all the entries i.e. dictionary


def Createpublisher(name, desc):
    return Publisher.objects.create(name=name, description=desc)


def CreateSuperHero(name, bio, pub, alt_ego, sup_pow, team):
    return SuperHero.objects.create(name=name, biography=bio, publisher=pub, alter_ego=alt_ego, superpowers=sup_pow, team_affiliation=team)


# CreateTeam('marvel', 'marvel team description')

class TeamModelTests(TestCase):
    def test_add_entry(self):
        data = CreateTeam('marvel', 'marvel team description')
        # print(data)
        # print(data.name)
        # print(data.description)
        self.assertIs(data.name, 'marvel')
        self.assertIs(data.description, 'marvel team description')

    def test_update_entry(self):
        data = CreateTeam('marvel', 'marvel team description')
        # print(data)
        # print(data.name)
        # print(data.description)
        data.name = 'marvel updated'
        data.description = 'marvel team description updated'
        # print(data)
        # print(data.name)
        # print(data.description)
        self.assertIs(data.name, 'marvel updated')
        self.assertIs(data.description, 'marvel team description updated')

    def test_delete_entry(self):
        CreateTeam('marvel', 'marvel team description')
        count = Team.objects.all().count()
        # print('count before : ', count)
        self.assertIs(count, 1)
        Team.objects.get(name='marvel').delete()
        count = Team.objects.all().count()
        # print('count after : ', count)
        self.assertIs(count, 0)


class PublisherModelTest(TestCase):
    def test_add_entry(self):
        data = Createpublisher('chetan', 'chetan publication')
        # print(data)
        # print(data.name)
        # print(data.description)
        self.assertIs(data.name, 'chetan')
        self.assertIs(data.description, 'chetan publication')

    def test_update_entry(self):
        data = Createpublisher('chetan', 'chetan publication')
        # print(data)
        # print(data.name)
        # print(data.description)
        data.name = 'chetan updated'
        data.description = 'chetan publication updated'
        # print(data)
        # print(data.name)
        # print(data.description)
        self.assertIs(data.name, 'chetan updated')
        self.assertIs(data.description, 'chetan publication updated')

    def test_delete_entry(self):
        Createpublisher('chetan', 'chetan publication')
        count = Publisher.objects.all().count()
        # print('count before : ', count)
        self.assertIs(count, 1)
        Publisher.objects.get(name='chetan').delete()
        count = Publisher.objects.all().count()
        # print('count after : ', count)
        self.assertIs(count, 0)


class SuperHeroModelTest(TestCase):
    def test_add_entry(self):
        t = CreateTeam('marvel', 'marvel team description')
        pub = Createpublisher('chetan', 'chetan publication')

        # t = Team(name='marvel', description='marvel team description')
        # t.save()
        # pub = Publisher(name='chetan', description='chetan publication')
        # pub.save()
        # print(t.name, t.description, pub.name, pub.description)
        # print(Team.objects.all().count())
        # print(Publisher.objects.all().count())

        data = SuperHero(name='Iron Man', biography='test bio', alter_ego='test alter ego', superpowers='test superpowers')
        # count = SuperHero.objects.all().count()
        # print(count)
        data.save()
        # count = SuperHero.objects.all().count()
        # print(count)
        data.publisher.add(pub)
        data.team_affiliation.add(t)
        # print(SuperHero.objects.all().values())
        # print(data.publisher.all())
        # print(data.team_affiliation.all())
        self.assertIs(data.name, 'Iron Man')
        self.assertIs(data.biography, 'test bio')
        self.assertIs(data.alter_ego, 'test alter ego')
        self.assertIs(data.superpowers, 'test superpowers')

    def test_update_entry(self):
        t = CreateTeam('marvel', 'marvel team description')
        pub = Createpublisher('chetan', 'chetan publication')
        data = SuperHero(name='Iron Man', biography='test bio', alter_ego='test alter ego', superpowers='test superpowers')
        data.save()
        data.publisher.add(pub)
        data.team_affiliation.add(t)

        data.name = 'Iron Man updated'
        data.biography = 'test bio updated'

        self.assertIs(data.name, 'Iron Man updated')
        self.assertIs(data.biography, 'test bio updated')

    def test_delete_entry(self):
        t = CreateTeam('marvel', 'marvel team description')
        pub = Createpublisher('chetan', 'chetan publication')
        data = SuperHero(name='Iron Man', biography='test bio', alter_ego='test alter ego', superpowers='test superpowers')
        data.save()
        data.publisher.add(pub)
        data.team_affiliation.add(t)

        count = SuperHero.objects.all().count()
        print('count before : ', count)
        self.assertIs(count, 1)
        SuperHero.objects.get(name='Iron Man').delete()
        count = SuperHero.objects.all().count()
        # print('count after : ', count)
        self.assertIs(count, 0)