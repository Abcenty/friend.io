from django.shortcuts import HttpResponseRedirect, render

# from friends.forms import UserProfileForm
from users.models import User
from friends.models import Friends, FriendRequest

# Create your views here.


"""def basket_add(request, product_id):
    current_page = request.META.get('HTTP_REFERER')
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
        return HttpResponseRedirect(current_page)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
        return HttpResponseRedirect(current_page)"""

"""def profile(request):
    if request.method == "POST":
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form,
               'baskets': Basket.objects.filter(user=request.user),
               'total_quantity': total_quantity,
               'total_sum': total_sum
               }
   return render(request, 'friends/profile.html', context)"""

"""def basket_delete(request, id):
    basket = Basket.objects.get(id=id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))"""


def friend_add(request, user_id):
    current_page = request.META.get('HTTP_REFERER')
    friend = User.objects.get(id=user_id)
    if not Friends.objects.filter(user_id_1=request.user, user_id_2=user_id) and not Friends.objects.filter(
            user_id_1=user_id,
            user_id_2=request.user) and not FriendRequest.objects.filter(
        sender=request.user, recipient=friend) and friend.id != request.user.id:
        FriendRequest.objects.create(sender=request.user, recipient=friend)
        return HttpResponseRedirect(current_page)
    else:
        return HttpResponseRedirect(current_page)


def friend_accept(request, friend_id):
    friend = User.objects.get(id=friend_id)
    if not Friends.objects.filter(user_id_1=friend, user_id_2=request.user):
        Friends.objects.create(user_id_1=friend, user_id_2=request.user)
        FriendRequest.objects.filter(sender=friend, recipient=request.user).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def profile(request):
    context = {'friends1': Friends.objects.filter(user_id_1=request.user),
               'friends2': Friends.objects.filter(user_id_2=request.user),
               'requests': FriendRequest.objects.filter(recipient=request.user)
               }
    return render(request, 'friends/profile.html', context)


def friend_decline(request, user_id):
    pass


def friend_delete(request, user_id):
    pass
