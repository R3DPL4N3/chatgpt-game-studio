# Türkçe başlangıç

Bu repo bir oyun veya yeni oyun motoru değil. Codex'in küçük adımlarla planlama, kod yazma ve test etme düzeni. Unity veya Unreal seçimini sen yaparsın.

## İlk kullanım

1. Repoyu indir. Bilgisayarında Python 3.11 veya üstü varsa repo klasöründe terminal aç.
2. `python scripts/validate.py` ve `python -m unittest discover -s tests -v` çalıştır. Windows'ta gerekiyorsa `python` yerine `py -3` kullan.
3. Oyun projenin klasörünü hedef vererek önce önizleme yap:
   `python scripts/install.py --target "D:/Projects/MyGame"`
4. Listede doğru dosyaları gördüğünde aynı komuta `--apply` ekle. Mevcut dosya varsa araç üzerine yazmaz. Özellikle mevcut AGENTS.md dosyasını silmek yerine kuralları elle birleştir.
5. Oyun projesini Codex'te aç ve yeni oturum başlat. “Hangi AGENTS.md, game-* skill dosyaları ve .codex/agents içindeki özel ajanları görüyorsun? Gerçek alt ajan başlatabiliyor musun?” diye sor. Dosyaların varlığı, skill seçiminin gerçekten çalıştığı anlamına gelmez.
6. `studio/PROJECT.md` içine motor sürümünü, gerçek proje yolunu, build/test komutlarını ve mevcut çalışma düzenini yaz. Bilmiyorsan Codex'ten önce projeyi incelemesini iste; tahmin ettirme.

## İlk görev: gösterilebilir mini extraction oyunu

> game-studio kullan. Önce mevcut motoru, çalışan sistemleri ve kullanılabilir lisanslı assetleri incele. Küçük ama etkileyici bir top-down extraction demosu oluştur: harabeye giriş, tek düşman türüyle savaş, sandıktan ganimet ve süre dolmadan çıkış. Sağ tık/basılı hareket, kamera yakınlaştırma, bir saldırı ve Q yeteneği, can göstergeleri, atmosferik ışık/ses ve kazanma/ölme/yeniden deneme akışı olsun. Çalışan sistemleri koru; yeni hesap, matchmaking, auction veya networking yeniden yazımı yapma. 49 uzman arasından gerekenleri seç; aynı anda en fazla dört alt ajan kullan, dosya sahipliğini ayır ve mümkünse bağımsız QA çalıştır. Önce kısa sırayı açıkla, sonra bu kapsamda uygula. Büyük mimari değişiklik veya ücretli bağımlılık için sor. Sonucu gerçekten çalıştırıp test et; mümkünse ekran görüntüsü göster. Test edemediğini açıkça NOT RUN olarak belirt. Şovu kod miktarında değil, oynanış ve sunumda yap.

Bu görevi **oyun projesinde** ver. Bu şablonun içinde oyun varmış gibi çalıştırma; proje/motor seçilmemişse önce hedefi belirt.

## 49 ajan nasıl kullanılır?

- `.codex/agents/` içinde 49 ayrı uzman tanımı var; motor, QA, tasarım, sanat, ses ve üretim rolleri dahil.
- Ana oturum işleri dağıtır. Hepsi birden başlamaz; uygun görevlerde en fazla dört alt ajan paralel çalışır.
- `python scripts/studio.py list` rolleri listeler. `python scripts/studio.py route --area network --engine unreal` ilgili ekibi önerir; kendi başına ajan çalıştırmaz.
- Kurulu oyunda aynı araç `python studio/tools/studio.py ...` yolundadır.
- Codex sürümü/istemcisi özel ajanları yüklemiyorsa seçili rol talimatları desteklenen alt ajana açıkça verilir. Alt ajan desteği de yoksa sıralı rol geçişi yapılır; bu bağımsız 49 ajan çalıştırmak değildir.
- Mevcut `.codex/config.toml` varsa silme/ezme. Ayarları inceleyerek birleştir; güven ve izin ayarlarını otomatik değiştirtme.
- Küçük işlerde eski üç skill ile tek özellik üzerinde ilerleyebilirsin.

## Neleri bilmek yeterli?

- AGENTS.md: çalışma kuralları.
- Skill: belirli bir işi nasıl ele alacağını anlatan talimat dosyası.
- Skill iş akışıdır; `.codex/agents/*.toml` ise destekleyen Codex istemcisinde çağrılabilen uzman ajan tanımıdır. Dosya varlığı, gerçekten çalıştırıldığının kanıtı değildir.
- PASS: belirtilen kontrol gerçekten geçti. NOT RUN: hiç çalıştırılmadı. BLOCKED: çalıştırmak için bir şey eksik. FAIL: kontrol başarısız.

Kodun tamamını ezberlemen gerekmez. “Girdi nereden geliyor, hangi dosya davranışı değiştiriyor, sonucu nerede test ediyorum?” sorularını cevaplayabilmen hedefimiz.

## Sınırlar

Kurulum oyunun dosyalarını, assetlerini veya motorunu değiştirmez. Oyun varlıklarını başka motora taşımadan önce lisansını kontrol et. Bu reponun Python testleri oyununu test etmez. Editör erişimi yoksa Codex'in oyunun çalıştığını söylemesine güvenme; eksik doğrulamayı açıkça iste.
