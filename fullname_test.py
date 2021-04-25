
import fullname

def test_name_score():
    name1 = "Mickey Mouse"
    name2 = "Minny Mouse"

    assert fullname.name_score(name1, name1) == 1.0
    assert fullname.name_score(name1, name2) < 1.0
    assert fullname.name_score(name1, name2) > 0.5
