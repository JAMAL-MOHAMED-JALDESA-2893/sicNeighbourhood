from django.shortcuts import render
from hood.models import Business, Post, Profile, Neighbourhood
from django.contrib.auth.models import User
from hood.forms import NewBusinessForm, NewHoodForm, PostForm, SignUpForm, UpdateProfileForm, UpdateUserForm
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

# Create your views here.
