# sentiment_analysis

## 우주청 감성분석 모듈

___

### dependency
```
pandas==1.1.4
konlpy==0.5.2
```


### 사용법

jupyter notebook에서

```python
!git clone https://github.com/ourlocalpetition/sentiment_analysis.git # 최초 1번만

# 패키지 내로 디렉토리 이동
import os
os.chdir('./sentiment_analysis')

# import 하고 감성분석
from sent_analysis import SentAnalysis
mysent = '7월 4주차에 벌어진 두 정당의 지지도 역전은 ‘컨벤션 효과’와도 관계가 있는 것으로 보인다. 민주당이 지난달 중순까지는 대선 경선에 대한 관심과 맞물려 지지도가 상승했으나, 민주당 경선 일정이 코로나19 여파로 늦춰진 동안 지난달 말 야권 유력 대선 주자 윤석열 전 검찰총장이 국민의힘에 전격 입당하면서 지지도가 함께 상승한 것으로 보인다.'

_sent = SentAnalysis(mysent)
_sent.count_pos()

>>> {'positive': 5, 'neutral': 0, 'negative': 1}
```
