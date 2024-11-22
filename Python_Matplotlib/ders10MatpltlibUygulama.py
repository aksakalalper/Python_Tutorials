import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

'''
Attribute	Description
Hours_Studied	Number of hours spent studying per week.
Attendance	Percentage of classes attended.
Parental_Involvement	Level of parental involvement in the student's education (Low, Medium, High).
Access_to_Resources	Availability of educational resources (Low, Medium, High).
Extracurricular_Activities	Participation in extracurricular activities (Yes, No).
Sleep_Hours	Average number of hours of sleep per night.
Previous_Scores	Scores from previous exams.
Motivation_Level	Student's level of motivation (Low, Medium, High).
Internet_Access	Availability of internet access (Yes, No).
Tutoring_Sessions	Number of tutoring sessions attended per month.
Family_Income	Family income level (Low, Medium, High).
Teacher_Quality	Quality of the teachers (Low, Medium, High).
School_Type	Type of school attended (Public, Private).
Peer_Influence	Influence of peers on academic performance (Positive, Neutral, Negative).
Physical_Activity	Average number of hours of physical activity per week.
Learning_Disabilities	Presence of learning disabilities (Yes, No).
Parental_Education_Level	Highest education level of parents (High School, College, Postgraduate).
Distance_from_Home	Distance from home to school (Near, Moderate, Far).
Gender	Gender of the student (Male, Female).
Exam_Score	Final exam score.
'''

# Veri setini oku
df = pd.read_csv('StudentPerformanceFactors.csv')

# Temel istatistikleri hesapla
print("Veri Seti Bilgileri:")
print(df.info())
print("\nTemel İstatistikler:")
print(df.describe())

# Eksik değerleri kontrol et
print("\nEksik Değerler:")
print(df.isnull().sum())

# Basit bir görselleştirme (örneğin, histogram)
df.hist(figsize=(10, 8))
plt.suptitle("Veri Seti Histogramları")
plt.show()

# Sadece sayısal sütunları seç
numerical_df = df.select_dtypes(include=['float64', 'int64'])

# Korelasyon matrisi oluştur
corr_matrix = numerical_df.corr()

# Korelasyon matrisini yazdır
print("\nKorelasyon Matrisi:")
print(corr_matrix)

# Isı haritası ile korelasyon matrisi görselleştirme
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Korelasyon Matrisi Isı Haritası")

# Isı haritası ile korelasyon matrisi görselleştirme
plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title("Korelasyon Matrisi Isı Haritası")
plt.show()
