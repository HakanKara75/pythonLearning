text="""
Ey Oğul!

Beysin! Bundan sonra öfke bize; uysallık sana... Güceniklik bize; gönül almak sana... Suçlamak bize; katlanmak sana... Âcizlik bize, yanılgı bize; hoş görmek sana... Geçimsizlikler, çatışmalar, uyumsuzluklar, anlaşmazlıklar bize; adâlet sana... Kötü göz, şom ağız, haksız yorum bize; bağışlama sana…”

“Ey Oğul!

Bundan sonra bölmek bize; bütünlemek sana... Üşengeçlik bize; uyarmak, gayretlendirmek, şekillendirmek sana...”

“Ey Oğul!

Yükün ağır, işin çetin, gücün kıla bağlı... Allah Teâlâ yardımcın olsun. Beyliğini mübârek kılsın. Hak yoluna yararlı etsin. Işığını parıldatsın. Uzaklara iletsin. Sana yükünü taşıyacak güç, ayağını sürçtürmeyecek akıl ve kalp versin.”

“Sen ve arkadaşlarınız kılıçla, bizim gibi dervişler de düşünce, fikir ve duâlarla bize vaad edilenin önünü açmalıyız. Tıkanıklığı temizlemeliyiz.”

“Oğul!

Güçlü, kuvvetli, akıllı ve kelâmlısın... Ama bunları nerede ve nasıl kullanacağını bilmezsen, sabah rüzgârlarında savrulur gidersin!

“Öfken ve nefsin bir olup aklını mağlûb eder. Bunun için dâimâ sabırlı, sebatkâr ve irâdene sahip olasın!..”

“Sabır çok önemlidir. Bir bey, sabretmesini bilmelidir. Vaktinden önce çiçek açmaz. Ham armut yenmez; yense bile bağrında kalır. Bilgisiz kılıç da tıpkı ham armut gibidir.”

“Milletin, kendi irfânı içinde yaşasın. Ona sırt çevirme. Her zaman duy varlığını. Toplumu yöneten de, diri tutan da bu irfandır."""
print(text)
print(len(text)) #1389
print(len(text.split())) #187

texttt= """
a b c A a b D

"""
print(len(texttt.split())) #6

word_count={}

for word in text.split():
    if word in word_count:
        word_count[word]= word_count[word]+1
    else:
        word_count[word]=1

    print(word_count)


