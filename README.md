# Tala_CRM
crm for Tala Assurance

#Steps
git clone https://github.com/JitBay/Tala_CRM.git
cd Tala CRM
git checkout develop
pip install -r requirements.txt

touch .env

# generate secret key
echo "SECRET_KEY=generated_secret_key" >> .env

python manage.py migrate 
python manage.py runserver
