from django.shortcuts import render
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['values'] = [
            {
                'title': 'Excelencia',
                'description': 'Nos esforzamos por brindar el mejor servicio en cada interacción.'
            },
            {
                'title': 'Integridad',
                'description': 'Actuamos con honestidad y transparencia en todo momento.'
            },
            {
                'title': 'Innovación',
                'description': 'Constantemente buscamos mejorar y modernizar nuestros servicios.'
            }
        ]
        return context


class ContactPageView(TemplateView):
    template_name = "contact_us.html"


def home(request):
    steps = [
        {
            'title': 'Elige tu Vehículo',
            'description': 'Selecciona entre nuestra exclusiva colección de vehículos premium.'
        },
        {
            'title': 'Reserva Online',
            'description': 'Proceso de reserva simple y seguro con confirmación instantánea.'
        },
        {
            'title': 'Verifica Documentos',
            'description': 'Proceso de verificación rápido y eficiente.'
        },
        {
            'title': 'Disfruta tu Viaje',
            'description': 'Recoge tu vehículo y comienza tu aventura.'
        }
    ]
    return render(request, 'home.html', {'steps': steps})
