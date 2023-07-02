
from api.example import ExampleAPI
import streamlit as st


@st.cache_resource
def get_api():
    return ExampleAPI()


def main():
    api = get_api()

    query = st.text_area('input')
    response = api.query_text2text(query)

    st.write(f'Query:\n{query}')
    st.write(f'Response:\n{response}')


if __name__ == '__main__':
    main()




