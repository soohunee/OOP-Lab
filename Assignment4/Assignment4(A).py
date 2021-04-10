from imdb import IMDb  # imdb package를 import한다.

ia = IMDb()  # ia라는 객체를 만든다.
# get_top250_movies method를 사용해 상위에 랭크된 250개의 영화 정보를 담은 toplist라는 객체를 만든다
toplist = ia.get_top250_movies()
ranknumber = 1  # 250개 영화들의 순서를 표시하기 위한 숫자이다.
for m in toplist:  # for 문을 이용해 toplist의 원소들에 하나하나 접근한다.
    # 몇 번째인지 표시하기 위해 ranknumber를 print한 후, 원소들의 제목과 연도에 접근해 print 한다.
    print(ranknumber, ':', m['title'], '(', m['year'], ')')
    ranknumber += 1  # 그 다음 영화를 표시해야 하므로, 1을 더한다.
