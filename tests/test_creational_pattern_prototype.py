from patterns.creational_pattern_prototype import Prototype, PrototypeFactory


def test_copy_is_different():
    # given
    prototype = Prototype("test")
    factory = PrototypeFactory()

    # when
    prototype_copy = factory.get_prototype_clone(prototype)

    # then
    assert str(prototype) != str(prototype_copy)
