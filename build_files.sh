echo "Build Start"
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput
echo "Build End"
