# Türkçe başlangıç

Bu repo bir oyun veya yeni oyun motoru değil. Codex'in küçük adımlarla planlama, kod yazma ve test etme düzeni. Unity veya Unreal seçimini sen yaparsın.

## İlk kullanım

1. Repoyu indir. Bilgisayarında Python 3.10 veya üstü varsa repo klasöründe terminal aç.
2. `python scripts/validate.py` ve `python -m unittest discover -s tests -v` çalıştır. Windows'ta gerekiyorsa `python` yerine `py -3` kullan.
3. Oyun projenin klasörünü hedef vererek önce önizleme yap:
   `python scripts/install.py --target "D:/Projects/MyGame"`
4. Listede doğru dosyaları gördüğünde aynı komuta `--apply` ekle. Mevcut dosya varsa araç üzerine yazmaz. Özellikle mevcut AGENTS.md dosyasını silmek yerine kuralları elle birleştir.
5. Oyun projesini Codex'te aç ve yeni oturum başlat. “Hangi AGENTS.md ve game-* skill dosyalarını görüyorsun?” diye sor. Dosyaların varlığı, skill seçiminin gerçekten çalıştığı anlamına gelmez.
6. `studio/PROJECT.md` içine motor sürümünü, gerçek proje yolunu, build/test komutlarını ve mevcut çalışma düzenini yaz. Bilmiyorsan Codex'ten önce projeyi incelemesini iste; tahmin ettirme.

## İlk görev mesajı

> AGENTS.md ve studio/PROJECT.md dosyalarını oku. game-plan-feature ile yalnızca sağ tık basılıyken hareket hedefini güncelleme özelliğini planla. Mevcut sistemi önce incele. Hangi dosyaların ve editör ayarlarının değişeceğini basitçe anlat. Ben onaylamadan kod yazma.

Bu örnek bir görevdir; projende bu özellik zaten varsa tekrar yaptırma. Sıradaki küçük ihtiyacı seç.

Planı onayladığında:

> Bu planı uygula. Bir seferde yalnızca bu özelliği yap. Her değişen dosyanın ne işe yaradığını açıkla. Sonra game-review-test ile kontrol et. Çalıştırmadığın testleri açıkça belirt.

## Neleri bilmek yeterli?

- AGENTS.md: çalışma kuralları.
- Skill: belirli bir işi nasıl ele alacağını anlatan talimat dosyası.
- Planlayıcı / geliştirici / inceleyici: iş aşamaları; otomatik açılmış üç ayrı yapay zekâ değiller.
- PASS: belirtilen kontrol gerçekten geçti. NOT RUN: hiç çalıştırılmadı. BLOCKED: çalıştırmak için bir şey eksik. FAIL: kontrol başarısız.

Kodun tamamını ezberlemen gerekmez. “Girdi nereden geliyor, hangi dosya davranışı değiştiriyor, sonucu nerede test ediyorum?” sorularını cevaplayabilmen hedefimiz.

## Sınırlar

Kurulum oyunun dosyalarını, assetlerini veya motorunu değiştirmez. Oyun varlıklarını başka motora taşımadan önce lisansını kontrol et. Bu reponun Python testleri oyununu test etmez. Editör erişimi yoksa Codex'in oyunun çalıştığını söylemesine güvenme; eksik doğrulamayı açıkça iste.
