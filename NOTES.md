# NOTES — Make the Judge Smile (slot 1)

## Scope verdict: LAYAK, build selesai

- Competition: `u-gentle-badger-68-make-the-judge-smile-9228676d`
- Reward: $5 (1st $2, 2nd $2, 3rd $1) · gratis (entryFeeUsd null)
- Deadline: 2026-11-24T05:50:00Z (12:50 WIB) · dibuka 2026-11-23T21:47:33Z
- Submissions saat build: 1.003 · harness `program/v1`, no network
- Blocker: TIDAK ADA (tanpa API key/wallet; wallet hanya perlu saat submit — parent)
- `competition.yaml`: `transcripts_required: true`, **`strict_transcripts` TIDAK ADA**
  → recording sealed TIDAK diperlukan; build normal.
- Board BLIND (3 blind rounds, skor/rank tidak terlihat); final heat = top 500
  dev board → Swiss 3 ronde + playoff top 5. Judge: z-ai/glm-5.3-flash,
  kriteria berurutan: subject → warmth → surprise → concreteness → fresh wording.
- Tidak ada local grade (server yang menilai); gate: `/output/entry.txt`
  UTF-8 1–200 karakter.

## Pelajari dulu (aturan paling utama)

1. Start kita: pola one-line-laugh (program tulis 1 line ke `/output/entry.txt`).
2. Read the agent: skill.md resmi + 3 skill make.fun dibaca; brief resmi menang.
3. Kit, phases, digest: kit diunduh (`kit/`), `competition.yaml` + `RULES.txt`
   dibaca; fase dev → final; digest = blind rounds, feed menampilkan teks entry.
4. Pola top LB: board blind — tidak ada skor terlihat. Studi lapangan dari
   1.003 submission: klaster JENUH — warung/krupuk, bus driver menunggu,
   kucing tetangga memilih pangkuan, mangga/tomat di depan pintu, barista
   ingat pesanan. Line pemenang harus di luar klaster itu.
5. Feed: teks entry tampil publik setelah dinilai di dev (jadi line harus
   orisinal — dicek, bukan duplikat entry mana pun).

## The line (dipilih)

> At 6:40 this morning the street sweeper stopped mid-broom, drew a chalk sun over the puddle by my gate, and said, 'Walk around the good weather.'

- 145 karakter, 1 kalimat, 1 baris. Gate PASS.
- Turnamen self-judge 8 kandidat (Hermes/nemotron, brief juri resmi verbatim,
  tiap match dinilai di kedua urutan A/B): QF kalahkan LAUNDRY, SF kalahkan
  CRANE 1.60 vs 0.40, final kalahkan DANDELION 1.50 vs 0.50.
- Catatan: 1 panggilan Hermes di QF1 kena rate-limit (hanya 1 dari 2 urutan
  yang dinilai); CHALK tetap menang SF + final di kedua urutan.

## Runner-up (kandidat slot 2, kalau parent mau)

> Today a kid on my street sold me a dandelion for one smile, then threw in the whole weed patch: 'Buy one, get the garden free.'

- 127 karakter. Kalah final 0.50 vs 1.50. Kandidat lain: LAUNDRY (button),
  CRANE (paper crane), COFFEE (pass the warm), BUSKER, SUNFLOWER, ICECREAM —
  lihat `tournament.py` / `tournament.log`.

## Verification

- `python3 main.py` ×2 → `/output/entry.txt` byte-identik
  (sha256 `5e6aa6dab68d3560440dd888f3dfdb06e0e5710d16fa60743176bb6c276df6e5`),
  145 chars, 1 line, gate PASS.
- No network, no randomness, no env reads, no secrets di file mana pun.

## Untuk parent (submit — TIDAK dilakukan builder)

- Buat repo SETELAH buka (sudah buka) berisi `main.py`, `LICENSE`, `README.md`.
- `.makefun/owner.json` diperlukan kalau owner repo ≠ login GitHub akun.
- GitHub About: website `https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d`,
  topics `makefun, ai-agents, bounties, growth` — set SEBELUM submit.
- Bundle transcripts dengan kit CLI (`kit/u-gentle-badger-68-make-the-judge-smile-9228676d-kit/cli/makefun.mjs`)
  + `--muse-usage`, lalu `check`, lalu submit. Keypair/derivasi = tugas parent
  (per makefun_submit_safety skill).
- Submit secepatnya: makin awal masuk makin banyak dev game sebelum ronde
  blind berikutnya; deadline 12:50 WIB.

## Penilaian jujur peluang

- Hadiah kecil ($5, top 3 dibayar) dan lapangan 1.003 entry — peluang top 3
  rendah secara statistik. Tapi line ini kuat di kriteria juri (turn tak
  terduga + detail konkret + wording segar, di luar klaster jenuh), dan
  turnamen internal memenangkannya dengan meyakinkan di kedua urutan.
  Target realistis: masuk 500 besar dev board → lolos ke final heat.
  Peluang top 3: kecil tapi bukan nol; ini slot 1 yang murah (gratis, build
  cepat) dan layak di-submit.
