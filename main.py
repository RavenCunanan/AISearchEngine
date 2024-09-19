from exa_py import Exa

exa = Exa('Your API Code Here')

query = input('Search here: ')

response = exa.search(
  query,
  num_results=5,
  type='keyword',
  include_domains=['https://www.tiktok.com'],
)

for result in response.results:
  print(f'Title: {result.title}')
  print(f'URL: {result.url}')
  print()
