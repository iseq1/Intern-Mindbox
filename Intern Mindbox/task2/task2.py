from pyspark.sql import SparkSession
from pyspark.sql.functions import coalesce, collect_list

# Создаем объект SparkSession
spark = SparkSession.builder.getOrCreate()

# Создаем исходный DataFrame с данными о продуктах и категориях
data = [
    ("Product A", "Category X"),
    ("Product A", "Category Y"),
    ("Product B", "Category Y"),
    ("Product C", "Category Z"),
    ("Product D", None),
    ("Product F", "Category X"),
    ("Product F", "Category Y"),
    ("Product E", "Category Y"),
    ("Product F", "Category Z"),
    ("Product G", None),
]
df = spark.createDataFrame(data, ["Product", "Category"])

# Группируем по продуктам и собираем все категории в список с помощью collect_list
df_grouped = df.groupBy("Product").agg(collect_list("Category").alias("Categories"))

# Добавляем продукты, у которых нет категорий, с помощью coalesce
df_complete = df_grouped.withColumn("Categories", coalesce(df_grouped["Categories"], []))

# Печатаем результирующий DataFrame с парами "Имя продукта – Имя категории"
df_complete.show()