echo "Build Start"
pip install -r requirments.txt
python3.7 manage.py collectstatic --noinput --clear
echo "Build End"