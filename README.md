# Doctor online Task


## Installation

Use the package manager [pip3](https://pip.pypa.io/en/stable/) to install all packages.

```bash
pip3 install djangorestframework
pip3 install djangorestframework-jwt
pip3 install django-rest-auth django-allauth
```

## To run server
```bash
python3 manage.py runserver
```

## To login as super admin
```
http://127.0.0.1:8000/admin
username : admin
password : admin
```
## urls
#### To login
```
http://127.0.0.1:8000/auth/login/
```
#### To register as patient or to show all patients
```
http://127.0.0.1:8000/patient/all

```
#### To register as doctor or to show all doctors
```
http://127.0.0.1:8000/doctor/all

```
#### To show patient details or to update or delete it if you created it
```
http://127.0.0.1:8000/patient/details/{{any id}}

```
#### To show patient details or to update or delete it if you created it
```
http://127.0.0.1:8000/patient/details/{{any id}}

``` 
#### To create clinic or to show all clinics

```
http://127.0.0.1:8000/clinic/all

```
#### To show clinic details or to update or delete it if you created it
```
http://127.0.0.1:8000/clinic/details/{{any id}} 

```
#### To reserve clinic or show all reservations
```
http://127.0.0.1:8000/patient/all-reservations

```
#### To show reservation details or to update or delete it if you created it

```
http://127.0.0.1:8000/patient/reservation/{{any id}}

```
