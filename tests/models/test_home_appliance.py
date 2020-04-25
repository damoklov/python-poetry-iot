from unittest import TestCase

from classes.models.home_appliance import HomeAppliance


class TestHomeAppliance(TestCase):
    def setUp(self):
        self.home_appliance = HomeAppliance(power_consumption=80, hours_per_month_usage=120.5)

    def test_compute_final_money_spent_per_month_in_usd(self):
        self.assertEqual(self.home_appliance.compute_final_money_spent_per_month_in_usd(), 127.15)

    def test_compute_final_power_consumption_per_month_in_watts(self):
        self.assertEqual(self.home_appliance.compute_final_power_consumption_per_month_in_watts(), 9640.0)
