# Awwards
A replica of https://www.awwwards.com/ site. Built using the Django framework

## Author
* Loise Muthoni

## Project Description
A user of the application should be able to:

1. View posted projects and their details
2. Post a project to be rated/reviewed
3. Rate/ review other users' projects
4. Search for projects
5. View projects overall score
6. View my profile page

# Setup and installation requirements
You need to have the following installed:
* Python3+
* Pip
* Virtual ```$ python3.7 -m venv virtual```
* Activate the virtual environment ```. virtual/bin/activate```
* Django ```(virtual)$ pip install Django==1.11.17```
* Get all requirements ```pip freeze > requirements.txt```

### Running the server
```python manage.py runserver```

# Behaviour Driven Development

| Input        | Output           | Behavior  |
| ------------- |:-------------:| -----:|
| Visit awwwards-clone site| Various projects are displayed  | User can review projects |
| Click on image| Image details displayed | Image details displayed |
| Search project | Images for project are displayed | App gets the projects for the searched project |
| Visit profile | Projects posted by user are displayed | App gets projects for user |
| Visit Admin | Prompts for admin credentials | Admin dashboard displayed |
| API projects | api with a list of projects is displayed | api displayed |

