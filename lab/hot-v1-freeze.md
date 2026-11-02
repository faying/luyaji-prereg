# hot-v1 凍結紀錄

| 項目 | 值 |
|---|---|
| `rules/hot-v1.md` SHA-256 | `fb8b2d91b3b7969bc7eb465cd09954b0ddea6afceafe8de6fc8b3cde61abf958` |
| `pipeline/hot_prereg.py` SHA-256 | `c8e53ef368fe5838f4c5b6d0cdd3fe7f11b9a9b1880603935b40628171ce15ce` |
| 前瞻窗第一期 | `2026126`（停售 2026-11-03 20:00 Asia/Shanghai） |
| 凍結時已開獎的最後一期 | `2026125` |

凍結時間 F 是這份紀錄推送到本 repo 的時間。若 F 晚於上面的停售時間，第一期順延到 `cutoff(t) > F` 的第一期。

計分：`python -m pipeline.hot_prereg --first-issue 2026126`
