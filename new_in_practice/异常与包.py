# 捕获常规异常
try:
    f = open("C:/Users/moving/Desktop/1.txt.", "r", encoding="UTF-8")
except:
    f = open("C:/Users/moving/Desktop/1.txt.", "w", encoding="UTF-8")
