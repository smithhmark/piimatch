import itertools

def _normalize_token_lists(tokens1, tokens2):
    tcnt1 = len(tokens1)
    tcnt2 = len(tokens2)
    if tcnt1 < tcnt2:
        left = tokens2[:]
        right = tokens1[:]
        right.extend( [None] * (tcnt2 - tcnt1))
    elif tcnt1 > tcnt2:
        left = tokens1[:]
        right = tokens2[:]
        right.extend( [None] * (tcnt2 - tcnt1))
    else:
        left = tokens1[:]
        right = tokens2[:]
    return left, right

def _best_of_many(left, rights, cmp, threshold):
    fnd_idx = -1
    best_score = -1.0
    for ii, right in enumerate(rights):
        if right is not None:
            score = cmp(left, right)
            if score > threshold:
                if score > best_score:
                    best_score = score
                    fnd_idx = ii
    return best_score, fnd_idx

def _longbiased_multitoken_matcher(
        tokens1,
        tokens2,
        comparison=None,
        threshold=0.5
        ):
    cmp = comparison
    if comparison is None:
        cmp = lambda x, y: int(x == y)
    left, right = _normalize_token_lists(tokens1, tokens2)
    scores = []
    misses = 0
    for lt in left:
        sc, idx = _best_of_many(lt, right, cmp, .1)
        if idx != -1:
            #print(f"[debug]\t{lt} matched with score {sc} aginst {right[idx]}")
            right.pop(idx)
        else:
            misses += 1
        scores.append(sc)
    net_score = sum(scores)/len(scores) 
    return net_score

def _ngrams(n, cs):
    if n >= len(cs):
        return [ cs[:]]
    grams = []
    for end_index in range(n, len(cs)+1):
        grams.append(cs[end_index-n:end_index])
    return grams


def how_many_ngrams(n, length):
     return max(1, length - n + 1)

def ngram_score(n, str1, str2):
    possible = how_many_ngrams(n, max(len(str1), len(str2)))
    left = set(_ngrams(n, str1))
    right = set(_ngrams(n, str2))
    incommon = len(left & right)
    return incommon/possible

def name_score(name1, name2):
    if name1 == name2:
        return 1.0
    tok1 = name1.split()
    tok2 = name2.split()
    return _longbiased_multitoken_matcher(tok1, tok2, lambda x,y: ngram_score(2, x,y), 0.5)
