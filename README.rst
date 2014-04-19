One way to add translations to  -- *django-cities-lite*
=========================================================
To use this (and get translated names as a fields with django-modeltranslation)
just install app, django-modeltranslations,  

run
`./manage.py schemamigration cities-light --auto`
and 
`./manage.py migrate cities-light`
than 
`./manage.py cities_light` will import local names into django-modeltranslation fields

