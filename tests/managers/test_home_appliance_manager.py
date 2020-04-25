from unittest import TestCase
from classes.managers.home_appliance_manager import HomeApplianceManager
from classes.models.home_appliance import HomeAppliance


class TestHomeApplianceManager(TestCase):
    def setUp(self):
        self.home_appliance_manager = HomeApplianceManager()
        self.appliance1 = HomeAppliance(appliance_name="Bosch", power_consumption=120, hours_per_month_usage=20.3)
        self.appliance2 = HomeAppliance(appliance_name="Samsung", power_consumption=80, hours_per_month_usage=120.5)
        self.appliance3 = HomeAppliance(appliance_name="Panasonic", power_consumption=75, hours_per_month_usage=74.2)

    def tearDown(self):
        self.home_appliance_manager.list_of_home_appliance.clear()

    def test_add_home_appliance(self):
        self.assertEqual(self.home_appliance_manager.list_of_home_appliance, [])
        self.home_appliance_manager.add_home_appliance(self.appliance1)
        self.assertEqual(self.home_appliance_manager.list_of_home_appliance, [self.appliance1])

    def test_remove_home_appliance_at_index(self):
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance1)
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance2)
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance3)
        self.assertTrue(self.appliance3 in self.home_appliance_manager.list_of_home_appliance)
        self.home_appliance_manager.remove_home_appliance_at_index(2)
        self.assertFalse(self.appliance3 in self.home_appliance_manager.list_of_home_appliance)

    def test_get_home_appliance_at_index(self):
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance1)
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance2)
        self.assertEqual(self.home_appliance_manager.get_home_appliance_at_index(1), self.appliance2)

    def test_add_multiple_home_appliances(self):
        self.assertEqual(self.home_appliance_manager.list_of_home_appliance, [])
        self.home_appliance_manager.add_multiple_home_appliances([self.appliance2, self.appliance3])
        self.assertEqual(self.home_appliance_manager.list_of_home_appliance, [self.appliance2, self.appliance3])

    def test_find_most_costly_home_appliance_by_power_usage(self):
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance1)
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance2)
        result = self.home_appliance_manager.find_most_costly_home_appliance_by_power_usage()
        self.assertEqual(result, self.appliance1)

    def test_summarize_total_money_spent(self):
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance1)
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance1)
        self.assertEqual(self.home_appliance_manager.summarize_total_money_spent(), 64.26)

    def test_summarize_total_power_usage(self):
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance1)
        self.home_appliance_manager.list_of_home_appliance.append(self.appliance1)
        self.assertEqual(self.home_appliance_manager.summarize_total_power_usage(), 4872.0)
