from newspaper import Article

article = Article('https://vnexpress.net/ky-su-phan-mem-ai-dau-tien-tren-the-gioi-4722040.html')

#download
article.download()
article.parse()

#in bai bao

print(article.text)
print(article.images)
