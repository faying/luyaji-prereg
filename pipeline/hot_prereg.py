"""Scores the hot-number preregistration (rules/hot-v1.md) on forward draws.

    python -m pipeline.hot_prereg --first-issue <issue from lab/hot-v1-freeze.md> [--history data/history.json]

Prints cumulative hits until the sample is complete; Z and p exist only once all 300 draws are in.
"""
import argparse
import json
import math
from collections import Counter

N = 300
RED_WINDOW, RED_TOP = 100, 6
BLUE_WINDOW, BLUE_TOP = 5, 1
RED_MEAN = 36 / 33
RED_VAR = 6 * (6 / 33) * (27 / 33) * (27 / 32)
BLUE_MEAN = 1 / 16
BLUE_VAR = (1 / 16) * (15 / 16)
ALPHA = 0.025


def top(counts: Counter, numbers: range, n: int) -> set[int]:
    """Most frequent numbers; ties go to the smaller number."""
    return set(sorted(numbers, key=lambda x: (-counts[x], x))[:n])


def red_pick(past: list[dict]) -> set[int]:
    c = Counter(x for d in past[-RED_WINDOW:] for x in d["reds"])
    return top(c, range(1, 34), RED_TOP)


def blue_pick(past: list[dict]) -> set[int]:
    c = Counter(d["blue"] for d in past[-BLUE_WINDOW:])
    return top(c, range(1, 17), BLUE_TOP)


def test_result(total: float, mean: float, var: float) -> dict:
    z = (total - N * mean) / math.sqrt(N * var)
    p = 0.5 * math.erfc(z / math.sqrt(2))
    return {"z": z, "p": p, "pass": p < ALPHA}


def score(history: list[dict], first_issue: str) -> dict:
    draws = sorted((d for d in history if d.get("reds")), key=lambda d: d["issue"])
    start = next((i for i, d in enumerate(draws) if d["issue"] == first_issue), None)
    if start is None:
        return {"first_issue": first_issue, "draws": 0, "needed": N, "red_hits": 0, "blue_hits": 0}
    if start < RED_WINDOW:
        raise ValueError("first issue has too little history before it")
    window = draws[start:start + N]
    red_hits = blue_hits = 0
    for offset, d in enumerate(window):
        past = draws[:start + offset]
        red_hits += len(red_pick(past) & set(d["reds"]))
        blue_hits += d["blue"] in blue_pick(past)
    out = {"first_issue": first_issue, "draws": len(window), "needed": N, "red_hits": red_hits, "blue_hits": blue_hits}
    if len(window) == N:
        out["red"] = test_result(red_hits, RED_MEAN, RED_VAR)
        out["blue"] = test_result(blue_hits, BLUE_MEAN, BLUE_VAR)
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
