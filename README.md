# Raspberry Pi Fotobox
## Was?
Dieses Repository enthält Beschreibung und Scripte zum Bau einer Fotobox auf Basis des Raspberry Pi 3, wie in BitBastelei #151 vorgestellt.

## Warum?
Warum nicht?

## Womit?
Das Projekt wurde durch [Reichelt elektronik](https://www.reichelt.de) unterstützt. Es wurden folgende Bauteile verwendet:
* [Raspberry Pi 3](https://www.reichelt.de/Einplatinen-Computer/RASPBERRY-PI-3/3/index.html?ACTION=3&GROUPID=8084&ARTICLE=164977&OFFSET=75&) - Single board computer. verwendet da RPi eine große Community hat und der 4-Kern ARM genügend Leistungsreserven für komplexe Filter o.Ä. bereithält
* [Raspberry Pi Camera V2.1](https://www.reichelt.de/Weiteres-Zubehoer/RASP-CAM-2/3/index.html?ACTION=3&GROUPID=6671&ARTICLE=170853&OFFSET=75&) - Kamera für den Raspberry Pi. 8MPx. Nutzt CSI als Kommunikationsschnittstelle und kann so Bilder direkt über die GPU rendern, daher hohe Bildwiderholraten möglich. 
* Dell UltraSharp 1704FPT - alter Monitor mit DVI-Eingang zur Anzeige.
_Alternativ: Jeder Monitor mit digitalem Eingang (HDMI, DP, DVI). Hinweis: Software ist aktuell auf 1280x1024 ausgelegt)_
* [Goobay GOO 71889](https://www.reichelt.de/Ladegeraete-fuer-USB-Geraete/GOO-71889/3/index.html?ACTION=3&GROUPID=5158&ARTICLE=175360&OFFSET=75&) - Micro USB-Netzteil für RPi3, 5V/2.5A.
_Alternativ: Beliebiges Micro-USB-Netzteil mit genügend Leistung für RPi3_
* [INTENSO 8GB Micro SD](https://www.reichelt.de/SD-Karten-Micro-/INTENSO-MSDHC8G/3/index.html?ACTION=3&GROUPID=7098&ARTICLE=89786&OFFSET=75&) - Speicherkarte für das Betriebssystem des RPi3
_Alternativ: Beliebige Micro-SD-Karte mit >8GB_
* 3 Stk. [AV 19-00](https://www.reichelt.de/Vandalismus-Taster/AV-19-00/3/index.html?ACTION=3&GROUPID=7588&ARTICLE=27911&OFFSET=75&) - Taster zur Bedienung. Im diesem fall 19mm Vendalismus-Taster wg. Größe und Spritzwasserschutz
_Alternativ: Beliebige Taster mit Schließer_
* [VT-1310 :: Kuppelleuchte](https://www.reichelt.de/Decken-Einbauleuchten/VT-1310/3/index.html?ACTION=3&LA=20&GROUP=L4&GROUPID=5953&ARTICLE=201361&START=0&SORT=preis&OFFSET=75) - als zusätzliche Beleuchtung. 8W LED, CRI >70. Hier mit Netzanschluss um zusätzliche Netzteile/Spannungen zu vermeiden.
_Optional. Alternativ: Beliebige Lampe mit entsprechender Stromversorgung, vorzugsweise gerichtet_
* [BRENNENSTUHL 1 15862 0](https://www.reichelt.de/Steckdosenleiste-allgemein/EL-3-FACH-OS-SW/3/index.html?ACTION=3&GROUPID=4280&ARTICLE=34978&OFFSET=75&) - 3-fach-Steckdosenleiste um alle Geräte der Fotobox einstecken zu können
_Optional. Alternativ: Beliebiger Mehrfachstecker mit genügend Steckplätzen_
* DVI <-> HDMI-Kabel - z.B. [HDG-XHC030-005](https://www.reichelt.de/A-V-Kabel-HDMI-/HDG-XHC030-005/3/index.html?ACTION=3&GROUPID=3615&ARTICLE=192400&OFFSET=75&). Anschluss passend zu Monitor
_Alternativ: Beliebiges passendes Anschlusskabel_
* Drahtbrücken mit Buchse - z.B. [Buchse-Buchse 15cm](https://www.reichelt.de/Experimentier-Steckboards/STECKBOARD-JBBGR/3/index.html?ACTION=3&GROUPID=7791&ARTICLE=139538&OFFSET=75&). Einfachste Möglichkeit passende Buchsen für RIp-GPIO-Header zu erhalten
_Optional. Alternativ: Beliebige passende Buchsen oder direkt anlöten_
* SD- oder MicroSD-Kartenleser - z.B. [CARDREADER-SD](https://www.reichelt.de/Kartenleser-und-Adapter/CARDREADER-SD/3/index.html?ACTION=3&GROUPID=5262&ARTICLE=144560&OFFSET=75&).
* USB-Stick mit VFAT-Dateisystem nach Wahl zur Speicherung der Bilder

## Wie?
Der Aufbau der Elektronik ist in BitBastelei #151 beschrieben, das Gehäuse wird in einer späteren Forge erstellt
[![BitBastelei #151 @ YouTube](http://img.youtube.com/vi/pN4XiSHx7JQ/0.jpg)](http://www.youtube.com/watch?v=pN4XiSHx7JQ)

Gundlegend:
* Hardware zusammenstecken
* Raspian installieren
* In *sudo raspi-config* unter *Interface* die Kamera einschalten
* Netzwerk anschließen bzw. WiFi einrichten
* sudo apt update
* sudo apt upgrade
* sudo apt install openbox xorg python3 python3-picamera python3-pyqt5 sxiv tmux lightdm vim usbmount python3-rpi.gpio git
* git clone https://github.com/adlerweb/fotobox.git fotobox
* Änderungen in /etc/usbmount/usbmount.conf
  * Aus **MOUNTOPTIONS** die Option *sync* entfernen
  * FS_MOUNTOPTIONS="-fstype=vfat,uid=1000"
* Ordner ~/.config/openbox anlegen
* Datei ~/.config/openbox/autostart
    xset -dpms &
    xet s off &
    python3 ~/fotobox/fotobox.py
* Hoffen, dass alles funktioniert

## Was nun?
Wie die meisten meiner Projekte kann dieses Repository nur als Vorlage dienen - es gibt viel zu verbessern. Warum kein besseres Design? Soundeffekte? Automatisches Posten auf Instagram, Facebook oder Twitter? Eingebauter Fotodrucker mit CUPS? LED-Lampe nur bei der Aufnahme einschalten? Viel ist möglich.
Ich nutze z.B. auf dem Raspberry Pi einen Webserver (Nginx/PHP-FPM) mit [UberGallery](http://www.ubergallery.net/) um Besuchern per WLAN einen Blick auf die Fotos zu ermöglichen.

