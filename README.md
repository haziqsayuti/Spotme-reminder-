# Spot Me Reminder! sahaja

Script Python ni tolong korang auto-login sistem "Spot Me" (first time masuk shj) and tolong klik button "Daftar Pergerakan" setiap jam, so senang cerita, korang boleh chill buat kerja lain tanpa lupa spotme every 1 hour.
Sbb chrome spotme akan maximize tak kira kita tgh buat apa..tgk youtube ke, tgh buka software lain dll.
Tapi ulasan still kena masukkan sendiri..so that MASA daftar pergerakan tu takdalah sama jam, minit dan saat tu tiap jam.

## ⚠️ Disclaimer
**Guna atas risiko sendiri ya ** Script ni dibuat untuk tujuan 'educational' je hehe. Sendiri nak mudah, sendiri tanggung risikonya!

## Benda Kena Ada (Prerequisites)
Sebelum nak start run script ni, pastikan laptop/PC korang dah install benda-benda ni:
* [Python 3.14](https://www.python.org/downloads/) (amik je yg latest)

## Cara Install
1. Download file `Spotme_reminder_1hour` ni masuk dalam PC korang.
2. Buka Command Prompt (cmd) kat Windows.
3. Taip command kat bawah ni untuk install library Selenium, lepas tu tekan Enter:
   `pip install selenium`

## Macam Mana Nak Guna (Setup & Usage)
1. Buka file `Spotme_reminder_1hour` tu guna text editor macam Notepad/Visual Studio Code.
2. Cari bahagian login. Tukar `"YOUR_IC_NUMBER"` and `"YOUR_NEW_PASSWORD"` letak IC dan password korang yang betul. Lepas tu **Save** file tu! 
3. Buka balik Command Prompt (cmd), pergi kat folder tempat korang save script tu, and run:
   command utk run : `python Spotme_reminder_1hour.py`
4. Nanti script tu akan buka Chrome, auto login, klik button Daftar Pergerakan tu, bila dah settel daftar pergerakan utk 1st korang biar ja chrome tu tak perlu tutup dia akan tggu dekat background untuk next hour. **Penting:** Jangan tutup (close) tingkap hitam CMD tu! Biar je dia jalan kat situ.
