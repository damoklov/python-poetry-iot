from unittest import TestCase
from classes.models.home_appliance import HomeAppliance
from classes.managers.home_appliance_manager_utils import HomeApplianceManagerUtils


class TestHomeApplianceManagerUtils(TestCase):
    def setUp(self):
        self.appliance1 = HomeAppliance(appliance_name="Bosch", power_consumption=120, hours_per_month_usage=20.3)
        self.appliance2 = HomeAppliance(appliance_name="Samsung", power_consumption=80, hours_per_month_usage=120.5)
        self.appliance3 = HomeAppliance(appliance_name="Panasonic", power_consumption=75, hours_per_month_usage=74.2)
        self.home_appliance_manager_utils = HomeApplianceManagerUtils
        self.home_appliance_list = [self.appliance1, self.appliance2, self.appliance3]

    def tearDown(self):
        self.home_appliance_list.clear()

    def test_sort_home_appliance_by_power_usage(self):
        result = self.home_appliance_manager_utils.sort_home_appliance_by_power_usage(self.home_appliance_list)
        for index in range(len(result)-1):
            self.assertTrue(result[index].power_consumption < result[index+1].power_consumption)

    def test_sort_home_appliance_by_name(self):
        result = self.home_appliance_manager_utils.sort_home_appliance_by_name(self.home_appliance_list)
        for index in range(len(result) - 1):
            self.assertTrue(result[index].appliance_name < result[index + 1].appliance_name)

    def test_sort_home_appliance_by_time_usage(self):
        result = self.home_appliance_manager_utils.sort_home_appliance_by_time_usage(self.home_appliance_list)
        print(self.home_appliance_list)
        for index in range(len(result) - 1):
            self.assertTrue(result[index].hours_per_month_usage < result[index + 1].hours_per_month_usage)
