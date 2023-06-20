import random
import string

from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, CreateView

from sky_django import settings
from users.forms import UserProfileForm, UserCreateForm
from users.models import User
from users.utils import generate_code


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def post(self, request, *args, **kwargs):
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.kwargs['pk']})

    def get_object(self, queryset=None):
        object = User.objects.get(pk=self.kwargs['pk'])
        return object


def confirm_code(request, email):
    if request.method == 'POST':
        verify_code = request.POST.get('verify_code')
        user = User.objects.get(email=email)
        if user.verify_code == verify_code:
            user.is_active = True
            user.save()
            return redirect(reverse('users:login'))
        else:
            raise ValidationError(f'You have used the wrong code!')
    else:
        context = {'title': 'Подтверждение почты'}

    return render(request, 'users/confirm_code.html', context)



class UserRegisterView(CreateView):
    model = User
    form_class = UserCreateForm
    template_name = 'users/register.html'

    def get_success_url(self):
        return reverse('users:confirm_code', kwargs={'email': self.object.email})

    def form_valid(self, form):
        if form.is_valid():
            new_user = form.save(commit=False)
            code = generate_code()
            new_user.verify_code = code
            new_user.save()
            send_mail(
                subject='Вы зарегистрировались',
                message=code,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[new_user.email]
            )

        return super().form_valid(form)
        # return HttpResponseRedirect(self.success_url)


def generate_password(request):
    symbols = string.ascii_letters
    new_passowrd = ''.join([random.choice(symbols) for _ in range(10)])
    send_mail(
        subject='Смена пароля',
        message=f'Ваш новый пароль {new_passowrd}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_passowrd)
    request.user.save()
    return redirect(reverse('users:login'))
