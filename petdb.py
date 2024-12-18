import pyodbc

global dbPet

class dbMSSQLHelper:
    #srv="localhost" # Cheba
    srv=".\\SQLEXPRESS"
    dbName="cats1"
    userid="sa"
    passwd="123456"
    User=None

    def __init__(self,_srv = "localhost",_db = "cats1"):
        self.srv=_srv
        self.dbName=_db
        self.connect()

    def connect(self):
        self.ready=False
        self.conn=None
        try:
            self.conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                "Server="+self.srv+";"
                "Database="+self.dbName+";"
                "user id="+self.userid+";"
                "password="+self.passwd+";"
                "Trusted_Connection=yes;")
            print("Connected")
            self.ready=True
        except Exception as e:
            print(f"Fail to open DB {str(e)}")
            self.conn=None

    def __del__(self):
        print("Closed")
        if self.conn!=None:
            self.conn.close()

    # Select raw
    def select(self, sql):
        try:
            cursor = self.conn.cursor()
            res=cursor.execute(sql).fetchall()
            cursor.close()
            return res
        except Exception as e:
            print(f"Fail: {sql} error: {str(e)}")
        return None

    # Select single field walue from tab with condition (all fields by def)
    def one(self, tab, cond, fld="*"):
        try:
            cursor = self.conn.cursor()
            # print(f"select {fld} from {tab} where {cond}") # +D+
            res=cursor.execute(f"select {fld} from {tab} where {cond}").fetchone()
            cursor.close()
            return res
        except Exception as e:
            print(f"Select one {fld} from {tab} error: {str(e)}")
        return None

    # Select all field values from tab with condition (all fields by def)
    def all(self, tab, fld="*", cond=None):
        if cond: cond="where "+cond
        try:
            cursor = self.conn.cursor()
            res=cursor.execute(f"select {fld} from {tab} {cond}").fetchall()
            cursor.close()
            return res
        except Exception as e:
            print(f"Select all from {tab} error: {str(e)}")
        return None
    
    # Load BLOB from file
    def loadBLOB(self,fname):
        try:
            f=open("Pics/default.jpg", 'rb')
            bdata=f.read()
            f.close()
        except Exception as e:
            print(f"Fail to get BLOB: {str(e)}")
            return None
        return bdata
    
    # Insert into tab, fileds list, tuple of params
    # returns inserted id
    def insert(self,tab,fld,val):
        parstr=("?,"*len(fld.split(",")))[:-1] # ?,?... line
        sql = f"INSERT INTO {tab} ({fld}) VALUES ({parstr})"
        try:
            cursor = dbPet.conn.cursor()
            cursor.execute(sql, val)
            dbPet.conn.commit()
            #id=cursor.execute("select SCOPE_IDENTITY()").fetchone()
            id=int(cursor.execute("select @@IDENTITY").fetchone()[0])
            cursor.close()
        except Exception as e:
            print(f"Fail to insert into {tab}: {str(e)}")
            return -1
        return id

    # Update tab, fileds list, tuple of params, cond
    # returns inserted id
    def update(self,tab,fld,val,cond):
        sql = f"UPDATE {tab} SET "
        for f in fld:
            sql+=f"{f}=? "
            if f!=fld[-1]: sql+=","
        sql+=f" WHERE {cond}"
        try:
            cursor = dbPet.conn.cursor()
            cursor.execute(sql, val)
            dbPet.conn.commit()
            cursor.close()
        except Exception as e:
            print(f"Fail to update {tab}: {str(e)}")
            return -1
        return id

dbPet=dbMSSQLHelper()

