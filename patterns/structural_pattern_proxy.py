import abc


class HttpServer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def download_file(self):
        pass


class HttpProxy(HttpServer):
    def __init__(self, http_server):
        self.http_server = http_server

    def download_file(self):
        return "[proxy header]" + self.http_server.download_file()


class HttpApache(HttpServer):
    def download_file(self):
        return "[apache header]"


def main():
    http_apache = HttpApache()
    http_proxy = HttpProxy(http_apache)
    print(http_proxy.download_file())


if __name__ == "__main__":
    main()
