from django.contrib import messages
from django.shortcuts import render,redirect

from app.forms import UserRegisterForm
from app.models import UserRegister,Nominations,ContestantVote

def welcomepage(request):
    return render(request,'welcome.html')

def userRegistration(request):
    userform = UserRegisterForm()
    return render(request,'userRegister.html',{'form':userform})


def userRegCheck(request):
    ur = UserRegisterForm(request.POST)
    if ur.is_valid():
        ur.save()
        messages.success(request,'User Details Saved')
    else:
        messages.error(request,ur.errors)
    return userRegistration(request)


def userLoginPage(request):
    return render(request,'userLoginPage.html')


def loginCheck(request):
    mail = request.POST.get("email")
    p_word = request.POST.get("pwd")
    try:
        gt = UserRegister.objects.get(email_id=mail,password=p_word)
        if gt:
            per_v = UserRegister.objects.filter(email_id=mail).values('idno')
            # per_l = UserRegister.objects.filter(email_id=mail).values_list('idno')
            # print(per_v)
            # print(per_l)
            # for c in per_l:ggggg
            #     print(c)
            #     print(c[0])
            for z in per_v:
                per = z['idno']
                alreg = ContestantVote.objects.values('voter_id')
                list = [x for x in alreg]
                h = [y['voter_id' ] for y in list]
                if z['idno'] in h:
                    return render(request, 'userLoginPage.html', {'message1': 'This Vote is Already Casted'})
                else:
                    name = gt.name
                    v_id = gt.idno
                    nomi = Nominations.objects.all()
                    return render(request, 'contestants.html', {'name': name, 'v_id': v_id, 'nomini': nomi})
    except UserRegister.DoesNotExist:
        return render(request, 'userLoginPage.html',{'message':'Please Enter Proper Credentials'})


def submitVote(request):
    party_nam = request.GET.get('pname')
    voter_name = request.GET.get('vname')
    voter_id = request.GET.get('vid')
    party_symbol = request.GET.get('pimg')
    cons = ContestantVote(voter_id=voter_id,voter_name=voter_name,selected_party=party_nam,selected_symbol=party_symbol)
    cons.save()
    return render(request,'thankyou.html',{"partyname":party_nam,"partysymbol":party_symbol,"votername":voter_name})


def logout(request):
    return redirect('main')