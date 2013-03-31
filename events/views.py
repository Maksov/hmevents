from django.views.generic.base import TemplateView


class TestPage(TemplateView):
    template_name = 'events/testpage.html'
    