admin_info=dict([('id','admin'),('password','12345')])
id_=input('아이디를 입력하세요')
password=input('비밀번호를 입력하세요')
if password==admin_info['password'] and id_==admin_info['id']:
    print('정보의 접근 권한이 있음니다.')
else:
    print('정보의 접근 권한이 없음니다.')

