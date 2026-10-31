# 實驗室 log

只往後加，不改、不刪舊條目。每一條的時間以推送到 GitHub（`faying/lucky-luya`）的時間為準。

---

## 2026-10-31 · ziwei-v1 凍結

全部凍結時間 F = 本條目所在 commit 推送到 GitHub 的時間（rules/ziwei-v1.md §3）。

| 項目 | 值 |
|---|---|
| 1. `rules/ziwei-v1.md` SHA-256 | `2226b96533b7d050b0a19bdd60826c5bc8db3ad0237c07445b2840f5839d51c1` |
| 2a. ZiweiKit git tag | `ziweikit-v1.0.0` → commit `8e56ffd17bf451d2572e6a24324f942bdabce1db` |
| 2b. engineTag | `ziweikit-v1.0.0+exp1` |
| 2c. golden 集合雜湊 | `0966441fd5d88c7cfb92f5293d4b47296264da595ae42020d086492ea42171df` |
| 3. 合成生辰清單 `ziwei-lab/synthetic-births-v1.txt` SHA-256 | `c0712c6f0b8a1eba3287e2bc5167487c886fb80826481b073191940791624c3a` |
| 歷史窗 `control/hist-v1.json` SHA-256 | `c3c83b81210cdc1fbeedb31b1a46e9db0fbf4e8dd70625d3531e62ae5378b0de`（2013101–2026124，1,982 期） |
| 池產生器 | `pool-struct-v1`，K = 64（§6 登記結果） |

golden 集合雜湊的重算指令（11 個檔）：

```sh
git ls-tree -r --name-only ziweikit-v1.0.0 golden | sort | while read f; do
  printf "%s  %s\n" "$(git show "ziweikit-v1.0.0:$f" | shasum -a 256 | cut -d' ' -f1)" "$f"
done | shasum -a 256
```

前瞻窗第一期：`cutoff(t) > F` 的第一期與第一個有效期中較晚者。若 F 早於 2026-11-01 20:00（Asia/Shanghai），即 2026125 期（池已於 2026-10-31T10:00:10Z 發布，見 `data/pool-log.jsonl`）；否則順延。
