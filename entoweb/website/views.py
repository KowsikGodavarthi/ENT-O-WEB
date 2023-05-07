from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from website.forms import FeedbackForm
from website.models import Booking


# Create your views here.
def home(request):
    return render(request, 'home.html')
def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.save()
            return redirect('welcome')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    error_message = ''
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/signup')
        else:
            error_message = 'Invalid email or password'
    return render(request, 'Login.html', {'error_message': error_message})

def signup(request):
    return render(request, 'signup.html')
def signup2(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        return render(request, 'welcome.html')
    else:
        return HttpResponse("INCORRECT")
def gallery(request):
    return render(request, 'gallery.html')
def payment(request):
    return render(request, 'Pay.html')
def gallery1(request):
    return render(request, 'gallery1.html')
def gallery2(request):
    return render(request, 'gallery2.html')
def gallery3(request):
    return render(request, 'gallery3.html')
def gallery4(request):
    return render(request, 'gallery4.html')
def aboutus(request):
    return render(request, 'aboutus.html')
def bookings(request):
    if request.method == 'POST':
        # Get the form data
        artist = request.POST.get('artist')
        date = request.POST.get('date')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        # Create a new Booking object and save it to the database
        booking = Booking(artist=artist, date=date, name=name, email=email, phone=phone)
        booking.save()

        # Render a success message to the user
        return HttpResponse('Booking created successfully')
    else:
        # Render the booking form
        return render(request, 'bookings.html')
def contactus(request):
    return render(request, 'contactus.html')
def registercust(request):
    return render(request, 'Register_Customer.html')
def registerent(request):
    return render(request, 'Register_Entertainer.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def forget_password(request):
	if request.method == 'POST':
		email = request.POST.get('email')
		if is_valid_email(email):
			new_password = generate_password()
			message = f"Your new password is: {new_password}"
			send_mail(
			    'New Password',
			    message,
			    settings.EMAIL_HOST_USER,
			    [email],
			    fail_silently=False,
			)
			# Here you would update the user's password in the database, but for the sake of this example we'll just show a success message to the user
			message = "Your password has been reset. Check your email for the new password."
		else:
			message = "Invalid email address."
	return render(request, 'forget_password.html', {'message': message})