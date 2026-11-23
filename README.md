# Dashboard Seismisitas Indonesia

Dashboard web interaktif untuk memetakan zona seismik Indonesia (clustering) dan
memperkirakan laju gempa per wilayah (forecast), dengan penalaran statistik eksplisit.

> Disclaimer: alat analisis edukatif, bukan sistem peringatan dini.

## Pertanyaan penelitian
1. Di mana zona seismik aktif Indonesia, dan apa karakter tiap zona (laju, kedalaman, b-value)?
2. Berapa jumlah gempa M >= 4,5 per sel grid 1 derajat per bulan, dan seberapa baik
   model dibanding baseline laju historis?
3. Seberapa besar ketidakpastian estimasi (b-value, laju, prediksi)?

## Lingkup
- Wilayah: lintang -11 s/d 6, bujur 95 s/d 141
- Data: katalog USGS ComCat, 1990 sampai sekarang, unduh M >= 4,0
- Target: jumlah gempa M >= 4,5 per sel 1 derajat per bulan
- Split waktu: latih <= 2018, validasi 2019-2021, uji >= 2022

## Metrik keberhasilan (ditetapkan sebelum modeling)
- Model terbaik mengalahkan baseline laju historis pada data uji (Poisson deviance, log-likelihood)
- Lolos uji kalibrasi dasar (N-test dan L-test ala CSEP, plot kalibrasi)
- Estimasi kunci dilaporkan dengan interval ketidakpastian
- Jika model hanya sedikit lebih baik dari baseline, hasil dilaporkan apa adanya

## Status fase
- [x] Fase 0: setup
- [ ] Fase 1: pengambilan data
- [ ] Fase 2: cleaning dan validasi
- [ ] Fase 3: statistik katalog
- [ ] Fase 4: clustering zona seismik
- [ ] Fase 5: forecasting
- [ ] Fase 6: dashboard
- [ ] Fase 7: testing dan dokumentasi
- [ ] Fase 8: deployment