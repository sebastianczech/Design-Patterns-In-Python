from patterns.creational_pattern_builder import PortConfiguratorNoEncap100Mb, PortConfiguratorDot1qEncap1Gb, \
    NetworkController


def test_port_100mb_no_encap():
    # given
    port_conf_no_enc_100mb = PortConfiguratorNoEncap100Mb()
    network_controller = NetworkController()
    network_controller.prepare_port_configuration(port_conf_no_enc_100mb)

    # when
    port = port_conf_no_enc_100mb.port

    # then
    assert port.speed == "100 Mbps"
    assert port.encapsulation == "none"


def test_port_1gb_dot1q_encap():
    # given
    port_conf_dot1q_encap_1gb = PortConfiguratorDot1qEncap1Gb()
    network_controller = NetworkController()
    network_controller.prepare_port_configuration(port_conf_dot1q_encap_1gb)

    # when
    port = port_conf_dot1q_encap_1gb.port

    # then
    assert port.speed == "1 Gbps"
    assert port.encapsulation == "dot1q"
