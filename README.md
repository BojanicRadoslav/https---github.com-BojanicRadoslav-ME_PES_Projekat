# https---github.com-BojanicRadoslav-ME_PES_Projekat

Zadatak projekta:
implementirati web server koji obsluzuje vise web klijenata i STM32 kontroler
Potrebno je implementirati sledece funkcionalnosti:
STM:
  Kontrola 2 mehanicka relea
  Merenje temperature i vlake koristeci DHT11 ili DHT22
Web server:
  Glavna stranica:
    prikaz trenutne vlage i temperature
  Kontrola relea:
    kontrolisanje relea od strane bilo kog konektovanog klijenta
    Live prikaz menjanja stanja izlaza
  Graficki servis:
    Prikaz baza podataka po danima
    Generisanje web stranice sa grafikom za selektovani dan(grafik zavisnosti vremena i temperature, vremena i vlage)
  Podesavanje stm:
    Interval merenja
    Offset temperature
    Offset vlage
STM konfigurator:
  Tkinger GUI aplikacija:
    podesavanje network podataka SSID i Password preko serijske komunikacije
    
STM32 periodicno salje podatke sa senzora vlage i temperature koristeci socketio event na Flask web server
Pri svakom slanju Softverska komponenta DataLogger zapisuje u odgovarajuci CSV fajl izmerene vrednosti
