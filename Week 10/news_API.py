import json

r = request.get('www.newsapi.org/v2/everything?', params ={"q":"bitcoin", "apiKey":"asdfjf3487hfdx283dy8732d"})


print(r.text)