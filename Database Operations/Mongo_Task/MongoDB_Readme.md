# Global Weather Data Analysis with MongoDB and Python

- [English Version](#english-version)
- [Türkçe Versiyonu](#türkçe-versiyonu)



## English Version

### Overview

This project uses Python and MongoDB to allow study of world weather data. We start by importing data from a CSV file, putting it in a MongoDB collection, and then converting the data to run monthly, temperature-based, and precipitation-based searches.
### Table of Contents

1. [Requirements](#requirements)
2. [Installation and Setup](#installation-and-setup)
3. [Step-by-Step Instructions](#step-by-step-instructions)
4. [Functions and Usage](#functions-and-usage)
5. [Explanations of Choices](#explanations-of-choices)

---

### Requirements

- **Python**: 3.7 or above
- **MongoDB**: Version 4.0 or above
- **Libraries**: `pymongo`, `pandas`

### Installation and Setup

#### Install Libraries
Make sure `pymongo` and `pandas` libraries are installed before launching the code. Type the following in your Jupyter Notebook or terminal:
```bash
pip install pymongo pandas
```

## Database Connection 

Use the given login code to connect to MongoDB. Check to see if MongoDB is running; if it isn't, contact with me to get the connection URL.

### Step-by-Step Instructions

1. **Import Libraries and Connect to MongoDB**  
First, I get the tools  need and use the `MongoClient` class from `pymongo` to connect to MongoDB. This step makes sure that our Python system can talk to MongoDB.
2. **Import Data from CSV to MongoDB**  
  I import a CSV file using `pandas` and translate data into a dictionary style fit for MongoDB. The facts is then entered into a MongoDB collection. This method uses pymongo for flawless database operations and `pandas` for effective data management.
3. **Convert `last_updated` Field to Date Format**  
In the first place, the last_updated field is a string. Once I change it to a date format, I can do actions that depend on dates and searches that look for months. Using the {update_many} method, I make this change to all the items in the collection.
4. **Verify Data Structure**  
In the first place, the last_updated field is a string. Once we change it to a date format, we can do actions that depend on dates and searches that look for months. Using the {update_many} method, I make this change to all the items in the collection.
5. **Retrieve Records by Month**  
MongoDB's `$month` operator lets us filter data depending on the month retrieved from a date field so we may gather data for a certain month. Time-based data analysis in particular finds great value in this capability.
6. **Get Top 3 Hottest Locations**  
The output is limited to the top 3 hottest locations based on temperature_celsius, in decreasing order of records. This procedure reveals the dataset's highest temperatures.
7. **Get Top 3 Days with Highest Precipitation**  
To discover days with the greatest rainfall, we sort by `precip_mm`, or rain millilitres. This question helps us identify severe weather events from precipitation.

---

### Applications and Features

Every code function is intended for a certain use:

- **get_records_by_month(month)**: Retrieves month-specific weather data for seasonal or monthly trend analysis.
- **get_top_3_hottest_locations()**: Finds the top three hottest temperatures for climate and heat pattern investigations.
- **get_top_3_highest_precipitation()**: Retrieves greatest precipitation days to help researchers discover big rainfall episodes.

---

### Explanations of Choices

- Pandas, known for their data manipulation capabilities, help us easily read CSV data for MongoDB input.
- **pymongo**: allows MongoDB updates, queries, and inserts using Python.
- MongoDB's **$month$ operator** filters data by month, simplifying and speeding up monthly analysis.
- Important for time-series research, **date conversion** lets us access strong date-based searches in MongoDB by transforming `last_updated` into a date format.

---

## Türkçe Versiyonu

### Genel Bakış

Bu proje, Python ve MongoDB kullanarak küresel hava durumu verilerini analiz etmeyi sağlar. Veriler CSV formatında MongoDB’ye aktarılır, ardından ay, sıcaklık ve yağış bazında sorgular yapılır.

### İçindekiler

1. [Gereksinimler](#gereksinimler)
2. [Kurulum ve Ayarlar](#kurulum-ve-ayarlar)
3. [Adım Adım Talimatlar](#adım-adım-talimatlar)
4. [Fonksiyonlar ve Kullanımı](#fonksiyonlar-ve-kullanımı)
5. [Seçimlerin Açıklamaları](#seçimlerin-açıklamaları)

---

### Gereksinimler

- **Python**: 3.7 veya üstü
- **MongoDB**: 4.0 veya üstü
- **Kütüphaneler**: `pymongo`, `pandas`

### Kurulum ve Ayarlar

#### Kütüphaneleri Yükleme
Kodları çalıştırmadan önce, `pymongo` ve `pandas` kütüphanelerinin yüklü olduğundan emin olun. Terminal veya Jupyter Notebook’ta aşağıdaki komutu çalıştırın:

```bash
pip install pymongo pandas
```

#### Veritabanı Bağlantısı
Veritabanına bağlanmak için sağlanan bağlantı adresini kullanın. MongoDB’nin çalıştığından ve erişilebilir olduğundan emin olun, gerekirse bağlantı URL’ini güncelleyin.

---

### Adım Adım Talimatlar

1. **Kütüphaneleri Yükleyin ve MongoDB'ye Bağlanın**  
   Gerekli kütüphaneleri yükleyip MongoDB’ye bağlanarak başlıyoruz. Bu adım, Python ortamımızın MongoDB ile iletişim kurabilmesini sağlar.

2. **CSV Verilerini MongoDB'ye Aktarın**  
   `pandas` kullanarak bir CSV dosyasını yükleyip MongoDB'ye uyumlu bir formatta aktarırız. Veriyi `pymongo` ile MongoDB koleksiyonuna ekleriz.

3. **`last_updated` Alanını Tarih Formatına Çevirin**  
   `last_updated` alanı başlangıçta bir `string` olarak kaydedilmiştir. Bu alanı tarih formatına dönüştürerek ay bazında sorgular yapmayı kolaylaştırıyoruz.

4. **Veri Yapısını Doğrulama**  
   Sorgulara geçmeden önce, örnek bir belgeyi inceleyerek `last_updated` alanının doğru formatta olup olmadığını kontrol ederiz.

5. **Ay Bazında Kayıtları Getirme**  
   Belirli bir ay için verileri çıkarmak için MongoDB’nin `$month` operatörünü kullanırız. Bu, zaman bazlı veri analizi için oldukça kullanışlıdır.

6. **En Sıcak 3 Lokasyonu Getirme**  
   Kayıtları `temperature_celsius` alanına göre sıralayıp en yüksek sıcaklığa sahip 3 lokasyonu buluruz. Bu işlem, sıcaklık analizleri için yararlıdır.

7. **En Yüksek Yağışlı 3 Günü Getirme**  
   Benzer şekilde, `precip_mm` alanına göre sıralama yaparak en yüksek yağış miktarına sahip günleri buluruz. Bu, en yoğun yağış olaylarını belirlemeye yardımcı olur.

---

### Fonksiyonlar ve Kullanımı

Kodda yer alan her fonksiyon belirli bir amaç için tasarlanmıştır:

- **get_records_by_month(month)**: Belirli bir ayın kayıtlarını getirir, bu da mevsimsel ve aylık analizler için kullanışlıdır.
- **get_top_3_hottest_locations()**: En yüksek sıcaklıklara sahip 3 lokasyonu döndürür, iklim ve sıcaklık desenleri üzerine çalışmalar için idealdir.
- **get_top_3_highest_precipitation()**: En yoğun yağışın gerçekleştiği günleri getirir, yağış analizi yapmayı sağlar.

---

### Seçimlerin Açıklamaları

- **`pandas`**: Veriyi CSV formatında okuyup MongoDB’ye hazırlamak için seçilmiştir. Veri yönetiminde oldukça güçlüdür.
- **`pymongo`**: MongoDB ile Python arasında veri alışverişi sağlar.
- **MongoDB `$month` Operatörü**: Ay bazında filtreleme için kullanılır, aylık analizlerde işlemleri basitleştirir.
- **Tarih Dönüşümü**: `last_updated` alanını tarih formatına dönüştürerek, MongoDB’de daha güçlü ve esnek tarih bazlı sorgular yapmayı mümkün kılar.

---