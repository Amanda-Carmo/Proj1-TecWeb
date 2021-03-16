def extract_route(string):    
    i = string.find('/') + 1
    sub = string[i:]
    f = sub.find(' ') 
    route = string[i:f+i]    
    print(route)

    return route


def read_file(path):

    path = str(path)

    if path.endswith('.txt') or path.endswith('.html') or path.endswith('.css'):
     
        file = open(path, "rb")
        return file.read()

    else:
        file = open(path, "rb")
        return file.read()

    
def load_data(file):
    import json
    with open('data/{0}'.format(file)) as json_file: 
        data = json.load(json_file) 
    return data

def load_template(template):    
    content = open("templates/"+template, "r+", encoding='utf8').read()
    return content

def add_dic(dic, file):
    import json
    with open('data/'+file,  "rb") as fil:
        lista = json.load(fil)
        lista.append(dic)

    with open("data/"+file, "w") as fil:
        json.dump(lista, fil)

    print (lista)    


def build_response(body='', code=200, reason='OK', headers=''): 
    if body == '' and code==200 and reason=='OK' and headers=='':
        return bytes("HTTP/1.1 {} {}\n\n".format(code, reason), encoding='utf8')
    
    elif body != '' and code == 200 and reason == "OK" and headers == "":
        return bytes("HTTP/1.1 200 OK\n\n{}".format(body), encoding='utf8')

    elif reason != "OK" and code!= 200 and headers!='':
        return bytes("HTTP/1.1 {} {}\n{}\n\n".format(code, reason, headers), encoding='utf8')

    if reason != "OK" and code!= 200 and headers=='':
        return bytes('HTTP/1.1 {} {}\n\n'.format(code, reason), encoding='utf8')



