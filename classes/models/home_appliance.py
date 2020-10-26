import distutils


class HomeAppliance:
    """
    >>> HomeAppliance().__class__.__name__
    'HomeAppliance'
    """
    price_per_watt = 0.01319

    def __init__(self, power_consumption=0, hours_per_month_usage=0.0,
                 repair_price=0.0, location_in_house='N/A',
                 appliance_name='N/A', plugged_into_socket=False):
        self._power_consumption = int(power_consumption)
        self._hours_per_month_usage = float(hours_per_month_usage)
        self._repair_price = float(repair_price)
        self._location_in_house = str(location_in_house)
        self._appliance_name = str(appliance_name)
        self._plugged_into_socket = bool(int(plugged_into_socket))

    def compute_final_money_spent_per_month_in_usd(self):
        """
        Summarizes money spent per month
        :return: float
        >>> obj.compute_final_money_spent_per_month_in_usd()
        237.74
        """
        price = HomeAppliance.price_per_watt * self._power_consumption * self._hours_per_month_usage
        return round(price, 2)

    def compute_final_power_consumption_per_month_in_watts(self):
        """
        Summarizes total power consumption per month
        :return: float
        >>> obj.compute_final_power_consumption_per_month_in_watts()
        18024.0
        """
        consumption = self._power_consumption * self._hours_per_month_usage
        return round(consumption, 4)

    @staticmethod
    def boolean_to_string(needs_socket: bool):
        return 'Yes' if needs_socket else 'No'

    def __str__(self):
        consumption = "Consumption: {0}\n".format(self._power_consumption)
        hours = "Hours per month: {0}\n".format(self._hours_per_month_usage)
        repair = "Repair price: {0}\n".format(self._repair_price)
        location = "Location: {0}\n".format(self._location_in_house)
        name = "Appliance name: {0}\n".format(self._appliance_name)
        plugged = "Needs socket: {0}\n".format(self._plugged_into_socket)
        price = "Price per watt: {0}\n".format(HomeAppliance.price_per_watt)
        return consumption + hours + repair + location + name + plugged + price

    @property
    def power_consumption(self):
        return self._power_consumption

    @power_consumption.setter
    def power_consumption(self, power_consumption):
        self._power_consumption = power_consumption

    @property
    def hours_per_month_usage(self):
        return self._hours_per_month_usage

    @hours_per_month_usage.setter
    def hours_per_month_usage(self, hours_per_month_usage):
        self._hours_per_month_usage = hours_per_month_usage

    @property
    def repair_price(self):
        return self._repair_price

    @repair_price.setter
    def repair_price(self, repair_price):
        self._repair_price = repair_price

    @property
    def location_in_house(self):
        return self._location_in_house

    @location_in_house.setter
    def location_in_house(self, location_in_house):
        self._location_in_house = location_in_house

    @property
    def appliance_name(self):
        return self._appliance_name

    @appliance_name.setter
    def appliance_name(self, appliance_name):
        self._appliance_name = appliance_name

    @property
    def plugged_into_socket(self):
        return self._plugged_into_socket

    @plugged_into_socket.setter
    def plugged_into_socket(self, plugged_into_socket):
        self._plugged_into_socket = plugged_into_socket


if __name__ == '__main__':
    import doctest
    obj = HomeAppliance(120, 150.2, 12.15, 'Kitchen', 'Bosch', False)
    doctest.testmod(verbose=True, extraglobs={"obj": obj})
