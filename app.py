import streamlit as st
import openai
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size = 1000,
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(
        texts=text_chunks, 
        embedding=embeddings)
    return vectorstore





def main():

    #openai.api_key = st.secrets['OPENAI_API_KEY']



    st.set_page_config(page_title='PDF Chatbot', page_icon='🤖')

    st.header('Chat with your PDF file!! 📄')
    st.text_input('What do you want to know from your document?')

    with st.sidebar:
        st.subheader('Your files')
        pdf_docs = st.file_uploader('Upload your PDF files here', accept_multiple_files=True)
        if st.button('Load'):
            with st.spinner('Loading'):

                #get pdf text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)

                #get chunks
                text_chunks = get_text_chunks(raw_text)
                #st.write(text_chunks)

                #create vector store
                vectorstore = get_vectorstore(text_chunks)


if __name__ == '__main__':
    main()