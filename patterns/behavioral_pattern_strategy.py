import abc


class IpAddress():
    def __init__(self, ip):
        self.ip = ip

    def get_ip(self):
        return self.ip


class DhcpOfferIpStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def offer_ip(self):
        pass


class DhcpOfferIpv4Strategy(DhcpOfferIpStrategy):
    def offer_ip(self):
        return IpAddress("127.0.0.1").get_ip()


class DhcpOfferIpv6Strategy(DhcpOfferIpStrategy):
    def offer_ip(self):
        return IpAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334").get_ip()


class DhcpOfferContext():
    def __init__(self, strategy):
        self._strategy = strategy

    def context_offer_ip(self):
        return self._strategy.offer_ip()


def main():
    ip4_strategy = DhcpOfferIpv4Strategy()
    dhcp_offer = DhcpOfferContext(ip4_strategy)
    print(dhcp_offer.context_offer_ip())


if __name__ == "__main__":
    main()
