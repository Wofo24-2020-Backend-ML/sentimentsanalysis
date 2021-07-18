from django.apps import AppConfig
from django.conf import settings
import os
import pickle

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

class AisentimentanalyzerConfig(AppConfig):
    #path = os.path.join(settings.MODELS, 'models.p')
    model_file = 'models.pkl'

    with open(model_file, 'rb') as picked:
        data= pickle.load(picked)
    model = data['model']
    vectorizer = data['vectorizer']