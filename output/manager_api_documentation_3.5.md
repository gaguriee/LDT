## 매니저 관리
https://admin.tworldfriends.co.kr/supervisor/managers

## 처리내용
이 API는 관리자(본사) 정보를 관리하는 엔드포인트입니다. 주요 기능은 다음과 같습니다:

1. 매니저 검색:
   - 제공된 키워드로 매니저를 검색합니다.
   - 매니저의 능력(abilities)으로 검색할 수 있습니다.
   - 필요한 업데이트가 있는 매니저를 검색할 수 있습니다.
   - 스윙 ID(swing_id)로 검색할 수 있습니다.

2. 매니저 목록 반환:
   - 검색된 매니저 목록을 페이지별로 반환합니다.
   - 각 매니저의 기본 정보와 부서 정보를 포함합니다.

## 요청

| 속성         | 설명                   | 필수여부 |
|--------------|------------------------|---------|
| keyword      | 매니저 검색 키워드      | 선택    |
| abilities    | 매니저 능력             | 선택    |
| needs_update | 업데이트 필요 여부      | 선택    |
| swing_id     | 스윙 ID 여부            | 선택    |

## 응답

| 속성          | 설명                 |
|--------------|----------------------|
| id           | 매니저 ID            |
| name         | 매니저 이름           |
| email        | 매니저 이메일         |
| tel_number   | 매니저 전화번호       |
| swing_id     | 스윙 ID              |
| username     | 매니저 사용자명       |
| role         | 매니저 역할           |
| abilities    | 매니저 능력           |
| needs_update | 업데이트 필요 여부    |
| department   | 부서 정보             |
| created_at   | 생성일시             |
| updated_at   | 업데이트 일시         |

## 연동 API
없음