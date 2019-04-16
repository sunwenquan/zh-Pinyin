import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('zh-pinyin-map.sqlite3')
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        sql = '''
        CREATE TABLE  IF NOT EXISTS [pinyin] (
            zh_id  INTEGER  PRIMARY KEY
                            UNIQUE
                            NOT NULL,
            pinyin CHAR (8) 
        );
        '''
        self.cur.execute(sql)
    def get_pinyin(self,zh_id):
        self.cur.execute('select pinyin from pinyin where zh_id=?',(zh_id,))
        
        res = self.cur.fetchone()
        if res:
            return res[0]
        return None

    def insert_item(self,item):
        """
        参数说明：
            - item : (zh_id,pinyin),例如： insert_item(1011,'ha')
            zh_id是汉字对应的unicode编码的十进制表示形式。
        """
        sql = '''
        insert into pinyin(zh_id,pinyin) values(?,?)
        '''
        self.cur.execute(sql,item)
        self.conn.commit()

    def insert_items(self,items:tuple):
        """
        """
        sql = '''
        insert into pinyin(zh_id,pinyin) values(?,?)
        '''
        self.cur.executemany(sql,items)
        self.conn.commit()

    def close_db(self):
        self.cur.close()
        self.conn.close()

if __name__ == '__main__':
    db = DB()

    # with open('pinyin-utf8.dat') as f:
    
    #     for line in f:
    #         zh,pinyin= line.strip().split(' ')[:2]
    #         item = (ord(zh),pinyin)
    #         db.insert_item(item)

    print(db.get_pinyin(ord('文')))
    db.close_db()
    
