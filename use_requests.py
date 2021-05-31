import requests

url = 'https://detik.com'
try:
    result = requests.get(url)
    if result.status_code == 200:
        print(f'Success! result: {result.status_code}')
        print(f'Content: {result.text}')
    else:
        print(f'request error code: {result.status_code}')

except Exception as er:
    print('there is an error ', er)

print('program ended')
