def create_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'mail': request.Post["mail"],
            'password': request.POST["password"]
        }
        art = None
        try:
            art = User.objects.get(username=form["username"])
            art = User.objects.get(email=form["mail"])
            # если юзер существует, то ошибки не произойдет и
            # программа удачно доберётся до следущей строки
            print(u"Такой юзер уже есть")
        except User.DoesNotExist:
            print(u"Такого юзера ещё нет")    
        if form["username"] and form["mail"] and form["password"] and art is None:
            art = User.objects.create_user(username=form["username"],
                                        email=form["mail"],
                                        password=form["password"])
            return redirect(archive)
        else:
            if art is not None:
                form['errors'] = u"Логин или почта уже занята"
            else:   
                form['errors'] = u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request, 'registration.html', {})