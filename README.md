YTU Rover - Dur Tabelası Tespiti (YOLOv8)
Bu çalışma, otonom araç sistemleri için YOLOv8 mimarisi kullanılarak eğitilmiş bir "Dur Tabelası" (Stop Sign) nesne tespiti modelini içermektedir. Model, özel bir veri setiyle eğitilmiş ve dış bir test seti üzerinde doğrulanmıştır.

Eğitim Parametreleri
Epochs (50): Yapay zeka modelinin eğitim işlemi sırasında veri setindeki tüm fotoğrafları baştan sona kaç kez gördüğünü (tekrar ettiğini) belirtir.

Batch Size (16): Modelin kendi içindeki ağırlıkları (öğrenme katsayılarını) güncellemeden önce tek seferde hafızaya alıp aynı anda işlediği fotoğraf sayısıdır.

Image Size (640): Eğitime sokulan farklı boyutlardaki fotoğrafların standartlaştırılarak ağa beslendiği piksel çözünürlüğüdür (640x640).

Performans Metrikleri ve Değerlendirme Kriterleri
Modelin otonom sürüş senaryolarındaki başarısı, aşağıdaki temel nesne tespiti metrikleri üzerinden değerlendirilmektedir:

Box Loss (Kutu Kaybı): Modelin tabelanın etrafına çizdiği çerçevenin (bounding box), gerçekte olması gereken çerçeveden ne kadar saptığını gösteren hata payıdır. Değerin düşük olması, modelin tabelanın sınırlarını tam isabetle çizdiğini ifade eder.

Class Loss (Sınıf Kaybı): Tespit edilen nesnenin gerçekten "Dur Tabelası" olup olmadığının tahminindeki hata payıdır. Değerin düşük olması, modelin nesnenin ne olduğunu karıştırmadığını gösterir.

Precision (Kesinlik): Modelin "Burada dur tabelası var" dediği tüm tespitlerin yüzde kaçının gerçekten dur tabelası olduğunu ölçer. Yüksek Precision, yanlış alarmların (hayalet nesnelerin) az olduğunu gösterir.

Recall (Duyarlılık): Test edilen fotoğraflarda gerçekte var olan tüm dur tabelalarının yüzde kaçının model tarafından kaçırılmadan bulunabildiğini ölçer. Yüksek Recall, gözden kaçan tabelaların az olduğunu gösterir.

mAP50 (Mean Average Precision @ .50): Tespit çakışma oranının %50'nin üzerinde olduğu durumlar için genel başarı ortalamasıdır. Nesne tespiti (object detection) modellerinin genel güvenilirliğini belirleyen ana karne notudur; değerin yüksek olması (1.0'a veya %100'e yakın olması) beklenir.