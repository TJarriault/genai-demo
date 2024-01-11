#Start Flask API
python app.py &

#Start streamlit frontend
streamlit run streamlit/streamlit_app.py --server.port 8502 &
