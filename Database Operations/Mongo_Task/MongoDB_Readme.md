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

#### Database Connection
Get connected to MongoDB using the given connection string. Make that MongoDB is available and operating; if needed change the connection URL.
---

### Step-by-Step Instructions

1. **Import Libraries and Connect to MongoDB**  
First we import necessary libraries and establish MongoDB connection using the `MongoClient` class from `pymongo`. This stage guarantees that our Python environment can interface with MongoDB.
2. **Import Data from CSV to MongoDB**  
  We import a CSV file using `pandas` and translate data into a dictionary style fit for MongoDB. The facts is then entered into a MongoDB collection. This method uses pymongo for flawless database operations and `pandas` for effective data management.
3. **Convert `last_updated` Field to Date Format**  
 First the `last_updated` field is a string. Changing it to a date format lets us do date-specific operations and monthly searches. We apply this modification across all the entries in the collection using the {update_many} method.
4. **Verify Data Structure**  
We review an example document to make sure the last_updated field is currently in date form before starting searches. This verifying process guarantees proper operation of our date-based searches.
5. **Retrieve Records by Month**  
MongoDB's `$month` operator lets us filter data depending on the month retrieved from a date field so we may gather data for a certain month. Time-based data analysis in particular finds great value in this capability.
6. **Get Top 3 Hottest Locations**  
 We restrict the output to the top 3 warmest sites after declining order of records based on the `temperature_celsius`. This process offers understanding of the greatest temperatures in the dataset.
7. **Get Top 3 Days with Highest Precipitation**  
   To identify the days with the most rainfall, we similarly arrange by `precip_mm`, or milliliters of rain. This question guides us in determining, from precipitation, the most severe weather occurrences.
---

### Applications and Features

Every code function is intended for a certain use:

- **get_records_by_month(month)**: Retrieves information for a specific month thereby enabling seasonal or monthly trend analysis of weather data.
- **get_top_3_hottest_locations()**: Fetches the top 3 locations with the highest recorded temperatures, useful for climate and heat pattern studies.
- **get_top_3_highest_precipitation()**: Retrieves days with the highest precipitation, allowing researchers to identify heavy rainfall events.

---

### Explanations of Choices

- Selected for their strong data manipulation features, **pandas** let us readily read CSV data and get it ready for MongoDB entry.
- **pymongo**: offers a Python interface for MongoDB, thereby allowing us to update, query, and insert databases.
- **$month$ operator in MongoDB**: used to filter data by month, therefore simplifying and quick monthly analysis is made.
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