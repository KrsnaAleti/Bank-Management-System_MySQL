import  mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='MySQL@123',database='bank')
cur = conn.cursor()
cur.execute('create table transactions(acct_no int(11),date date, time time, withdrawal_amt bigint(20),amount_added '
            'bigint(20))')
