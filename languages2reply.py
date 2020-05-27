import cgi, sys
from formMockup import FieldMockup
from languages2common import hellos, inputkey

debugme = False

hdrhtml = """Content-type: text/html

<title>Languages</title>
<h1>Syntax</h1><hr>
"""

langhtml = """
<h3>%s</h3><p><pre>
%s
</pre></p><br>
"""

def showHello(form):
    choice = form[inputkey].value
    try:
        print(langhtml % (cgi.escape(choice),
                         cgi.escape(hellos[choice])))
    except KeyError:
        print(langhtml % (cgi.escape(choice),
                            "Sorry--I don't kno that language"))

def main():
    if debugme:
        form = {inputkey:FieldMockup(sys.argv[1])}
    else:
        form = cgi.FieldStorage()
    
    print(hdrhtml)
    if not inputkey in form or form[inputkey].value == 'All':
        for lang in hellos.keys():
            mock = {inputkey: FieldMockup(lang)}
            showHello(mock)
    else:
        showHello(form)
    print('<hr>')

if __name__ == "__main__":
    main()