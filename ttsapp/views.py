import os
import uuid
from django.conf import settings
from django.shortcuts import render
from gtts import gTTS
from .forms import TTSForm

def index(request):
    audio_url = None
    error_msg = None

    if request.method == 'POST':
        form = TTSForm(request.POST)
        if form.is_valid():
            text = (form.cleaned_data['text'] or '').strip()
            lang = form.cleaned_data['lang']
            slow = form.cleaned_data['slow']
            wanted_name = (form.cleaned_data['filename'] or '').strip()

            if not text:
                error_msg = 'Informe um texto para converter.'
            else:
                if not wanted_name:
                    wanted_name = str(uuid.uuid4())
                safe_name = ''.join(c for c in wanted_name if c.isalnum() or c in ('-', '_')).rstrip() or 'audio'

                rel_dir = 'tts'
                abs_dir = os.path.join(settings.MEDIA_ROOT, rel_dir)
                os.makedirs(abs_dir, exist_ok=True)

                rel_path = f"{rel_dir}/{safe_name}.mp3"
                abs_path = os.path.join(settings.MEDIA_ROOT, rel_path)

                tts = gTTS(text=text, lang=lang, slow=slow)
                tts.save(abs_path)

                audio_url = settings.MEDIA_URL + rel_path
    else:
        form = TTSForm(initial={'lang': 'pt'})

    context = {
        'form': form,
        'audio_url': audio_url,
        'error_msg': error_msg,
    }
    return render(request, 'ttsapp/index.html', context)
