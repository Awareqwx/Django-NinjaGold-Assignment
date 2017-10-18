# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

import random

# Create your views here.
def index(request):
    context = {
        "acts":request.session.setdefault("acts", []),
        "gold":request.session.setdefault("gold", 0)
    }
    return render(request, "goldApp/index.html", context)

def process(request, name, goldmin, goldmax):
    acts = request.session["acts"]
    print int(goldmax)
    print int(goldmin)
    gold = random.randrange(int(goldmin), int(goldmax) + 1)
    request.session["gold"] += gold
    if name == "Casino":
        if gold != 0:
            acts.append("Entered a casino and " + ("gained " + str(gold) + " gold! Hooray!" if gold > 0 else "lost " + str(-gold) + " gold... Ouch..."))
        else:
            acts.append("Broke even at the casino")
    else:
        acts.append("Earned " + str(gold) + " from the " + name)
    request.session["acts"] = acts
    return redirect("/gold/")

def reset(request):
    request.session.pop("acts")
    request.session.pop("gold")
    return redirect("/gold/")