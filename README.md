# Picture storage — test app for OSsystem

Easy app to store pictures.

To create the app I used the Django framework, React.js, and MongoDB. It's my first app with React, so I very open to your comments and suggestions! Note, I used React.js just partially for the front-end (to create gallery), other parts made with Django templates. It's not best practice, but I did it to save development time. In the future, I ready to go deeper into React and do apps more homogenously.
## Requirements

Before running app make sure you have a fresh version of [Node.js](https://nodejs.org/en/download/) and [MongoDB](https://docs.mongodb.com/manual/installation/) installed (and Python of course).

Besides, you also **have to install others requirements**. 
Use the package manager [pip](https://pip.pypa.io/en/stable/) and [npm](https://www.npmjs.com/) for this.

In the beginning, you can easily install all the required python libs in one command: 

```bash
pip install -r requirements.txt
```

If you want to edit React app you need to set up React, webpack, and babel. For this just move in the `apps/frontend` folder and install dependencies: 

_(But it's not necessary to do it to use app. Only for developing)_

```bash
cd ./apps/frontend && npm install
```

## Run

At first time you need to set the database structure. For this just run it:

```bash
python manage.py makemigrations store
python manage.py migrate store
```

After that needs to create a database user:

```bash
python manage.py createsuperuser
```

Enter an user name, password. You can skip email.

Now, we're ready to run the app!

```bash
python manage.py runserver
```

**And, at last, very important to create a few records of Categories in Django-Admin** `http://127.0.0.1:8000/admin/`

## Preview

![Preview of working app](https://im4.ezgif.com/tmp/ezgif-4-072cf69ceb82.gif)
