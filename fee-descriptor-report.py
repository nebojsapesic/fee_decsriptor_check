import cx_Oracle


def fee_descriptor_check():
    dsn_tns = cx_Oracle.makedsn('10.10.251.7', '1814', service_name='cmsqacq.wdprocessing.pvt')
    abc = cx_Oracle.connect(user=r'Interchange_Testing', password='Interchange_Testing', dsn=dsn_tns)
    if abc:
        new_cursor = abc.cursor()
        prefix = str(input("Enter prefix: "))
        qs_query = "select feedescriptor, DBMS_LOB.substr(feedescriptorexpressionsql, 100) from twi.interchangerate where feedescriptor like '{}%'".format(prefix.upper())
        new_cursor.execute(qs_query)
        j = 0
        for row in new_cursor.fetchmany(5000):
            if row[1] is None:
                # print('{}. Compute fee descriptor is unchecked.'.format(j))
                continue
            if row[0][0:len(row[1][1:-2])] != row[1][1:-2]:
                j += 1
                print("{}. {} - {}".format(j, row[0][0:len(row[1][1:-2])], row[1][1:-2]))
    else:
        print('Login failed.')


fee_descriptor_check()

