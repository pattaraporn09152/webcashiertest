import numpy as np
import pandas as pd

# อ่านข้อมูลจาไฟล์ 'test.csv'
df = pd.read_csv('test.csv')

# แสดงตัวอย่างข้อมูล 5 แถวแรก
df.head()

# แสดง histogram
df.hist()

# แสดงข้อมูลทางสถิติเฉพาะ 'บ้าน' 'ราคา'
df[['บ้าน', 'ราคา']].describe()
