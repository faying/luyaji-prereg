"""Scores the cold-number preregistration (rules/cold-v1.md) on forward draws.

    python -m pipeline.cold_prereg --first-issue <issue from lab/cold-v1-freeze.md> [--history data/history.json]

Prints cumulative hits until the sample is complete; Z and p exist only once all 300 draws are in.
"""
import argparse
import json
import math
from collections import Counter

N = 300
COLD = 6
MEAN = 36 / 33
VAR = 6 * (6 / 33) * (27 / 33) * (27 / 32)
ALPHA = 0.05


def cold_pick(past: list[dict]) -> set[int]:
    """The 6 reds drawn least often so far; ties go to the smaller number."""
    c = Counter(x for d in past for x in d["reds"])
    return set(sorted(range(1, 34), key=lambda x: (c[x], x))[:COLD])


def score(history: list[dict], first_issue: str) -> dict:
    draws = sorted((d for d in history if d.get("reds")), key=lambda d: int(d["issue"]))
    start = next((i for i, d in enumerate(draws) if d["issue"] == first_issue), None)
    if start is None:
        return {"first_issue": first_issue, "draws": 0, "needed": N, "hits": 0}
    window = draws[start:start + N]
    hits = sum(len(cold_pick(draws[:start + i]) & set(d["reds"])) for i, d in enumerate(window))
    out = {"first_issue": first_issue, "draws": len(window), "needed": N, "hits": hits}
    if len(window) == N:
        z = (hits - N * MEAN) / math.sqrt(N * VAR)
        p = 0.5 * math.erfc(-z / math.sqrt(2))  # one-tailed: fewer hits than chance
        out.update(z=z, p=p, **{"pass": p < ALPHA})
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--first-issue", required=True)
    ap.add_argument("--history", default="data/history.json")
    a = ap.parse_args()
    with open(a.history, encoding="utf-8") as f:
        print(json.dumps(score(json.load(f), a.first_issue), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
