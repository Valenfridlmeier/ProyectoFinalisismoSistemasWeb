from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'movies/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Lista de películas de prueba
        context['movies'] = [
            {
                'title': 'Inception',
                'year': 2010,
                'rating': 8.8,
                'poster': 'https://via.placeholder.com/300x450?text=Inception',
            },
            {
                'title': 'The Matrix',
                'year': 1999,
                'rating': 8.7,
                'poster': 'https://via.placeholder.com/300x450?text=The+Matrix',
            },
            {
                'title': 'Interstellar',
                'year': 2014,
                'rating': 8.6,
                'poster': 'https://via.placeholder.com/300x450?text=Interstellar',
            },
            {
                'title': 'The Dark Knight',
                'year': 2008,
                'rating': 9.0,
                'poster': 'https://via.placeholder.com/300x450?text=The+Dark+Knight',
            },
        ]

        return context


class AboutView(TemplateView):
    template_name = 'movies/about.html'
