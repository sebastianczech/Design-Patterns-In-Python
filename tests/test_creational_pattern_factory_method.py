from patterns.creational_pattern_factory_method import JuniperRouter, CiscoRouter


def test_protocol_bgp():
    # given
    router = CiscoRouter()

    # when
    name = router.routing_protocol.protocol_name()

    # then
    assert name == "BGP"


def test_protocol_ospf():
    # given
    router = JuniperRouter()

    # when
    name = router.routing_protocol.protocol_name()

    # then
    assert name == "OSPF"
