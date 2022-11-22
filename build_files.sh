echo "Build Start"
python 3.7 -m pip install -r requirments.txt
python3.7 manage.py collectstatic --noinput --clear
echo "Build End"