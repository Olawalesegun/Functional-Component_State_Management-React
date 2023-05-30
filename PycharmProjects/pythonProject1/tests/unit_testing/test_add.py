from oop.add import add_up

#   PYTEST HERE
def test_add():
    assert add_up(5, 6) == 11
    result = add_up("David", " Esther") == "David Esther"
    assert type(result) == str
    assert "David" in resul
