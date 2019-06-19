from django.shortcuts import render, HttpResponse, redirect
from .models import Comment
# ======================================================================================================================
def index(request):
    return render(request, "wall_app/index.html")
# ======================================================================================================================
def post_message(request):

    if request.method != "POST":
        print("ERROR: Expecting a POST request to be made to this route")

    # Step 0: Grab the value of the field from request.POST['message']
    message = request.POST['message']

    # Step 1: Create a new message row in the Table
    comment = Comment.objects.create(message=message)

    # Step 2: Pass table into HTML
    comments = Comment.objects.all()
    context = {'comments': comments}

    print(comments)

    return render(request, "wall_app/index.html", context)