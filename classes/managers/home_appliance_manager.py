from classes.managers import sort_type
from classes.managers.home_appliance_manager_utils import HomeApplianceManagerUtils
from classes.models.home_appliance import HomeAppliance


class HomeApplianceManager:
    """
    >>> HomeApplianceManager().__class__.__name__
    'HomeApplianceManager'
    >>> obj.add_home_appliance(appliance1)
    >>> obj.add_home_appliance(appliance2)
    >>> obj.add_home_appliance(appliance3)
    """
    def __init__(self, list_of_home_appliance=None):
        if list_of_home_appliance is None:
            list_of_home_appliance = list()
        self._list_of_home_appliance = list_of_home_appliance

    def add_home_appliance(self, home_appliance):
        """
        Adds one object into list
        :param home_appliance: HomeAppliance
        :return: None
        >>> len(obj.list_of_home_appliance)
        3
        >>> obj.add_home_appliance(appliance1)
        >>> len(obj.list_of_home_appliance)
        4
        """
        self._list_of_home_appliance.append(home_appliance)

    def remove_home_appliance_at_index(self, index):
        """
        Removes object in list by given index
        :param index: int
        :return: None
        >>> obj.list_of_home_appliance[1] is appliance2
        True
        >>> obj.remove_home_appliance_at_index(1)
        >>> obj.list_of_home_appliance[1] is appliance2
        False
        """
        self._list_of_home_appliance.pop(index)

    def get_home_appliance_at_index(self, index):
        """
        Retrieves object from list by given index
        :param index: int
        :return: HomeAppliance
        >>> obj.get_home_appliance_at_index(2).appliance_name
        'Apple'
        """
        return self._list_of_home_appliance[index]

    def add_multiple_home_appliances(self, list_to_add):
        """
        Updates current list with items from new list
        :param list_to_add: list
        :return: None
        >>> len(obj.list_of_home_appliance)
        4
        >>> obj.add_multiple_home_appliances([appliance1, appliance2])
        >>> len(obj.list_of_home_appliance)
        6
        """
        self._list_of_home_appliance.extend(list_to_add)

    def find_most_costly_home_appliance_by_power_usage(self):
        """
        Finds most expensive appliance by power usage
        :return: None/HomeAppliance
        >>> obj.find_most_costly_home_appliance_by_power_usage().appliance_name
        'Dell'
        """
        result = HomeApplianceManagerUtils.sort_home_appliance_by_power_usage(self._list_of_home_appliance)
        try:
            return result[-1]
        except IndexError:
            return None

    def summarize_total_money_spent(self):
        """
        Sums up total cost of appliance per month
        :return: float
        >>> obj.summarize_total_money_spent()
        128.77
        """
        return sum([x.compute_final_money_spent_per_month_in_usd() for x in self._list_of_home_appliance])

    def summarize_total_power_usage(self):
        """
        Sums up total power used per month
        :return: float
        >>> obj.summarize_total_power_usage()
        9762.0
        """
        return sum([x.compute_final_power_consumption_per_month_in_watts() for x in self._list_of_home_appliance])

    @property
    def list_of_home_appliance(self):
        return self._list_of_home_appliance

    @list_of_home_appliance.setter
    def list_of_home_appliance(self, list_of_home_appliance):
        self._list_of_home_appliance = list_of_home_appliance


if __name__ == '__main__':
    import doctest
    appliance1 = HomeAppliance(appliance_name="Dell", power_consumption=100.0, hours_per_month_usage=23.5)
    appliance2 = HomeAppliance(appliance_name="Kettle", power_consumption=0.0, hours_per_month_usage=120.0)
    appliance3 = HomeAppliance(appliance_name="Apple", power_consumption=60.0, hours_per_month_usage=45.2)
    doctest.testmod(verbose=True, extraglobs={"obj": HomeApplianceManager(),
                                              "appliance1": appliance1,
                                              "appliance2": appliance2,
                                              "appliance3": appliance3})
