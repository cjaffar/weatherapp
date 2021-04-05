from datetime                                   import datetime, timedelta
from django.shortcuts                           import redirect

from django.conf import settings
from django.core.validators                     import validate_email
from django.core.exceptions                     import ValidationError
from django.contrib                             import messages
from django.urls                                import reverse
from django.contrib.auth.mixins                 import LoginRequiredMixin
from django.contrib.auth.views                  import LoginView
from django.views.generic                       import ListView, RedirectView

from .models                                    import Weather, City

class IndexView(LoginRequiredMixin, ListView) :

    model = Weather

    def get_queryset(self, *args, **kwargs):

        fivedays_ahead = datetime.now() + timedelta(days=5)

        weather = Weather.objects.filter(date__lte=fivedays_ahead)
        # weather = weather.annotate(day=TruncDay('date')).values('city', 'city__pk', 'date', 'min_temp', 'max_temp', 'wind_speed')

        if self.kwargs.get('pk') is not None :
            weather = weather.filter(city__pk=self.kwargs.get('pk', 0) )

        return weather.order_by('city__name', 'date')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['cities'] = City.active.all()
        context['city'] = City.active.filter(pk=self.kwargs.get('pk')).first()

        return context


class Home(RedirectView) :

    def get_redirect_url(self, *args, **kwargs):

        if not self.request.user.is_authenticated:
            return reverse('login')

        return reverse('index')


class LoginView(LoginView) :

    def form_valid(self, *args, **kwargs):

        post = self.request.POST

        try:
            validate_email(post.get('username'))
        except ValidationError as e :
            messages.error(self.request, e.message)
            return redirect('login')

        return super().form_valid(*args, **kwargs)

