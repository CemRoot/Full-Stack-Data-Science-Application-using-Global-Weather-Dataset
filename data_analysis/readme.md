---

# Global Weather Data Analysis

**Languages**: [English](#english) | [Turkish](#turkish)

---

## English

### Project Overview

#%% md

### A Brief Justification for the Suitability of the Data Set

**Reason:**

The Global Weather Dataset has weather information from many places around the world. It talks about important weather
factors like temperature, humidity, and rainfall. The file is perfect for weather research and forecasting on a world
scale because it covers a lot of ground and has a lot of information. This information can be used to look at the
effects of climate change, area weather trends, and extreme weather events.

### Requirements

Before starting the project, make sure the following tools are installed:


```bash
pip install pandas matplotlib seaborn
```

### File Structure

- **Data_Analysis.ipynb**: The main Jupyter Notebook file for data analysis and visualization.
- **GlobalWeatherRepository.csv**: The set of data that includes past weather data.

### How to Run the Notebook

1. Open the `Data_Analysis.ipynb` file in a Jupyter Notebook environment.
2. To load the data, handle it, and make visualisations, run each cell in turn easy peasy :D 

### Functions and Key Sections in the Notebook

1. **Data Loading**:
    - Loads the weather data from **GlobalWeatherRepository.csv**.
    - Uses `pandas` to read and preprocess the data for analysis.

2. **Data Cleaning**:
    - Takes care of missing values, gets rid of unnecessary fields, and gets the data ready for analysis.
    - This is necessary to make sure the analysis is correct and consistent.


3. **Exploratory Data Analysis**:
    - **Summary Statistics**: Clike mean, median, and standard deviation for temperature, humidity, etc.
    - **Correlation Analysis**: Shows how different weather factors are related to each other.
    - **Data Visualizations**:
        - **Temperature Trends**: Charts temperature changes over time.
        - **Humidity and Precipitation Distribution**: Shows distribution of humidity and precipitation values.


4. **Interactive Visualizations**:
    - **Seaborn & Matplotlib**: It makes different charts and graphs so that you can see trends and connections in the data.
    - **Plot Types**: It has line plots, bar charts, and scatter plots to help you see different things.


5. **Conclusion**:
    - summarises analytical data to reveal global weather patterns.

### Example Commands

To start the Jupyter Notebook:

```bash
jupyter notebook Data_Analysis.ipynb
```

### License

This project is open source, available under the [MIT License](LICENSE).

---

## Turkish

### Proje Genel Bakış

**Global Hava Durumu Veri Analizi** projesi, Python kütüphaneleri kullanarak küresel hava durumu verilerini keşfetmek,
analiz etmek ve görselleştirmek için tasarlanmıştır. Bu proje, **GlobalWeatherRepository.csv** dosyasını kullanarak hava
durumu eğilimlerini ve kalıplarını analiz eder.

### Gereksinimler

Projeyi çalıştırmadan önce aşağıdaki kütüphanelerin yüklü olduğundan emin olun:

```bash
pip install pandas matplotlib seaborn
```

### Dosya Yapısı

- **Data_Analysis.ipynb**: Veri analizi ve görselleştirme için ana Jupyter Notebook dosyası.
- **GlobalWeatherRepository.csv**: Tarihsel hava durumu verilerini içeren veri dosyası.

### Notebook'u Çalıştırma

1. `Data_Analysis.ipynb` dosyasını bir Jupyter Notebook ortamında açın.
2. Veriyi yüklemek, işlemek ve görselleştirmeleri oluşturmak için her hücreyi sırayla çalıştırın.

### Notebook'taki Fonksiyonlar ve Önemli Bölümler

1. **Veri Yükleme**:
    - **GlobalWeatherRepository.csv** dosyasından hava durumu verilerini yükler.
    - `pandas` kullanarak veriyi analiz için önceden işler.

2. **Veri Temizleme**:
    - Eksik değerlerle başa çıkar, ilgisiz sütunları kaldırır ve analiz için veriyi hazırlar.
    - Analizin doğruluğunu ve tutarlılığını sağlamak için önemlidir.

3. **Keşifsel Veri Analizi (EDA)**:
    - **Özet İstatistikler**: Sıcaklık, nem gibi değişkenlerin ortalama, medyan, standart sapma gibi temel
      istatistiklerini hesaplar.
    - **Korelasyon Analizi**: Farklı hava durumu parametreleri arasındaki ilişkiyi gösterir.
    - **Veri Görselleştirmeleri**:
        - **Sıcaklık Eğilimleri**: Zamanla sıcaklık eğilimlerini grafik olarak gösterir.
        - **Nem ve Yağış Dağılımı**: Nem ve yağış değerlerinin dağılımını gösterir.

4. **Etkileşimli Görselleştirmeler**:
    - **Seaborn & Matplotlib**: Verilerdeki kalıpları ve ilişkileri anlamak için çeşitli grafikler oluşturur.
    - **Grafik Türleri**: Çizgi grafikleri, çubuk grafikler ve dağılım grafikleri gibi çeşitli grafik türleri içerir.

5. **Sonuç**:
    - Analizden elde edilen bulguları özetler ve küresel hava durumu eğilimlerine dair içgörüler sunar.

### Örnek Komutlar

Jupyter Notebook’u başlatmak için:

```bash
jupyter notebook Data_Analysis.ipynb
```

### Lisans

Bu proje açık kaynaklıdır ve [MIT Lisansı](LICENSE) ile kullanıma sunulmuştur.

--- 
