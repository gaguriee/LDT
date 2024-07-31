import os
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

# LLM 체인 생성
llm = ChatOpenAI(temperature=0.2, model_name="gpt-3.5-turbo")
chain_markdown = LLMChain(llm=llm, prompt=prompt_markdown)
chain_openapi = LLMChain(llm=llm, prompt=prompt_openapi)

def generate_documentation(source_code, api_name, api_endpoint):
    """소스 코드를 입력받아 API 문서를 생성"""
    markdown_doc = chain_markdown.run(source_code=source_code, api_name=api_name, api_endpoint=api_endpoint)
    openapi_doc = chain_openapi.run(source_code=source_code, api_name=api_name, api_endpoint=api_endpoint)
    return markdown_doc, openapi_doc

def save_documentation(documentation, filename):
    """생성된 문서를 파일로 저장"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(documentation)
    print(f"Documentation has been saved to {filename}")

# 사용 예시
api_name = "매니저 관리"
api_endpoint = "https://admin.tworldfriends.co.kr/supervisor/managers"
source_code = """
    [
        {
            "filename": "/Users/user/Desktop/projects/vsolution/tworldfriends/laravel/app/Http/Controllers/Manager/Supervisor/ManagerController.php",
            "sourceCode": "    public function index(Request $request)\n    {\n        $keyword = $request->input('keyword', false);\n        $abilities = $request->input('abilities', false);\n        $needsUpdate = $request->boolean('needs_update');\n        $swingId = $request->boolean('swing_id');\n\n        $query = Manager::query()->has('department');\n\n        if ($keyword) {\n            $query->where(function ($query) use ($keyword) {\n                $query->orWhere('name', 'like', '%' . $keyword . '%')\n                    ->orWhere('username', 'like', '%' . $keyword . '%');\n            });\n        }\n\n        if ($abilities) {\n            $query->whereJsonContains('abilities', $abilities);\n            $query->whereJsonLength('abilities', count($abilities));\n        }\n\n        if ($request->has('swing_id')) {\n            $swingId\n                ? $query->whereNotNull('swing_id')\n                : $query->whereNull('swing_id');\n        }\n\n        if ($request->has('needs_update')) {\n            $query->where('needs_update', $needsUpdate);\n        }\n\n        return new ManagerCollection(\n            $query->orderByDesc('first_logged_at')->paginate()\n        );\n    }\n",
            "fileComment": "/**\n * @tags \uad00\ub9ac\uc790(\ubcf8\uc0ac)\n */",
            "methodComment": "/**\n     * @see ManagerCollection::toArray\n     * @see SimpleDepartmentResource::toArray\n     *\n     * @param Request $request\n     * @return ManagerCollection\n     */"
        },
        {
            "filename": "/Users/user/Desktop/projects/vsolution/tworldfriends/laravel/app/Http/Resources/ManagerCollection.php",
            "sourceCode": "    public function toArray($request)\n    {\n        return $this->collection->map(function ($manager) {\n            return [\n                'id' => $manager->id,\n\n                'name' => $manager->name,\n                'email' => $manager->email,\n                'tel_number' => $manager->tel_number,\n                'swing_id' => $manager->swing_id,\n                'username' => $manager->username,\n\n                'role' => $manager->role,\n                'abilities' => $manager->abilities,\n                'needs_update' => $manager->needs_update,\n\n                'department' => new SimpleDepartmentResource($manager->department),\n\n                'created_at' => optional($manager->created_at)->toISOString(true),\n                'updated_at' => optional($manager->updated_at)->toISOString(true),\n            ];\n        });\n    }\n",
            "fileComment": "",
            "methodComment": ""
        },
        {
            "filename": "/Users/user/Desktop/projects/vsolution/tworldfriends/laravel/app/Http/Resources/SimpleDepartmentResource.php",
            "sourceCode": "    public function toArray($request)\n    {\n        return [\n            'code' => $this->code,\n            'name' => $this->name,\n            'type' => $this->type,\n        ];\n    }\n",
            "fileComment": "/**\n * @mixin Department\n */",
            "methodComment": ""
        }
    ]
"""

# 문서 생성
markdown_doc, openapi_doc = generate_documentation(source_code, api_name, api_endpoint)

# 문서를 파일로 저장
save_documentation(markdown_doc, "output/manager_api_documentation_3.5.md")
save_documentation(openapi_doc, "output/manager_api_documentation_3.5.yml")

# 생성된 문서 내용 출력 (선택사항)
print(markdown_doc)
print(openapi_doc)
