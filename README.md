# 개꿀 독서과정 검색기 :mag::eyes:

> written by ty.park

  

## 개발의도

- **업무에 오픈소스 생성AI 적용을 위한 파일럿프로젝트**
- 이지러닝 개꿀 독서과정 검색
  - 쿼리셀렉터 등을 사용하여 독서과정 책제목 목록 추출
  - OPEN API를 사용해 카테고리 페이지수 등 정보를 수집
  - **오픈소스 생성AI를 사용해 대화형 검색기능**을 제공

​    

## 개발내용상세

- **파이썬 기본모듈**
  - [Requests: HTTP for Humans™ — Requests 2.28.2 documentation (python-requests.org)](https://docs.python-requests.org/en/latest/)
  - file reading
    - for line in file : 메모리에 파일 라인 단위로 올라감
    - file.readLines() : 메모리에 모든 파일 내용이 올라감
- **책검색 오픈API**
  - 국립중앙도서관 API
  - :white_check_mark: 알라딘
    - 안내 페이지 [[알라딘서재]OpenAPI 안내 (aladin.co.kr)](https://blog.aladin.co.kr/openapi/6695306)
    - 상세 매뉴얼 [알라딘 Open API 매뉴얼 - Google Docs](https://docs.google.com/document/d/1mX-WxuoGs8Hy-QalhHcvuV17n50uGI2Sg_GHofgiePE/edit)
- **대화형 검색기능**
  - [nebullvm/apps/accelerate/chatllama at main · nebuly-ai/nebullvm (github.com)](https://github.com/nebuly-ai/nebullvm/tree/main/apps/accelerate/chatllama)
  - [[AI 모델 탐험기] #21 GPT-3의 오픈소스 버전, GPT-J | by AI Network | AI Network_KR | Medium](https://medium.com/ai-networkkr/ai-모델-탐험기-21-gpt-3의-오픈소스-버전-gpt-j-de3bdcdf65dd)
  - [[기획] OpenAI-ChatGPT의 오픈소스 대안 - 공개SW 포털 (oss.kr)](https://www.oss.kr/oss_guide/show/2929db63-ff0a-46c3-adab-ca336320441f?page=1)
  - [GPT-Neo : GPT-3 규모의 모델을 오픈소스/무료로 만드는 프로젝트 | GeekNews (hada.io)](https://news.hada.io/topic?id=3599)
  - :white_check_mark: [kakao KoGPT 이해하기 | Kakao Developers 문서](https://developers.kakao.com/docs/latest/ko/kogpt/common)
    - 요청/응답 포함 2048 토큰 처리 가능
    - 결과기준 월 1000건 무료쿼터 제공

  

## 고민한내용

- **한정된 2048 토큰으로 검색기능 제공하기**
  - 질의대상 모든 데이터를 생성 AI 모델에 학습시켜 사용자 입력에 따라 결과를 출력하면 좋겠지만
  - 기술적으로도 비용적으로도 어려운 일임
  - 따라서 사용자 질의문을 가공하는 데 생성 AI를 사용하기로 함

- **결론 : 질의 대상 데이터 대신에, 질의문을 처리하기 **

  - 사용자 질의문에서 데이터를 정렬할 칼럼정보를 추출하고

  - 정렬 및 결과출력은 파이썬이 수행함
