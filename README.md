#ONLINE STORE(Z Kids Toys Store )
THis App was built with the help with an online Django course
This application consists of multiple apps that interacts together. 
The application includes:
1- shop app to manage categories and the associated products.
2- search app to handle all searches by product name or a keyword in the description.
3- cart app to manage purchases and checkout as well processing payements with Stripe.
4- order app to manage all orders and payement information   

### To install

1. Create and activate a virtual environment. Use Python3 as the interpreter. Suggest locating the venv/ directory outside of the code directory.

2. pip install -r requirements.txt

3. python manage.py makemigrations

4. python manage.py migrate

5. python manage.py runserver

Note: Payments are processed using Stripe API that requires a public key and a secret key.
Please register an account in Stripe to get those keys.


Site at

127.0.0.1:8000

### Create superuser


`python manage.py createsuperuser`

enter username and password

will be able to use these to log into admin console at

127.0.0.1:8000/admin



