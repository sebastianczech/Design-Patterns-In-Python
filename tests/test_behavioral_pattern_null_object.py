from patterns.behavioral_pattern_null_object import VlanEncapsulationData


def test_dot1q_encap():
    # given
    vlanEncap = VlanEncapsulationData()

    # when
    result = vlanEncap.prepare_encapsulation("dot1q").get_encapsulation_name()

    # then
    assert result == "dot1q"


def test_not_existing_encap():
    # given
    vlanEncap = VlanEncapsulationData()

    # when
    result = vlanEncap.prepare_encapsulation("not_existing_encap").get_encapsulation_name()

    # then
    assert result == ""
