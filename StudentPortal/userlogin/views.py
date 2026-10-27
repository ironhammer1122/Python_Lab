from django.shortcuts import render
import re

# Create your views here.
def user_login(request):
    result = ""

    if request.method == "POST":
        user_id = request.POST.get("user_id", "")
        user_pass = request.POST.get("user_pass", "")

        id_pattern = r'^[A-Za-z0-9_]{5,12}$'
        pass_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&*!]).{8,}$'

        if not re.fullmatch(id_pattern, user_id):
            result = "Invalid User ID!"

        elif not re.fullmatch(pass_pattern, user_pass):
            result = "Invalid Password!"

        else:
            result = "Validation Successful!"

    return render(request, "userlogin.html", {"result": result})