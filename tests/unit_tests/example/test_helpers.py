from example.helpers import who_let_the_dogs_out


def test_who_let_the_dogs_out():
    assert who_let_the_dogs_out() == ["who", "who", "who", "who?!"]
