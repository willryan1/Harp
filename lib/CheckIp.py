import urllib.request, urllib.error, json

def new():
    api_check = "https://check.torproject.org/api/ip"
    try:
        conn = urllib.request.urlopen(api_check)
    except urllib.error.HTTPError as e:
        print('HTTPError: {}'.format(e.code))
    except urllib.error.URLError as e:
        print('URLError: {}'.format(e.reason))
    else:
        data = json.loads(conn.read().decode())
        check_ip = data['IP']
        check_tor = data['IsTor']
        if(check_tor):
            check_tor = "activated"
        else:
            check_tor = "disabled"
        print("\nStatus: {}\nIP: {}\n".format(check_tor, check_ip))
