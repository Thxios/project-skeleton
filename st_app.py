
from api.example import ExampleAPI
import streamlit as st


@st.cache_resource
def get_api():
    return ExampleAPI()


def main():
    api = get_api()

    query = st.text_area('input')
    print(query)

if __name__ == '__main__':
    main()




