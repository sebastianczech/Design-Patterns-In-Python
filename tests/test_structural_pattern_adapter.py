from patterns.structural_pattern_adapter import AdapterAuthenticationManager


def test_authentication_adapter():
    # given
    adapter = AdapterAuthenticationManager()

    # when
    result = adapter.authenticate_request("aE9281")

    # then
    assert result == "authenticate by token: aE9281"
