# DUEL — NI23 G4 · Final 5 · THE MORNING POST

Bangun ulang penuh (staging build lama hilang saat restart VM 24 Nov).
Konsep per ni23g4-fase2-konsep.md: THE MORNING POST, lead #48 Alcaraz
ATP Finals, palet krem pasir · tinta marun · aksen biru baja, pola
koran front-page pemenang final NI22.

## Duel A vs B
- A: 214.280 byte final. Lead selebar penuh, 12 kartu grid 3 kolom,
  strip angka, pita peta titik + DATE CHECK, ALSO ON full-width 10px.
- B: 202.018 byte. Grid 4 kolom (kartu 244px): teks "Src:" di pita
  kepala kartu BERTABRAK dengan chip status (terbaca garbled di kartu
  34/24/25/46) dan beberapa deck terpotong di batas kartu.
- Uji 300px + render penuh: A — semua judul + deck utuh di dalam
  kartu, nol teks garbled; B — pita kepala rusak oleh tabrakan teks.
- PEMENANG: A — B gugur pada sumbu keterbacaan/garbled (penentu 95%
  kekalahan menurut audit NI22), bukan pada ukuran.

## Koreksi deck sebelum vonis final A
Empat deck A awal terpotong di batas kartu (terukur: membungkus 3
baris pada lebar fakta 280px) — dipersingkat tanpa membuang fakta
pool: #11 Benghazi, #43 House (angka 258-173 tetap di judul), #24 ICJ
(700,000+ tetap), #7 COP31 (awal deck ditukar supaya Antalya terhitung
fakta). Sesudah koreksi: semua deck tepat 2 baris, fakta deck 100%
kartu >=2, rata-rata 2,92; margin checker 13/13 LOLOS.

## Gerbang Tembak Pengganti vs entry berdiri G3 "THE EARTH LEDGER"
Data lawan (resi G3): build 266.473 byte, sha d4181337…, 13 kartu +
brief 14-39 (39 cerita), lead ledakan kapal Benghazi, submisi
01a20bad-808a.
Sumbu terukur:
- Ukuran file: A 214.280 B < G3 266.473 B → A lebih ramping (seri
  juri diputuskan ke file lebih kecil).
- Keluasan: A 13 kartu + 27 brief = 40 cerita > G3 39 cerita; 8
  region berkode warna dengan jumlah per region (5+10+5+13+3+2+1+1
  = 40, cocok isi).
- Kepadatan fakta deck: A 100% kartu >=2 fakta spesifik, rata-rata
  2,92 (terukur margin checker) — standar pola pemenang final NI22.
- Klaim dibingkai: kartu 2 "IRGC Claims…" berchip CLAIM + deck
  menegaskan "a claim, not a fact"; kartu 9 "still burns … not sunk".
- Perabot: kicker jujur 52 reports, masthead serif 66px + tanggal
  44px, strip harga emas pool, timeline 7 slot bertime pool, peta
  titik pin bernomor = nomor kartu (13/13) + legenda, kotak DATE
  CHECK 7 buangan bernama, footer HOW SURE 3 baris, ALSO ON 27 brief
  pada 10px terbaca penuh.
- VONIS: LEBIH KUAT — layak tembak.

## Bukti pemenang
- entry.png: 214.280 byte · sha256 dac8e34c48b5479d0a2e545b336aa1c76b6c70cea8f0ec9c4d639512d147a887
- Dimensi IHDR: 1024x1024 · test_entry.py: LULUS · margin checker: 13/13 LOLOS
- Hash jangkar: f8b8f72 (repo warisan v3, riwayat G3 utuh di bawahnya)
