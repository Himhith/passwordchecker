##TO DO
#

import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char

    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check api again')
    return res


def pwned_api_check(password):
    #check password if it exists in API response
    #sha1password= hashlib.sha1(password.encode('utf-8'))
    sha1password =(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    first5_char, tail = sha1password[:5], sha1password[5:]
    response=request_api_data(first5_char)
   # print(first5_char,tail)
  #  print(response.text)
    return get_password_leaks_coutn(response,tail)

def read_res(response):
    print(response.text)

def get_password_leaks_coutn(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    #haashe nie mają pierwszych 5 znaków należy albo dodać je do kodu albo wziąć
    print(hash_to_check)
    for h, count in hashes:
      ##  print(count)
     #   print(h)
        if h == hash_to_check:
            return count
    return 0

#request_api_data('afdfafasdfdd')
#print(pwned_api_check('passwod123'))

def main(args):
    for password in args:
        count= pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times.')
        else:
            print(f'{password} was NOT found.')
    return 'done'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))