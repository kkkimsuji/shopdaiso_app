# 샵다이소 분석

[샵다이소.pdf](https://github.com/kkkimsuji/shopdaiso_app/files/15032864/default.pdf)

**데이터 수집**: 구글 플레이스토어, 구글 트렌드,  유튜브, 통계청 

**배운점**

- 데이터 분석 프로젝트 진행 방법
- 스크래핑 코드 작성

### 📋 프로젝트 개요

---

주변을 보면 다이소 매장에서 물건을 구매하는 사람은 많은데, 샵다이소 앱을 통해 구매하는 사람은 극히 드물다. 심지어 앱의 존재를 모르는 사람이 압도적이다. 매장 재고 확인뿐만 아니라 배송 및 픽업 서비스도 제공하는 샵다이소. 활성화되지 않은 이유는 무엇일까?

### 📊 분석 방향, 진행 방향

---

- 스크래핑 - Selenium, requests, Beautifulsoup
- 앱 이용자의 후기 분석(구글 플레이스토어)
- 앱 ’샵다이소’ 가능 매장과 오프라인 매장 비교
- 유튜브, 인스타그램, 블로그 등 다이소 관련 분석

 

### 🎯 결론

---

샵다이소 이용자들은 많은 불편함을 느끼고 있었다. 수도권 중심 서비스 제공, 서비스 오류 등 많은 불편함이 있었다. 샵다이소 서비스를 활발히 할 수 있는 서비스를 구상해보았다. 

1. 수도권 중심의 서비스
2. 앱 기능적 문제
    1. 자주 발생하는 오류
    2. 주문 취소, 배송지 변경이 불가 (고객센터와 연결해야 한다)
3. 제대로 제공되지 않는 서비스
    1. 재고 확인 - 앱의 정보가 오프라인 매장과 다르다
    2. 픽업 서비스 - 픽업 예약을 했지만 예약 시간까지 제대로 준비되어 있지 않다

### 🧠 아이디어 제안

---

‘샵다이소’ 앱의 이용자 증가를 위한 개선 방안을 고안하였다. 

1. 주문 및 픽업, 재고 확인 서비스 개선
    1. 주문 취소 및 변경, 배송지 변경 기능 추가
    2. 매장 검색 시, 현재 위치 기반 ‘내 주변 매장’ 검색 기능 추가
    3. 매장 내 재고 확인 시, ‘많음’,’보통’,’적음’ 등 단계 추가  
2. 새로운 픽업 서비스 
    1. 저렴한 단가 상 배송이 어려운 다이소 맞춤 픽업 서비스
    2. 앱에서 픽업 예약 → 해당 매장 물품 재고 확인 → 매장 내에 물품이 없을 경우 → 물류 센터에서 픽업건 물품 배송
3. 커뮤니티 개설
    1. 유튜브에 다이소의 좋은 상품을 소개하는 영상이 많음
    2. 사용자끼리 다이소 제품의 신박한 사용법, 인테리어 활용 등 아이디어 공유


---
### 주요 분석 결과
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/661aca38-e5f0-412f-975f-36758313066a)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/0e9ceff5-8078-45d4-86e3-b73d8701a2c6)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/090e4567-7771-48f9-a6d3-139227bac86d)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/5108ad71-90d7-4085-9adb-75177293271e)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/c1dcf946-e57b-48df-add6-ec4534ea694a)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/df3c559d-8609-4e7a-a5dc-2dbc2ec27a2c)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/51ea8658-de56-4526-bea4-183414e61509)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/47e0dc63-def2-4d57-b733-c65aac7a4637)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/740d44f6-3b6f-49af-b622-bc06112b2c07)
![image](https://github.com/kkkimsuji/shopdaiso_app/assets/117288953/a50480b8-eb74-49e9-a5ac-63c026f6098e)
