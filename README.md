# Maajaam
maajaama kood: api, gui jms.

me kasutame pyseriali, et lugeda cansati saadetud infot.
me parsime seda csv ja StringIO abil

Meil on eraldi thread, mis kogu aeg loeb serial porti

kui ta info kätte saab, siis ta parsib ära ja annab fn-le handle_data, mis peaks kuvama seda ekraanil ja uuendama graafikuid.

Graafikut jaoks kasutame PyQT.


Soovitan pip-iga installida endale pyserial, pyqt jms kui pole juba installitud.
