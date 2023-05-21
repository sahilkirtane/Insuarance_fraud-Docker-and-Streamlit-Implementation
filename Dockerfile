FROM python

WORKDIR /insurance

EXPOSE 8501

COPY . /insurance

RUN pip install -r requirements.txt

CMD streamlit run server.py