import requests,json,os
posts = requests.get('https://jsonplaceholder.typicode.com/posts')
jsons = posts.json()
print('elija un numero del 1 al 100')
n = int(input())
dic = {}
#dicnoprimos = {}
#tf = bool 
#def IsPrime(num):
#    for x in range(num + 1):
#        x = x + 1
#        print(num,x)
#        if num % x != 0:
#            tf = True
#            print(tf)
#        else:
#            tf = False
#            print(tf)
#    print(tf)
#    return tf
def posteos():
    aux = 1
    if n<100 and n > 0 :
        for aux in range(n):
            print(aux)
#            IsPrime(aux)
#            if IsPrime == True:
            for aux2 in range(aux+1):
                    dic[f'post{aux2+1}'] = jsons[aux2]
#            else:
#            for aux3 in range(n):
#                    dicnoprimos[f'post{aux3+1}'] = jsons[aux]
    return dic#, dicnoprimos
print(posteos())
Json = json.dumps(dic)
if os.path.exists('Downloads'):
    os.chdir('Downloads')
    with open('dic.json','w') as file:
            file.write(Json)
else:
    os.mkdir('downloads')

