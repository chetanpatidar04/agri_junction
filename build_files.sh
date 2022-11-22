echo "Build Start"
python -m pip install -r requirements.txt
python manage.py collectstatic --noinput
echo "Build End"