# from newspaper import Article

# article = Article('https://vnexpress.net/ky-su-phan-mem-ai-dau-tien-tren-the-gioi-4722040.html')

# #download
# article.download()
# article.parse()

# #in bai bao

# print(article.text)
# print(article.images)


import nltk
from nltk . tokenize import word_tokenize

nltk . download ('punkt')

data = "Tôi thích học AI và Toán"
# Bước 1: Tokenization data
tokenization = word_tokenize ( data )
# Bước 2: Gọi thư viện Pos tagging
result = nltk . pos_tag ( tokenization )
print ( result )
