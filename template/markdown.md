Analyze the provided source code and create a detailed API documentation in Markdown format. 
Focus on explaining the API logic to non-developers in simple terms. The documentation should be structured as follows:

Include the following api name and endpoint.

## {{api_name}} 
{{api_endpoint}}
 

## 처리내용
- Provide a clear, step-by-step explanation of what the API does.
- Highlight key functionalities and features.
- Explain any important business logic or data processing.

example:
이 API는 사용자 로그인을 처리합니다. 주요 기능은 다음과 같습니다:

1. 사용자 인증:
   - 제공된 이메일(또는 사용자명)과 비밀번호를 확인합니다.
   - 입력된 정보가 데이터베이스의 사용자 정보와 일치하는지 검증합니다.

2. 세션 관리:
   - 인증 성공 시, 새로운 세션을 생성합니다.
   - 세션 토큰을 생성하여 사용자에게 제공합니다.

3. 응답 전송:
   - 로그인 성공 시, 세션 토큰과 함께 사용자 기본 정보를 반환합니다.
   - 실패 시, 적절한 오류 메시지를 반환합니다.


## 요청
Create a table with the following columns: 
- 속성 (Property)
- 설명 (Description)
- 필수여부 (Required)

| 속성 | 설명 | 필수여부 |

Include all possible request parameters, their descriptions, whether they are required, and their data types.

필수여부 options: '필수' (Required), '선택' (Optional), '조건부 필수' (Conditionally Required)


## 응답
Create a table with the following columns:
- 속성 (Property)
- 설명 (Description)

| 속성 | 설명 | 

Include all possible response fields, their descriptions, and data types.


## 연동 API
List any external APIs used by this endpoint. Use the following format:
{{제공자}} > {{명칭}} {{(식별자)}} - [{{설명}}](url)

If there are no external APIs, write '없음'.

Additional guidelines:
1. Write in Korean.
2. Do not include direct code references in the documentation.
3. Analyze the provided source code thoroughly to determine all possible request parameters and response body structures.
4. Include information from query builders and resource collections in your analysis.
5. If certain fields or behaviors are conditional, explain the conditions clearly.

Source code:
{source_code}

api_name:
{api_name}

api_endpoint:
{api_endpoint}
