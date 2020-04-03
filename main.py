from bs4 import BeautifulSoup
import requests

search = input("Enter for:")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)

'''
find sibling
        children = item.find("h2")
        print("next sibling pf the h2:", children.next_sibling)
'''
#        find parent
#        print("Summery:", item.find("a").parent.parent.find("p").text)

'''
find children
        children = item.children
        for child in children:
            print("child:", child)
'''
