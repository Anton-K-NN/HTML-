'''
Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.

Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

Sample Input 1:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 1:

Yes
Sample Input 2:

https://stepic.org/media/attachments/lesson/24472/sample0.html
https://stepic.org/media/attachments/lesson/24472/sample1.html
Sample Output 2:

No
Sample Input 3:

https://stepic.org/media/attachments/lesson/24472/sample1.html
https://stepic.org/media/attachments/lesson/24472/sample2.html
Sample Output 3:

Yes
'''
import re
import sys
import requests
A=input()
B=input()
ref=[]
ref2=[]
res=requests.get(A)
#print(res.text)
for line in res.text:
    line = res.text.rstrip()
    # print(line)
    pattern = r"<a href=\"(.+.html)"
    match = re.findall(pattern, line)
    ref+=match
#print(match)
#print(ref)
#print(B)
for x in set(ref):
    res = requests.get(x)
    #print(res.text)
    if res.status_code == 200:
        line = res.text.rstrip()
        # print(line)
        pattern = r"<a href=\"(.+.html)"
        match = re.findall(pattern, line)
        ref2+=match
if B in ref2:
    print("Yes")
else: print("No")