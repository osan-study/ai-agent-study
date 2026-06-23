from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# GPT-4o-mini 설정
gpt4o_mini = ChatOpenAI(
    model_name='gpt-4o-mini',
    temperature=0.7,
    max_tokens=150,
)


if __name__ == '__main__':
    # GPT-4o-mini 사용
    response_mini = gpt4o_mini.invoke(
        [
            SystemMessage(content="너는 영어를 한글로 번역해주는 전문 번역가야."),
            HumanMessage(content='Hello My Name is YunJinChoi')])
    print(response_mini.content)


# temperature	특징	예시
# 0.0	가장 확실한 단어만 선택 -	기술 문서 요약, 코드 생성
# 0.7	적당히 무작위(보통)  - 	일상적 대화, 마케팅 문구
# 1.0	창의성 ↑, 다양성 ↑ (단, 신뢰도 ↓)	시 -  스토리 생성, 브레인스토밍
# >1.2	- 매우 무작위하기 떄문에 비추천, 장난감용, 극단적 실험용
