'Tablet' is an online marketing project about tablet computers.

It contains products, brands and news.

The project uses Django version 1.3.

Other technologies used are: jQuery/JavaScript (for the navigation menu), CSS (with some CSS3 elements) und HTML (some HTML5 elements) for the front-end und MySQL as DBMS/database.

Note:

The Django Comments form in the templates needs the 'request' variable'. In settings.py, 'django.core.context_processors.request' must be added to the other default processors in TEMPLATE_CONTEXT_PROCESSORS:

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + ( 'django.core.context_processors.request', )

----

'Tablet' ist ein Online-Marketing-Projekt über Tablet-Computer.

Es enthält Produkte/Modelle, Marken und Nachrichten. 

Das Projekt verwendet Django Version 1.3 (entwickelt auf Ubuntu Linux).

Die anderen Technologien sind: jQuery/JavaScript (für das Menü), CSS (einige CSS3-Elemente) und HTML (einige HTML5-Elemente) für Front-End und MySQL für die Datenbank.

Hinweis:

Die Django Comments Form in dem Template braucht die 'request' Variable. So in 'settings.py' muss 'django.core.context_processors.request' zu den anderen Default-Prozessoren in den TEMPLATE_CONTEXT_PROCESSORS hinzugefügt werden:

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
)
