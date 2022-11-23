echo "Build Start"
pip install -r requirements.txt
python3.8 manage.py collectstatic --noinput
echo "Build End"