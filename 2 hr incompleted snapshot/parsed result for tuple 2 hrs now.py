['N_NATIONKEY','N_NAME','N_REGIONKEY','N_COMMENT']
['R_REGIONKEY','R_NAME','R_COMMENT']
['P_PARTKEY','P_NAME','P_MFGR','P_BRAND','P_TYPE','P_SIZE','P_CONTAINER','P_RETAILPRICE','P_COMMENT']
['S_SUPPKEY','S_NAME','S_ADDRESS','S_NATIONKEY','S_PHONE','S_ACCTBAL','S_COMMENT']
['PS_PARTKEY','PS_SUPPKEY','PS_AVAILQTY','PS_SUPPLYCOST','PS_COMMENT']
['C_CUSTKEY','C_NAME','C_ADDRESS','C_NATIONKEY','C_PHONE','C_ACCTBAL','C_MKTSEGMENT','C_COMMENT']
['O_ORDERKEY','O_CUSTKEY','O_ORDERSTATUS','O_TOTALPRICE','O_ORDERDATE','O_ORDERPRIORITY','O_CLERK','O_SHIPPRIORITY','O_COMMENT']
['L_ORDERKEY','L_PARTKEY','L_SUPPKEY','L_LINENUMBER','L_QUANTITY','L_EXTENDEDPRICE','L_DISCOUNT','L_TAX','L_RETURNFLAG','L_LINESTATUS','L_SHIPDATE','L_COMMITDATE','L_RECEIPTDATE','L_SHIPINSTRUCT','L_SHIPMODE','L_COMMENT']


to add table name using lower case

 "nation":(4,['N_NATIONKEY','N_NAME','N_REGIONKEY','N_COMMENT'])
        ,"REGION":(3,['R_REGIONKEY','R_NAME','R_COMMENT'])

        ,"PART":(9,['P_PARTKEY','P_NAME','P_MFGR','P_BRAND','P_TYPE','P_SIZE','P_CONTAINER','P_RETAILPRICE','P_COMMENT'])
        ,"SUPPLIER":(7,['S_SUPPKEY','S_NAME','S_ADDRESS','S_NATIONKEY','S_PHONE','S_ACCTBAL','S_COMMENT'])
        ,"PARTSUPP":(5,['PS_PARTKEY','PS_SUPPKEY','PS_AVAILQTY','PS_SUPPLYCOST','PS_COMMENT'])
        ,"CUSTOMER":(8,['C_CUSTKEY','C_NAME','C_ADDRESS','C_NATIONKEY','C_PHONE','C_ACCTBAL','C_MKTSEGMENT','C_COMMENT'])
        ,"ORDERS":(9,['O_ORDERKEY','O_CUSTKEY','O_ORDERSTATUS','O_TOTALPRICE','O_ORDERDATE','O_ORDERPRIORITY','O_CLERK','O_SHIPPRIORITY','O_COMMENT'])
        ,"LINEITEM":(16,['L_ORDERKEY','L_PARTKEY','L_SUPPKEY','L_LINENUMBER','L_QUANTITY','L_EXTENDEDPRICE','L_DISCOUNT','L_TAX','L_RETURNFLAG','L_LINESTATUS','L_SHIPDATE','L_COMMITDATE','L_RECEIPTDATE','L_SHIPINSTRUCT','L_SHIPMODE','L_COMMENT'])

        C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\customer.tbl', {9}, 1500), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\lineitem.tbl', {17}, 60175), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\nation.tbl', {5}, 25), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\orders.tbl', {10}, 15000), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\part.tbl', {10}, 2000), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\partsupp.tbl', {6}, 8000), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\region.tbl', {4}, 5), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\supplier.tbl', {8}, 100)]
[]
('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT')
['1', 'Customer#000000001', 'IVhzIApeRb ot,c,E', '15', '25-989-741-2988', '711.56', 'BUILDING', 'to the even, regular platelets. regular, ironic epitaphs nag e', '']
[('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT'), ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT'), ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT'), ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT'), ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT'), ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT'), ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT'), ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT'), ('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT')]
Traceback (most recent call last):
  File "etl_main.py", line 104, in <module>
    read_files("C:\PersonalProj\interviews\interview-test-data-engineer\data",".tbl","|",bad_files,cursor)
  File "etl_main.py", line 90, in read_files
    result = cursor.executemany('INSERT INTO ' + table_name + ' VALUES ('+ ('?,' * len(dic)).strip(",") + ')',  messages)
sqlite3.IntegrityError: datatype mismatch

C:\PersonalProj\interviews\interview-test-data-engineer>python etl_main.py
[('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\customer.tbl', {9}, 1500), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\lineitem.tbl', {17}, 60175), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\nation.tbl', {5}, 25), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\orders.tbl', {10}, 15000), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\part.tbl', {10}, 2000), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\partsupp.tbl', {6}, 8000), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\region.tbl', {4}, 5), ('C:\\PersonalProj\\interviews\\interview-test-data-engineer\\data\\supplier.tbl', {8}, 100)]
[]
('C_CUSTKEY', 'C_NAME', 'C_ADDRESS', 'C_NATIONKEY', 'C_PHONE', 'C_ACCTBAL', 'C_MKTSEGMENT', 'C_COMMENT')
1
Customer#000000001
IVhzIApeRb ot,c,E
15
25-989-741-2988
711.56
BUILDING
to the even, regular platelets. regular, ironic epitaphs nag e
