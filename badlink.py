import cgi, sys

form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<html><body>')

for name in form:
    print('[%s:%s]' % (name, form[name].value))

print('</body></html>')