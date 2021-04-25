import pytest
import math

import fullname


def test_normalize_token_lists():
    l1 = ["a", "b"]
    l2 = ["x","y","z"]
    left, right = fullname._normalize_token_lists(l1, l2)
    assert len(left) == len(right)
    assert left[0] == "x"
    assert right[-1] is None

def _int_match(x,y):
    return min(x,y)/max(x,y)

def test_best_of_many():
    left = 123
    rights1 = [ 1, 2, 3, ]
    rights2 = [ 10, 120, 102, 3, ]

    score, idx = fullname._best_of_many(
            left,
            rights1,
            _int_match,
            .5)
    assert score == -1.0
    assert idx == -1

    score, idx = fullname._best_of_many(
            left,
            rights2,
            _int_match,
            0.5)
    assert score < 1.0 and score > .95
    assert idx == 1

def test_longbiased_multitoken_matcher():
    left = [1 ,2, ]
    right= [1, 2]
    rcvd = fullname._longbiased_multitoken_matcher(left, right, _int_match)
    assert rcvd == 1.0

def test_name_score():
    name1 = "Mickey Mouse"
    name2 = "Minny Mouse"

    assert fullname.name_score(name1, name1) == 1.0
    assert fullname.name_score(name2, name2) == 1.0
    score = fullname.name_score(name1, name2)
    print(score)
    assert score < 1.0
    assert score > 0.5
    assert score == 0.6

def test_ngram_score():
    xs = "abcde"
    ys = "abcde"
    assert fullname.ngram_score(2, xs, ys) == 1.0

    xs = "abcde"
    ys = "zbcde"
    assert fullname.ngram_score(2, xs, ys) == 0.75
