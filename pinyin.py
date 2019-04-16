from db import DB

db = DB()
def get_zh_pinyin(zh=None):

    pinyin = db.get_pinyin(ord(zh))
    zh_pinyin = '\n'.join([pinyin.center(8),zh.center(8)])
    return zh_pinyin

def get_all_zh_pinyin(s):
    pinyin = []
    text = []
    for c in s:
    
        if not c.strip() or c in (',，。.!！？?'):
            text.append(c)
            pinyin.append(c)
        else:
            text.append(c)
            pinyin.append(db.get_pinyin(ord(c)))
    result = []
    j= 0
    text_temp = []
    for i,t in enumerate(zip(pinyin,text)):
        print(i,t)
        text_temp.append(t[1])
        if t[0] !='\n':
            result.append(t[0]) 
        else:
            result.append('\n')
            result.extend(text_temp)
            text_temp = []
    print(len('中'.encode()))
    return [item.encode('gbk').center(12).decode('gbk') for item in result]
if __name__ == '__main__':
    result = get_all_zh_pinyin('中国人民很好，\n真的很好\n')
    print(result)
    r = ''.join(result)
    with open('result.txt','w') as f:
        f.write(r)
    


