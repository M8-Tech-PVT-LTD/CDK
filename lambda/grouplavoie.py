import requests
from bs4 import BeautifulSoup
import json


def lambda_handler(request, response):
    url = request['url']
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.select('table')
    data = {}
    bathroom_element = soup.find('i', class_='c-property-details-bar__bathrooms')
    bedroom_element = soup.find('i', class_='c-property-details-bar__bedrooms')

    bathroom_count = bathroom_element.find_next('span', class_='c-property-details-bar__number').text.strip()
    bedroom_count = bedroom_element.find_next('span', class_='c-property-details-bar__number').text.strip()
    data['bathroom_count'] = bathroom_count
    data['bedroom_count'] = bedroom_count

    for row in table:
        for tr in row.find_all('tr'):
            if tr.find('td'):
                key = tr.find('td').text.strip().lower().replace(' ', '_')
                value = tr.find_all('td')[1].text.strip()
                if key not in data:
                    data[key] = value

    characteristics = soup.select('.c-caracteristiques__row')
    for row_div in characteristics:
        if row_div:
            key = row_div.find('div', recursive=False).text.strip().lower().replace('/', '').replace(' ', '_')
            value = row_div.find_all('div', recursive=False)[1].text.strip()
            data[key] = value
    subtitle_elements = soup.find_all('h2', class_='c-sidebar-property__subtitle')
    for subtitle_element in subtitle_elements:
        key = subtitle_element.text.strip().replace(" ", "_").lower()
        value_element = subtitle_element.find_next(class_='c-sidebar-property__info')
        if value_element:
            value = value_element.text.strip()
            data[key] = value

    # json_students_data = json.dumps(data, indent=2)
    # with open('data.json', 'w') as json_file:
    #     json_file.write(json_students_data)
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/plain'
        },
        'body': format(data)
    }
