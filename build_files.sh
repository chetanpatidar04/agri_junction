echo "Build Start"
pip install -r requirements.txt
python3.7 manage.py collectstatic --noinput
echo "Build End"
