from patterns.creational_pattern_singleton import HomeNetworkParameters


def test_home_network_is_the_same_for_all_instances():
    home1 = HomeNetworkParameters()
    home2 = HomeNetworkParameters()
    assert home1 is home2
