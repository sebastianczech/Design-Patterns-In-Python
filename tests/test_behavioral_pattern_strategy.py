from patterns.behavioral_pattern_strategy import DhcpOfferIpv4Strategy, DhcpOfferContext


def test_ipv4_strategy():
    # given
    ip4_strategy = DhcpOfferIpv4Strategy()
    dhcp_offer = DhcpOfferContext(ip4_strategy)

    # when
    result = dhcp_offer.context_offer_ip()

    # then
    assert result == "127.0.0.1"


def test_ipv6_strategy():
    # given
    ip6_strategy = DhcpOfferIpv4Strategy()
    dhcp_offer = DhcpOfferContext(ip6_strategy)

    # when
    result = dhcp_offer.context_offer_ip()

    # then
    assert result == "127.0.0.1"
