from bs4 import BeautifulSoup
import requests

url = ('https://jadwalsholat.org/jadwal-sholat/monthly.php?id=47')
contents = requests.get(url)
if contents.status_code == 200:
    print('Request succeed')
else:
    print(f"Request failed with status code {contents.status_code}")

def schedule_bogor():
    soup = BeautifulSoup(contents.text, 'html.parser')
    data = soup.find_all('tr', 'table_highlight')
    data = data[0]

    praying = {}
    i = 0
    for d in data:
        if i == 1:
            praying['Imsyak'] = d.get_text()
        elif i == 2:
            praying['Shubuh'] = d.get_text()
        elif i == 3:
            praying['Terbit'] = d.get_text()
        elif i == 4:
            praying['Dhuha'] = d.get_text()
        elif i == 5:
            praying['Dzuhur'] = d.get_text()
        elif i == 6:
            praying['Ashar'] = d.get_text()
        elif i == 7:
            praying['Maghrib'] = d.get_text()
        elif i == 8:
            praying['Isya'] = d.get_text()
        i = i + 1

    print(praying)
    print(praying['Maghrib'])


if __name__ == '__main__':
    schedule_bogor()