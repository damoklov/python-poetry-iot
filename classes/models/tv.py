from classes.models.quality import Quality
from classes.models.home_appliance import HomeAppliance


class TV(HomeAppliance):
    """
    >>> TV().__class__.__name__
    'TV'
    """
    def __init__(self, power_consumption=0, hours_per_month_usage=0.0,
                 repair_price=0.0, location_in_house='N/A',
                 appliance_name='N/A', plugged_into_socket=False,
                 quality=Quality.HD, num_channels_available=0):
        super().__init__(power_consumption, hours_per_month_usage,
                         repair_price, location_in_house,
                         appliance_name, plugged_into_socket)
        self._quality = quality
        self._num_channels_available = num_channels_available

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, quality):
        self._quality = quality

    @property
    def num_channels_available(self):
        return self._num_channels_available

    @num_channels_available.setter
    def num_channels_available(self, num_channels_available):
        self._num_channels_available = num_channels_available


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
