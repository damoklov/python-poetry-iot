from classes.models.home_appliance import HomeAppliance


class WashingMachine(HomeAppliance):
    """
    >>> WashingMachine().__class__.__name__
    'WashingMachine'
    """
    def __init__(self, power_consumption=0, hours_per_month_usage=0.0,
                 repair_price=0.0, location_in_house='N/A',
                 appliance_name='N/A', plugged_into_socket=False,
                 washing_time=0.0, item_capacity=0):
        super().__init__(power_consumption, hours_per_month_usage,
                         repair_price, location_in_house,
                         appliance_name, plugged_into_socket)
        self._washing_time = washing_time
        self._item_capacity = item_capacity

    @property
    def washing_time(self):
        return self._washing_time

    @washing_time.setter
    def washing_time(self, washing_time):
        self._washing_time = washing_time

    @property
    def item_capacity(self):
        return self._item_capacity

    @item_capacity.setter
    def item_capacity(self, item_capacity):
        self._item_capacity = item_capacity


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
