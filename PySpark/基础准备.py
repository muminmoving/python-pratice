from pyspark import SparkConf,SparkContext
# 创建类对象
conf = SparkConf().setMaster("local[*]").setAppName("nihao")
# 基于Sparkconf创建SparkContext
sc = SparkContext(conf=conf)
print(sc.version)
sc.stop()