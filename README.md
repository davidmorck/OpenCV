# Python YOLO training

* I mappen __annottionsXML__ finns de XML-filer som ska användas för att träna keras. Den skapades med __converter.py__.

* I mappen __Images__ finns alla bilder som används för träning och testning.

* I mappen __IMGLABEL__ finns både bilder och labels.

* I mappen __Labels__ finns labels som säger vilket objekt som är markerat och var merkeringen är. 

* __classes.txt__ innehåller namnen på objekt jag har använt.

* __converter.py__ kombinerar labels och bilder för att skapa XML-filer.

* __main.py__ är koden som startar programmet där man gör markeringar av objekt i bilder. 

* __process.py__

* __renamer.py__ är en kod som gör om **jpg** till **JPEG**.