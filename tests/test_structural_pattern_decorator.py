from patterns.structural_pattern_decorator import EthernetPacket, IpPacket, TcpPacket, HttpPacket


def test_network_packets_decorator():
    # given
    ethernet_packet = EthernetPacket()
    ip_packet = IpPacket(ethernet_packet)
    tcp_packet = TcpPacket(ip_packet)
    http_packet = HttpPacket(tcp_packet)

    # when
    result = http_packet.get_structure()

    # then
    assert result == "[ethernet][ip][tcp][http]"
