import abc


class AdapterContractAuthenticationManager(metaclass=abc.ABCMeta):
    def __init__(self):
        self._adaptee = AdapteeAuthenticationService()

    @abc.abstractmethod
    def authenticate_request(self, token):
        pass


class AdapterAuthenticationManager(AdapterContractAuthenticationManager):
    def authenticate_request(self, token):
        return self._adaptee.authenticate(token)


class AdapteeAuthenticationService:
    def authenticate(self, token):
        return "authenticate by token: " + token


def main():
    adapter = AdapterAuthenticationManager()
    print(adapter.authenticate_request("aE9281"))


if __name__ == "__main__":
    main()
