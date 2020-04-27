from classes.models.home_appliance import HomeAppliance


class Kettle(HomeAppliance):
    """
    >>> Kettle().__class__.__name__
    'Kettle'
    """
    def __init__(self, power_consumption=0, hours_per_month_usage=0.0,
                 repair_price=0.0, location_in_house='N/A',
                 appliance_name='N/A', plugged_into_socket=False,
                 time_to_boil=0.0, water_capacity=0.0):
        super().__init__(power_consumption, hours_per_month_usage,
                         repair_price, location_in_house,
                         appliance_name, plugged_into_socket)
        self._time_to_boil = time_to_boil
        self._water_capacity = water_capacity

    @property
    def time_to_boil(self):
        return self._time_to_boil

    @time_to_boil.setter
    def time_to_boil(self, time_to_boil):
        self._time_to_boil = time_to_boil

    @property
    def water_capacity(self):
        return self._water_capacity

    @water_capacity.setter
    def water_capacity(self, water_capacity):
        self._water_capacity = water_capacity


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)