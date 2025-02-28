from http.client import responses

from requests import get
from pprint import pprint
endpoint ="https://newsapi.org/v2/everything?q=tesla&from=2025-01-28&sortBy=publishedAt&apiKey=66e0566ae44e445bb306c435410e49ee"
response =get(url=endpoint)
data =response.json()
pprint(data)
print(f'Author: {data.get("articles")[0].get("author")}')
print(f'Title: {data.get("articles")[0].get("title")}')
print(f'Content: {data.get("articles")[0].get("content")}')

while True :
     process = input("işlem türünü seçiniz ")s
     match process:
         case "create":

             new_author = input("Yazarın adını girin: ")
             new_title = input("Yeni haberin başlığını girin: ")
             new_content = input("Yeni haberin içeriğini girin: ")
             new_article = {
                 "author": new_author,
                 "title": new_title,
                 "content": new_content
             }
             data["articles"].append(new_article)

         case "list":
             list_typ = input("listenecek şeyi giriniz")
             match list_typ:
                 case "title":
                     for article in data.get("articles", []):
                         pprint(article.get("title"))
                 case "content":
                     for article in data.get("articles", []):
                         pprint(article.get("content"))
                 case "author":
                     for article in data.get("articles", []):
                         pprint(article.get("author"))
         case "title update":
                 degisen_title = input("Güncellemek istediğiniz haberin başlığını girin: ")
                 boskutu = None
                 for article in data.get("articles", []):
                     if article.get("title") == degisen_title:
                         boskutu = article
                         break
                 if boskutu:
                     new_title= input("yeni başlık adınını yazın")
                     boskutu['title'] = new_title
                 else :
                    pprint("başlık yok")
         case"delete":
             pass #çok zorlandım chat ile yaparken bile mantığını anlamaktada zorlandımm yeniden ilgilenceğim
