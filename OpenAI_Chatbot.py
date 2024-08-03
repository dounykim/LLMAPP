# 챗봇 생성을 위한 코드를 chatbot.py라는 이름으로 작성
import streamlit as st
from langchain.llms import OpenAI

st.title('간단한 챗봇')

# 사용자가 OpenAI API 키를 입력할 수 있도록 사이드바에 입력란을 생성한다. 입력된 키는 password 타입으로 표시되어 보안이 유지된다.
openai_api_key = st.sidebar.text_input('OpenAI API Key', st.secrets['OPENAI_API_KEY'], type='password')

def generate_response(input_text): # 사용자가 입력한 텍스트에 대해 GPT 모델을 사용해 응답을 생성하고, 그 결과를 화면에 표시한다.
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'): # 폼(form)을 생성하여 사용자가 텍스트 입력란(text_area)에 질문을 입력하고, 실행 버튼을 누르면 응답이 생성된다.
    text = st.text_area('프롬프트를 입력하세요:', '샌드위치를 만드는 방법에 대해 알려주세요.')
    submitted = st.form_submit_button('실행')
    if not openai_api_key.startswith('sk-'): # openai_api_key가 입력되지 않거나 잘못된 경우 경고 메시지를 표시한다.
        st.warning('OpenAI API Key를 입력하세요!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'): # API 키가 입력된 상태에서 실행 버튼을 클릭하면, 사용자가 입력한 텍스트를 기반으로 GPT 모델이 응답을 생성한다.
        generate_response(text)

# 스크롤ㄹ 기능 추가
