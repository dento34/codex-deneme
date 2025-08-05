# codex-deneme

Bu depo, Rider-Waite-Smith tarot destesi görselleriyle çalışmak için örnek betikler içerir.

## Kart görsellerini yeniden boyutlandırma

`resize_tarot_cards.py`, indirilen kart görsellerini gerçek tarot kartı boyutuna getirir.
Varsayılan boyut 2.75" x 4.75" ölçülerindeki (300 DPI'da 825×1425 piksel) kartlardır.
Görseller oran korunarak yeniden ölçeklendirilir ve beyaz bir arka plan üzerine ortalanır.

### Kullanım

Önce gerekli paketi yükleyin:

```bash
pip install Pillow
```

Ardından betiği çalıştırın:

```bash
python resize_tarot_cards.py --input-dir rider_waite_smith_cards --output-dir rws_cards_resized
```

İsteğe bağlı olarak `--width`, `--height` veya `--dpi` parametreleriyle farklı boyutlar belirtebilirsiniz.
