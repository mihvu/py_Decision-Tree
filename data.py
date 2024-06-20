import pandas as pd

# Đọc dữ liệu từ tệp CSV bằng pandas
def read_csv_file(file_path):
    return pd.read_csv(file_path)

# Sử dụng hàm để đọc dữ liệu từ tệp CSVfrom sklearn.neighbors import NearestNeighbors
df = pd.read_csv("titles.csv")
print(df)

print(df.head())