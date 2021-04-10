https://www.imdb.com/ 은 전 세계에서 가장 큰 영화 평가/데이터베이스 서비스 입니다.

PyPI 에 등록된 Package인 IMDbPY Library는 imdb.com 에 등재된 영화 정보를 Python으로 추출 할 수 있도록 돕는 라이브러리 입니다.

Official Documentaion 활용하여, imdb 로 부터 영화 정보를 추출하고 간단히 가공하는 코드를 작성하여 제출하세요.

IMDbPY library
PyPI - IMDbPy
IMDbPy official documentation
Example of covid
"matrix"라는 키워드가 들어가는 영화를 찾고 그 영화의 제목을 출력하기\
    from imdb import IMDb ia = IMDb()

    matrix_movies = ia.search_movie('matrix')

    for m in matrix_movies:
        print(m['title'])
        
Problem 01
imdb에서 상위에 랭크된 250개의 영화(movie)의 title과 개봉년도(year)를 console에 순차적으로 출력하는 코드를 작성하세요.
Console Output 형태 예시(예시일 뿐 실제 실행 결과는 다를 수 있음. 형태만 참조 할 것):
Rank #1 - The Shawshank Redemption (1994)
Rank #2 - Schindler's List (1993)

파일명 : 01.py
Problem 02
라이브러리를 이용해 배우 고아성(영문명 : Asung Ko)을 찾고(Person 객체를 이용) 고아성의 필모그래피(배우가 여태까지 출연한 영화 목록)을 출력하는 코드를 작성하세요.
Console Output 형태 예시(예시일 뿐 실제 실행 결과는 다를 수 있음. 형태만 참조 할 것):
Samjin Group Yeong-aw TOEIC-ban (2020)
A Resistance (2019)
La-i-peu on Ma-seu (2018)

파일명 : 02.py
code 작성 방법
Code 에 정답은 없음. 문제에 제시된 조건에 따라 정확한 결과가 출력되는지 채점
Python Indentation 등 기본적인 Python 문법 준수 필요, pep 8 준수 필요
pip 사용하여 해당 패키지를 설치 후 작성 하여야 함
본인이 왜 그렇게 코드를 작성하였는지 line-by-line으로 Comments(주석) 달 것
