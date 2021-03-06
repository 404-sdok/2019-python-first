20190125
====

20190125 스터디 결과

## 컴퓨터도 거르는 주석;;
코드를 작성할때, 어떤 코드에 대해 설명을 붙여야 할 때가 있습니다.

무슨 역할을 하는 코드인가, 앞으로 무엇이 필요한가에 대해서요.

하지만 우리의 말은 컴퓨터에게 실행하게 하면 오류만 나고, 컴퓨터는 코드의 그 어떤부분이라도 실행하려고 합니다.

하지만 예외가 있습니다.
```
# 주석은 컴퓨터도 거른다;
```
하지만 그런 부분에도 예외는 있습니다.

주석은 컴퓨터가 읽지 않습니다. 이유는 간단합니다. 메모니까요.

### 이건 주석이 아냐!
몇몇 웹사이트를 보면 주석이라고 소개하는 또 다른 기호가 있습니다.
```
'''
내 어-썸한 프로그램

이건 엄청 어썸하기 때문에 나 말고는 아무도 못쓸걸
'''
```
하지만 이건 주석이 아닙니다. 이건 여러줄에 걸친 문자열인데, 문자를 적어놓고 아무것도 시키질 않으니 주석처럼 사용하는겁니다.

엄연히 말하자면 **주석이 아닙니다.**

저게 주석이면 이것도 주석이죠:
```
'내가 주석이냐 이것아'
```

## 문자열을 다루자
문자열은 아무거나 적을 수 있기 때문에, 일어날 수 있는 상황이 너무 많습니다.

이전에 몇몇 상황을 대응하기 위해 이스케이프 문자를 언급했고, 이번엔 몇가지 더 알아보겠습니다.

### 문자열 포매팅
```
NAVER

Sign in

Username
Password

 * Stay Signed in
Forgot your Username or Password? | Sign up

----

Sign in & Join with
Facebook | Line

Copyright © NAVER Corp. All Rights Reserved.
```
이것은 네이버의 [영문 로그인 페이지](https://nid.naver.com/nidlogin.login)를 글자만 옮겨놓은 것 입니다.

많은 국가에 인터넷 서비스를 제공하려면 많은 언어를 지원해야 하는데, 언어를 일일이 지원하게 되면 이렇게 될겁니다.

```
sign_in = '로그인'
username = '아이디'
password = '비밀번호'
stayin = '로그인 유지하기'
forget = '아이디나 비밀번호를 잃어버렸나요?'
sign_up = '회원가입'
other_login = '다른 아이디로 로그인하기'

main_page = '''
NAVER

''' + sign_in + '''

''' + username + '''
''' + password + '''

 * ''' + stayin + '''
''' + forget + ''' | ''' + sign_up + '''

----

''' + other_login + '''
Facebook | Line

Copyright © NAVER Corp. All Rights Reserved.
'''
```
몇가지 내용만 변수로 변경했는데 본격적으로 알수 없게 변해버렸습니다.

이런 일이 비일비재하게 발생하자 문자열 포매팅이라는 방식이 생겨났습니다.

```
a = '세상'
'안녕 %s아!' % a
```
변수를 문자열 중간에 넣는 것이 아닌, 다른 대체제를 넣고 문자열이 끝나는 부분에 변수를 몰아 넣는 것입니다.

```
%d  십진수
%x  16진수
%o  8진수
%f  실수
%s  문자열
%%  %
```

하지만, 변수가 어떤 내용인지에 따라 각각 넣어두는 대체제를 달리해야했습니다.

이것이 비효율적이라고 느낀 사람들은 새로운 대체제를 만들어냈습니다.

### 중괄호를 사용한 문자열 포매팅
```
a = '세상'
'안녕 {}아!'.foramt(a)
```
이제 문자열에 합성할 변수의 내용을 고려할 필요가 없어졌습니다.

그리고 중괄호는 이런 것도 가능합니다.
```
a = '세상'
'안녕 {target}아!'.format(target = a)
```
당장 짧은 문장에서는 큰 문제가 없지만, 긴 문자열에서 중괄호의 순서를 바꾸게 되면 심히 복잡해지게 됩니다.

이를 방지하기 위해 중괄호에 이름을 붙이기 시작했고, 이러한 방식으로 사용합니다.