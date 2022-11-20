import requests,sys,shlex
mr_ziz = " ".join(map(shlex.quote, sys.argv[2:]))
bahasa = sys.argv[1];
params = {
    'p1': 'auto',
    'p2': bahasa,
    'p3': mr_ziz,
}

response = requests.get('https://t24.freetranslations.org/freetranslationsorg.php', params=params).text
#a = response.split('"text":"')[1];
#b = a.split('"')[0];
print (f"""{response}
_© ZizBot ~ Multi Device 2022_
""")
