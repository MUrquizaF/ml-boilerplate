setup:
	pip install -r requirements.txt

run-app:
	streamlit run app/main_app.py --server.runOnSave=true
