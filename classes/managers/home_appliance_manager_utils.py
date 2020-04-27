import operator
from classes.managers.sort_type import SortType
from classes.models.kettle import Kettle
from classes.models.tv import TV
from classes.models.washing_machine import WashingMachine


class HomeApplianceManagerUtils:

    @staticmethod
    def sort_home_appliance_by_power_usage(list_of_home_appliance, sort_type=SortType.ASCENDING):
        """
        Sorts list of objects by power usage
        :param list_of_home_appliance: list
        :param sort_type: SortType
        :return: list
        >>> result = obj.sort_home_appliance_by_power_usage(appliances)
        >>> print(list(map(lambda x: x.__class__.__name__, result)))
        ['Kettle', 'TV', 'WashingMachine']
        """
        if sort_type == SortType.ASCENDING:
            return sorted(list_of_home_appliance, key=operator.attrgetter("power_consumption"))
        elif sort_type == SortType.DESCENDING:
            return sorted(list_of_home_appliance, key=operator.attrgetter("power_consumption"))

    @staticmethod
    def sort_home_appliance_by_name(list_of_home_appliance, sort_type=SortType.ASCENDING):
        """
        Sorts list of objects by name
        :param list_of_home_appliance: list
        :param sort_type: SortType
        :return: list
        >>> result = obj.sort_home_appliance_by_name(appliances)
        >>> print(list(map(lambda x: x.__class__.__name__, result)))
        ['Kettle', 'TV', 'WashingMachine']
        """
        if sort_type == SortType.ASCENDING:
            return sorted(list_of_home_appliance, key=lambda x: x.appliance_name, reverse=False)
        elif sort_type == SortType.DESCENDING:
            return sorted(list_of_home_appliance, key=lambda x: x.appliance_name, reverse=True)

    @staticmethod
    def sort_home_appliance_by_time_usage(list_of_home_appliance, sort_type=SortType.ASCENDING):
        """
        Sorts list of objects by name
        :param list_of_home_appliance: list
        :param sort_type: SortType
        :return: list
        >>> result = obj.sort_home_appliance_by_time_usage(appliances)
        >>> print(list(map(lambda x: x.__class__.__name__, result)))
        ['WashingMachine', 'Kettle', 'TV']
        """
        if sort_type == SortType.ASCENDING:
            list_of_home_appliance.sort(key=lambda x: x.hours_per_month_usage, reverse=False)
            return list_of_home_appliance
        elif sort_type == SortType.DESCENDING:
            list_of_home_appliance.sort(key=lambda x: x.hours_per_month_usage, reverse=True)
            return list_of_home_appliance


if __name__ == '__main__':
    import doctest
    appliance_list = [TV(power_consumption=120.0, appliance_name="Dell", hours_per_month_usage=320.5),
                      Kettle(power_consumption=0.0, appliance_name="Bosch", hours_per_month_usage=100.2),
                      WashingMachine(power_consumption=220.0, appliance_name="Samsung", hours_per_month_usage=20.0)]
    doctest.testmod(verbose=True, extraglobs={"obj": HomeApplianceManagerUtils,
                                              "appliances": appliance_list})
