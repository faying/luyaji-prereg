# Luya Ji — 紫微實驗預先登記（ziwei-v1）

這個 repo 只放凍結時的實驗規則與雜湊，作為公開、可查的凍結時間。

- `rules/ziwei-v1.md` — 凍結的實驗規則
- `lab/log.md` — 凍結紀錄：規則、引擎 tag 與 golden set、合成生辰、歷史窗的 SHA-256
- `control/hist-v1.json` — 對照用的歷史窗（2013101–2026124）

來源：私有 repo 的 commit `7b81458`（tag `ziweikit-v1.0.0` = `8e56ffd`）。凍結後不再修改本 repo 的這些檔案。

`lab/log.md` 寫的 F 是私有 repo 的推送時間（2026-10-31T12:43:20Z），外部無法查證；可公開查證的凍結時間以本 repo 第一個 commit 的推送時間為準。

---

## 熱號實驗（hot-v1）

- `rules/hot-v1.md` — 凍結的實驗規則
- `pipeline/hot_prereg.py` — 計分腳本
- `lab/hot-v1-freeze.md` — 凍結紀錄：兩個檔的 SHA-256 與前瞻窗第一期

來源：私有 repo 的 commit `7912eb2`。凍結時間以新增這些檔案的 commit 推送到本 repo 的時間為準。凍結後不再修改。
