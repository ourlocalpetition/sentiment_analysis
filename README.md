# sentiment_analysis

## 우주청 감성분석 모듈

___

사용법:

jupyter notebook에서

```python
!git clone https://github.com/ourlocalpetition/sentiment_analysis.git # 최초 1번만
!mv ./sentiment_analysis

from sent_analysis import sent_analysis
mysent = '분석할 문장'
_sent = sent_analysis(mysent)
_sent.count_pos()

>>> {'positive': 5, 'neutral': 0, 'negative': 1}
```

분석결과
