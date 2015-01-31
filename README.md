# NRK subtitle nedlaster

Jeg skulle egentlig bare se på NRKs *Kampen om Tungtvannet*, men siden jeg ikke har Flash, og Chrome (eller NRK nettTV) ikke ville la meg se med HLS (se instillinger [her](http://tv.nrk.no/innstillinger)!), måtte jeg ta til takke med å bruke en egen HLS klient. Da fungerte selvsagt ikke undertekster.

Dette scriptet laster ned og parser teksten til en serie, gitt at dette er lagret på samme måte som Kampen om Tungtvannet (jeg tipper NRK lagrer alle undertekster likt, men jeg har ikke testet), for deretter å printe ut til `stdout` en `.srt` fil.
