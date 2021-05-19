from patterns.structural_pattern_proxy import HttpApache, HttpProxy


def test_network_packets_decorator():
    # given
    http_apache = HttpApache()
    http_proxy = HttpProxy(http_apache)

    # when
    result = http_proxy.download_file()

    # then
    assert result == "[proxy header][apache header]"
