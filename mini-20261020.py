"""Odds and ends."""

def group_by(items, key):
    out = {}
    for it in items:
        out.setdefault(key(it), []).append(it)
    return out

def flatten(xs):
    return [y for x in xs for y in x]
