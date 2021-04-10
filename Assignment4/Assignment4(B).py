from imdb import IMDb  # imdb package를 import한다.

ia = IMDb()  # ia라는 객체를 만든다.
asung = ia.search_person('Asung Ko')
# print(asung[0].personID)를 이용해 확인해보면, 'Asung Ko'의 id가 2163344이라는 것을 알 수 있었다.
Person = ia.get_person('2163344')  # id 2163344를 가진 'Asung Ko'의 정보들을 담은 Person 객체를 생성한다.
"""
print(Person.default_info)를 통해 확인해보면, filmography라는 정보가 담겨있는 것을 알 수 있었다.
print(Person['filmography'])를 통해 확인해보면 dictionary 형식으로 actress 키에 배우로서 출연한 작품들이 list로 담겨있고,
self 키에 출연한 티비 프로그램들이 list로 담겨있는 것을 확인할 수 있었다.
따라서, actress 키의 value들에 접근해서 print했다.
"""
order = 1  # 영화들의 순서를 표시하기 위한 숫자이다.
for m in Person['filmography']['actress']:  # filmopgraphy의 dictionary에 actress 키의 value들에 접근했다.
    # 몇 번째인지 표시하기 위해 order를 print한 후, value 들의 제목과 연도에 접근해 print 한다.
    print(order, ':', m['title'], '(', m['year'], ')')
    order += 1  # 그 다음 영화를 표시해야 하므로, 1을 더한다.
