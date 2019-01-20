
from urllib.parse import unquote

str = "/index.php?title=%E7%89%B9%E6%AE%8A:%E6%9C%80%E8%BF%91%E6%9B%B4%E6%94%B9&feed=atom"
content = "contest" + str
afstr = unquote(str)
print(afstr)
print(content.replace(str, afstr))
print(content)

with open('test.html', 'wb+') as wf:
    fbody = "www.w3cschool.cc"
    wf.write(fbody.encode())

fbody = ""
with open('test.html', 'rb+') as rf:
    fbody = rf.read()
    print(fbody)
    fbody = fbody.decode().replace("w3cschool.cc", "runoob.com")

with open('test.html', 'wb+') as wf:
    wf.write(fbody.encode())