import requests
query=input("What is the topic you're looking for? : ")
api="664985f941ef42ce8e07f2b15ca76ad9"

url=f"https://newsapi.org/v2/everything?q={query}&from=2025-04-18&sortBy=publishedAt&apiKey={api}"
print(url)
r=requests.get(url)
data=r.json()
articles= data["articles"]
for index, article in enumerate(articles):


    print(index+1,article["title"], article["url"])
    print("\n***********************\n")
