fotoboxCfg = {}

fotoboxCfg['window-width']    = 1280
fotoboxCfg['window-height']   = 1024

# Depending on the camera used previews might got smaller than set here
fotoboxCfg['cam-p-width']     = 960
fotoboxCfg['cam-p-height']    = 720
fotoboxCfg['cam-p-x']         = 9
fotoboxCfg['cam-p-y']         = 261
fotoboxCfg['cam-p-hflip']     = True # False = Like a camera, True = Like a mirror

# PiCam v1: 2592x1944, v2: 3280x2464
fotoboxCfg['cam-c-width']     = 3280
fotoboxCfg['cam-c-height']    = 2464
fotoboxCfg['cam-c-hflip']     = False # False = Like a camera, True = Like a mirror

fotoboxCfg['nopi']            = False #True = Skip rasperry specific modules

fotoboxCfg['temp']            = '/tmp/fotobox/'
fotoboxCfg['save']            = '/home/pi/fotobox/images/'

fotoboxCfg['countdown']       = 3 # Seconds

fotoboxText = {}

fotoboxText['info-home']    = 'Hallo und willkommen in der Fotobox!<br>Drücke einfach auf &quot;Aufnahme&quot; und los geht es!'
fotoboxText['info-count']   = 'Los geht es!<hr><span style="font-size: 200%; font-weight: bolder;">${countdown}</span>'
fotoboxText['info-review']  = 'Alles OK?<br>Wenn ja drücke auf "Speichern". Doch zu blöd geguckt? Dann versuch es gleich nochmal.'
fotoboxText['info-view']    = 'Hier kannst du dir die Fotos der Veranstaltung direkt anschauen. Mit "Nächstes" und "Vorheriges" kannst du zwischen den Bildern wechseln. Mit "Zurück" geht es wieder zur Kamera.'

fotoboxText['btn-capture']  = 'Aufnahme ▶'
fotoboxText['btn-view']     = 'Ansehen ▶'
fotoboxText['btn-save']     = 'Speichern ▶'
fotoboxText['btn-recapture'] = '<span style="font-size: 75%">Neuer Versuch</span> ▶'
fotoboxText['btn-cancel']   = 'Abbruch ▶'
fotoboxText['btn-next']     = 'Nächstes ▶'
fotoboxText['btn-previous'] = 'Vorheriges ▶'
fotoboxText['btn-back']     = 'Zurück ▶'
fotoboxText['btn-empty']    = ''
