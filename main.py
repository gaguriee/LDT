import os
import json
from dotenv import load_dotenv
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI

# .env 파일에서 환경 변수 로드
load_dotenv()

# OpenAI API 키를 환경 변수에서 가져옴
api_key = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = api_key

# 프롬프트 템플릿 정의
def read_template(filename):
    """템플릿 파일에서 내용을 읽어옴"""
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

template_markdown = read_template('template/markdown.md')
template_openapi = read_template('template/openapi.yml')

# 프롬프트 템플릿 생성
prompt_markdown = PromptTemplate(
    input_variables=["api_name", "api_endpoint", "source_code"],
    template=template_markdown
)

prompt_openapi = PromptTemplate(
    input_variables=["api_name", "api_endpoint", "source_code"],
    template=template_openapi
)

def create_llm_chain(model_name):
    """LLM 체인 생성"""
    llm = ChatOpenAI(temperature=0.2, model_name=model_name)
    chain_markdown = LLMChain(llm=llm, prompt=prompt_markdown)
    chain_openapi = LLMChain(llm=llm, prompt=prompt_openapi)
    return chain_markdown, chain_openapi

def generate_documentation(source_code, api_name, api_endpoint, model_name, doc_type):
    """소스 코드를 입력받아 API 문서를 생성"""
    chain_markdown, chain_openapi = create_llm_chain(model_name)
    if doc_type == "markdown":
        return chain_markdown.run(source_code=source_code, api_name=api_name, api_endpoint=api_endpoint)
    elif doc_type == "yml":
        return chain_openapi.run(source_code=source_code, api_name=api_name, api_endpoint=api_endpoint)
    else:
        raise ValueError("Invalid document type")

def save_documentation(documentation, filename):
    """생성된 문서를 파일로 저장"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(documentation)
    print(f"Documentation has been saved to {filename}")

# 사용자 입력 받기
api_name = input("API 이름을 입력하세요: ")
api_endpoint = input("API 엔드포인트를 입력하세요: ")

# 소스 코드 파일 경로 입력 받기
source_code_file = input("소스 코드 파일의 경로를 입력하세요: ")
try:
    with open(source_code_file, 'r', encoding='utf-8') as file:
        source_code = json.load(file)
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {source_code_file}")
    exit(1)
except json.JSONDecodeError:
    print(f"JSON 파일 형식이 올바르지 않습니다: {source_code_file}")
    exit(1)

# GPT 모델 선택
model_name = input("사용할 GPT 모델을 선택하세요 (gpt-4o 또는 gpt-3.5-turbo): ").strip()
if model_name not in ["gpt-4o", "gpt-3.5-turbo"]:
    print("잘못된 모델명입니다. gpt-3.5-turbo를 기본값으로 사용합니다.")
    model_name = "gpt-3.5-turbo"

# 모델 버전 가져오기
model_version = "gpt-4o" if model_name == "gpt-4o" else "3.5-turbo"

# 문서 타입 선택
doc_type = input("생성할 문서 타입을 선택하세요 (markdown 또는 yml): ").strip().lower()
if doc_type not in ["markdown", "yml"]:
    print("잘못된 문서 타입입니다. markdown을 기본값으로 사용합니다.")
    doc_type = "markdown"

# 문서 생성
documentation = generate_documentation(json.dumps(source_code), api_name, api_endpoint, model_name, doc_type)

# 파일 확장자 설정
file_extension = "md" if doc_type == "markdown" else "yml"

# 문서를 파일로 저장
save_documentation(documentation, f"output/{api_name}_{model_version}.{file_extension}")

# 생성된 문서 내용 출력 (선택사항)
print(documentation)

'''
api_name = "매니저 관리"
api_endpoint = "https://admin.tworldfriends.co.kr/supervisor/managers"
source code 경로 = "example_source_code.json"
'''