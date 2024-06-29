import streamlit as st



def main():
    st.set_page_config(page_title='PDF Chatbot', page_icon='🤖')

    st.header('Chat with your PDF file!! 📄')
    st.text_input('What do you want to know from your document?')

    with st.sidebar:
        st.subheader('Your files')
        st.file_uploader('Upload your PDF files here')
        st.button('Load')


if __name__ == '__main__':
    main()