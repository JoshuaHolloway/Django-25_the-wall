from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Messages, Users
from datetime import datetime
import bcrypt
# ======================================================================================================================
def get_user_info(user_id):
    return {'user': Users.objects.get(id=user_id)}
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def get_all_users_info():
    return {'users': Users.objects.all()}
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
def root(request):
    # Initialize session
    if 'user_logged_in' not in request.session:
        request.session['user_logged_in'] = {}
    return redirect("/users/reg_login")
# ======================================================================================================================
def reg_login(request):
    return render(request, "wall_app/reg_login.html")
# ======================================================================================================================
def wall(request):

    # time = datetime.now()
    # time = time.strftime("%Y/%m/%d %I:%M %p")
    return render(request, "wall_app/wall.html", {'messages': Messages.objects.all()})
# ======================================================================================================================
def post_message(request):

    if request.method != "POST":
        print("ERROR: Expecting a POST request to be made to this route")

    # Step 0: Grab the value of the field from request.POST['message']
    message = request.POST['message']

    # Step 1: Create a new message row in the Table
    #comment = Comment.objects.create(message=message) # BEFORE adding [FK]
    user_id = request.session['user_logged_in']['id']
    user = Users.objects.get(id=user_id)
    comment = Messages.objects.create(message=message, user=user)

    # Step 2: Pass table into HTML
    messages = Messages.objects.all()
    context = {'messages': messages}

    return render(request, "wall_app/wall.html", context)
# ======================================================================================================================
# ======================================================================================================================
def validate(request):

    # Return true if no errors
    valid = False

    # pass the post data to the method we wrote and save the response in a variable called errors
    errors = Users.objects.basic_validator(request.POST, Users.objects.all())

    # check if the errors dictionary has anything in it
    if len(errors) > 0:

        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)

        # Errors found
        return valid

    else:
        # No erros => Valid
        valid = True
        return valid
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def register(request):

    valid = validate(request)
    if valid:

        # Grab values from form
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password_orig = request.POST['password']

        # Hash Password
        password_hash = bcrypt.hashpw(password_orig.encode(), bcrypt.gensalt())

        # Create row in database
        user = Users.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password_hash=password_hash)

        messages.success(request, "Successfully registered")
        print("Successfully registered")
        return redirect("/users/reg_login")
    else: # not-valid
        # redirect the user back to the form to fix the errors
        return redirect("/users/reg_login")
# ======================================================================================================================
def userLogin(request):

    # Grab email from form
    email = request.POST['email-login']

    # Grab row from database IF email is in database
    # TODO: Check to see if email is in database
    user = Users.objects.get(email=email)


    # Grab entered password and test against stored hash
    password_login = request.POST['password-login']
    if bcrypt.checkpw(password_login.encode(), user.password_hash.encode()):
        print("password match")

        # Set Session with logged-in users info
        request.session['user_logged_in'] = {
            'id': user.id,
            'first_name': user.first_name,
            'logged_in': True
        }

        # Get one of the guys in this dictionary like so:
        #request.session['user_logged_in']['id']

        # return render(request, "wall_app/logged_in.html", {'user': user})
        return redirect("/wall")
    else:
        print("failed password")
        return HttpResponse("You Loose!")
# ======================================================================================================================
def logout(request):
    request.session.pop('user_logged_in')
    return redirect("/")
# ======================================================================================================================
