"""
create or use a client-side cookie storing username;
"""

import http.cookies, os

cookstr = os.environ.get("HTTP_COOKIE")
cookies = http.cookies.SimpleCookie(cookstr)
usercook = cookies.get("user")

if usercook == None:
    cookies = http.cookies.SimpleCookie()
    cookies['user'] = 'Paul'
    print(cookies)
    greeting = '<p>His name shall be...%s</p>' % cookies['user']
else:
    greeting = '<p>Welcome back, %s</p>' % usercook.value

print('Content-type: text/html\n')
print(greeting)