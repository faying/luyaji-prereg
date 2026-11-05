# cold-v1 凍結紀錄

| 項目 | 值 |
|---|---|
| `rules/cold-v1.md` SHA-256 | `897059cd45cb6011fbb9d99fa9f0d441aad8a044649f3a1c13f6ada56c06c907` |
| `pipeline/cold_prereg.py` SHA-256 | `168e90934d5b42291616bb15a27faf1511254574a54376fa19941162773d4165` |
| 前瞻窗第一期 | `2026128`（停售 2026-11-08 20:00 Asia/Shanghai） |
| 凍結時已開獎的最後一期 | `2026127` |
| 探索用到的最後一期 | `2026125` |

凍結時間 F 是這份紀錄推送到本 repo 的時間。若 F 晚於上面的停售時間，第一期順延到 `cutoff(t) > F` 的第一期。

計分：`python -m pipeline.cold_prereg --first-issue 2026128`
