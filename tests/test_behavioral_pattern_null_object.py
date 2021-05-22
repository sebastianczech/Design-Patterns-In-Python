from patterns.behavioral_pattern_null_object import VlanEncapsulationData


def test_dot1q_encap():
    # given
    vlanEncap = VlanEncapsulationData()

    # when
    result = vlanEncap.getEncapsulation("dot1q").getEncapsulation()

    # then
    assert result == "dot1q"


def test_not_existing_encap():
    # given
    vlanEncap = VlanEncapsulationData()

    # when
    result = vlanEncap.getEncapsulation("not_existing_encap").getEncapsulation()

    # then
    assert result == ""
