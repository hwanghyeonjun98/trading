def check_connection():
    if instCpCybos.IsConnect == 1:
        print('정상적으로 연결')
    else:
        print('연결 실패')
        
check_connection()