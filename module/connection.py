def check_connection(instCpCybos):
    if instCpCybos.IsConnect == 1:
        print('정상적으로 연결')
    else:
        print('연결 실패')
        