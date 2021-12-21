import socket

# 네트워크 통신을 하기 위한 소켓 객체를 생성
# IPv4를 이용한 TCP통신용 소켓
# 이렇게 생성된 소켓 객체를 통해서 서버와 통신(입/출력)할 수 있다.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#https://stackoverflow.com/ : visual code 오류나면 검색해보자
print('에러없이 되는지 확인')


#통신을 하기 위한 서버와의 객체를 생성
#소켓 프로그래밍에서는 connect()을 통해서 통신하기 위한 서버의 객체를 얻어올 수 있다. 

serverAddress = socket.gethostbyname('info.cern.ch')
serverPort = 80

sock.connect( (serverAddress, serverPort))

print('DEBUG:::connect 완료')

# 서버에 전달할 HTML코드를 요청해야 한다. => Request Header 
## `header`에 대한 이해가 중요하다
## `http`를 이해한다는 것은 결국 `header`이해하는 것이다. 백엔드 할때도 중요하니 잘 잡아둬라. 
request_header = 'GET /index.html http/1.1\r\n' # \r carrige return
    # request line(start-line) + CRLF(엔터의 의미가 아니라  http헤더에서 구분자 역할을 한다. 라인과 라인, 필드와 필드 구분)
                                #CRLF사용은 규칙이다. CRLF나오기 전까지가  start-line! 
                                #우리 수업에서 가장 중요한 것은 start-line을 이해하는 것이다. 
    
   

request_header  += 'Host: info.cern.ch\r\n'
    # Header-feild 
    # 예제에서는 하나의 변수만 사용했는데 더 많은 변수 사용이 가능하다.
request_header += '\r\n'
    # 마지막 \r\n 은 header의 끝을 의미한다. 

sock.send( request_header.encode() )
response = sock.recv(1024)
print( response.decode() )


sock.close()  # 깜빡하고 안닫으면 꽉차버리는 불상사가 생긴다. 미리 써두자. 