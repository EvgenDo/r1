from django.test import TestCase
from models import tUser, tWaybill, tCompany, tGoods
import time

class TestUser(TestCase):

    def setUp(self, name = 'Jhon Smith', sign = 0):
        return tUser.objects.create(cName = name, cSignCode = sign)

    def test_fullname(self):
        testUser = self.setUp()
        s = testUser.cName
        name, surname = s.split(" ", 1)
        self.assertEqual(testUser.cName, name+" "+surname)

    def test_insert(self):
        testName = "Ivan Ivanovich"
        testUser = self.setUp(name = testName)
        testUser.save()
        self.assertEqual(testUser, tUser.objects.get(cName = testName))

    def test_select(self):
        testName = "Ivan Ivanovich"
        testUser = self.setUp(name = testName)
        testUser.save()
        selectedVal = tUser.objects.get(cName = testName)
        self.assertEqual(testName, selectedVal.cName)

    def test_edit(self):
        testName = "Ivan Ivanovich"
        testUser = self.setUp(name = testName)
        testUser.save()
        editName = "Evgen Ivanovich"
        testUser.cName = editName
        testUser.save()
        self.assertNotEqual(testUser.cName, testName)

class TestWaybill(TestCase):

    def setUp(self, total = 1,
              compToName = "HungStudsInc",
              compFromName = "Star Bars",
              userToName = "Jhon Smith",
              userFromName = "Anon Nimus"
              ):
        compTo = tCompany.objects.create(cName = compToName, cAdress = "Mars 1/2")
        compFrom = tCompany.objects.create(cName = compFromName, cAdress = "Far-Fat in Far Space")
        userTo = tUser.objects.create(cName = userToName, cSignCode = 423)
        userFrom = tUser.objects.create(cName = userFromName, cSignCode = 000)
        return tWaybill.objects.create(cCompToID = compTo,
                                       cCompFromID = compFrom,
                                       cToID = userTo,
                                       cFromID = userFrom,
                                       cDate = time.strftime("%Y-%m-%d %H:%M"),
                                       cTotal = total)

    def test_sum(self):
        wb = self.setUp(100)
        self.assertTrue(wb.cTotal > 0)
        self.assertFalse(wb.cTotal < 0)

    def test_delete(self):
        wb = self.setUp()
        wbid = wb.id
        compTo = tCompany.objects.get(id = wb.cCompToID.id)
        compFrom = tCompany.objects.get(id = wb.cCompFromID.id)
        userTo = tUser.objects.get(id = wb.cToID.id)
        userFrom = tUser.objects.get(id = wb.cFromID.id)
        self.assertIsNotNone(wb)
        self.assertIsNotNone(compTo)
        self.assertIsNotNone(compFrom)
        self.assertIsNotNone(userTo)
        self.assertIsNotNone(userFrom)
        wb.delete()
        try:
            wb = tWaybill.objects.get(id = wbid)
        except tWaybill.DoesNotExist:
            wb = None
        self.assertIsNone(wb)
        self.assertIsNotNone(compTo)
        self.assertIsNotNone(compFrom)
        self.assertIsNotNone(userTo)
        self.assertIsNotNone(userFrom)