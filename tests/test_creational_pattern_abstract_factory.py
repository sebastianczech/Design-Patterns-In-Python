from patterns.creational_pattern_abstract_factory import FactoryCisco


def test_cisco_port_chassis():
    # given
    cisco_factory = FactoryCisco()
    cisco_port = cisco_factory.create_port()
    cisco_chassis = cisco_factory.create_chassis()

    # when
    info_port = cisco_port.info()
    info_chassis = cisco_chassis.info()

    # then
    assert info_port == "Port Cisco"
    assert info_chassis == "Chassis Cisco"
