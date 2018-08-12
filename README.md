# mythra-cms
Mythra.fi site with Django CMS

## Installing

### Setup virtualenv with Python 3
```bash
virtualenv -ppython3 venv
source venv/bin/activate
```

### Clone the project and install requirements
```bash
git clone ...
cd mythra-cms
pip install -r requirements.txt
```

### Create your copy of local settings
```bash
cd mythra
cp local_settings.py.template local_settings.py
cd ..
```

### Migrate to initialize your database
```bash
python manage.py migrate
```

### Compile translations
```bash
python manage.py compilemessages
```

### Create superuser
```bash
python manage.py createsuperuser
```

### Compile styles with SASS
```
npm i
npm run build
```

### Launch server
```bash
python manage.py runserver
```
