
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
import re
import os

# NLTK gerekli dosyaları indir
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Metin dosyasını okuyun ve ön işleme adımlarını uygulayın:
def preprocess_text(text):
    # Küçük harfe çevirme
    text = text.lower()

    # Kelime ve noktalama işaretlerine ayırma
    tokens = word_tokenize(text)

    text = re.sub(r'\([^()]\d+[^()]\)', '', text)
    text = re.sub(r'\[[^\[\]]\d+[^\[\]]\]', '', text)
    text = text.replace("ark.", '')

    # Stop kelimeleri ve noktalama işaretlerini çıkar
    stop_words = set(stopwords.words("turkish"))
    tokens = [word for word in tokens if word.isalnum() and word not in stop_words]

    # Köklerine ayırma
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return tokens

# Dosyaların bulunduğu klasör
data_path = "turkiye"

# Klasördeki tüm .txt dosyalarını işle
for dosya_adi in os.listdir(data_path):
    if dosya_adi.endswith(".txt"):
        # İşlenecek metin dosyasını oku
        with open(os.path.join(data_path, dosya_adi), 'r', encoding="utf-8") as text_file:
            islenecek = text_file.read()
            text = islenecek

        # Metni ön işleme adımlarından geçir 
        preprocessed_text = preprocess_text(text)

        # Belirli bir yüzdeyle cümle sayısı belirleme
        percentage = 0.15 # Özetin yüzde kaçı alınacak
        sentences = sent_tokenize(text)
        num_sentences = int(len(sentences) * percentage)

        # Cümleleri birleştirerek özet oluşturma
        summary = " ".join(sentences[:num_sentences])

        # Özet sonucunu yazdır
        print(f"Dosya: {dosya_adi}")
        print("Metin Özeti:")
        print(summary)

        gercekmetinuzunlugu = len(text)
        özetuzunlugu = len(summary)

        print(f"Oluşturulan özet uzunluğu: {özetuzunlugu}")
        print(f"Gerçek metin uzunluğu: {gercekmetinuzunlugu}")
        print("---")

        ozet_dosya_yolu = "ozet.txt"
        with open(ozet_dosya_yolu, "w", encoding="utf-8") as file:
            file.write(summary)

print("İşlem tamamlandı.")