#4 вариант
import json
import requests

city_name = 'Ekaterinburg'
key = '64bccd5fd02857b50f39facbeba7094f'

response = requests.post(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}')
result = json.loads(response.text)

desc = result['weather'][0]['description']
hum = result['main']['humidity']
press = result['main']['pressure']

print('Weather in Ekaterinburg:')
print(f'Description: {desc}')
print(f'Humidity: {hum} %')
print(f'Pressure: {press} Pa')

# newsapi.org
api_key = 'a703ba89cc9f4e76b2cb72150a7d3a3d'
payload = {'q': 'Design'} #Ключевое слово для поиска (например, дизайн)

url = f"https://newsapi.org/v2/everything?q={payload['q']}&language={'ru'}&pageSize={5}&apiKey={api_key}"

response = requests.get(url)
data = response.json()

for article in data['articles']:
    print('Заголовок новости:', article['title'])
    print('Источник:', article['source']['name'])
    print('Дата публикации:', article['publishedAt'])
    print('Описание:', article['description'])
    print('URL статьи:', article['url'])
    print('----------')