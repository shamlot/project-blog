def input_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }
        if form["username"] and form["password"]:
            user = authenticate(request, username=form["username"],password=form["password"])
            if user is None:
                form['errors'] = u"Такой пользователь не зарегестрирован!"
                return render(request, 'auth.html', {'form': form})
            else:
                login(request, eser)
            return redirect(archive)    
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'auth.html', {'form': form})
    else:
        return render(request, 'auth.html', {})