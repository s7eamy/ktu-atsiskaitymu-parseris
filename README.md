# KTU atsiskaitymų parseris

Įrankis iš KTU suteikiamų studijų modulio kortelių geba ištraukti modulio pavadinimą, atsiskaitymus, jų galutinio pažymio dalis ir atsiskaitymo dieną, kuomet nurodama užsiėmimų diena.

### Instaliacijos instrukcijos

Parsisiųsk šitą repozitoriją į norimą direktoriją, pavyzdžiui, su komanda 

```git clone https://github.com/s7eamy/ktu-atsiskaitymu-parseris.git```

Toje direktorijoje susikurk Python virtualią aplinką:

```python -m venv .venv```

Aktyvuok virtualią aplinką:

```source .venv/bin/activate``` (Linux)
```.\.venv\Scripts\activate.bat``` (Windows cmd line)
```.\.venv\Scripts\Activate.ps1``` (Windows PowerShell)

Parsisiųsk reikiamą biblioteką:

```pip install beautifulsoup4```

### Naudojimosi instrukcijos

Įrankis iškviečiamas taip:

```python main.py [-c | --class_codes modulis1 modulis2 ...] [-d | --start_dates YYYY-mm-dd YYYY-mm-dd ...]```

Išvestis bus atspausdinama ir konsolėje, ir išvedama kabliataškiais atskirtu formatu faile `<modulio pavadinimas>.csv`. Kiekvienam moduliui bus sugeneruotas atskiras failas.

### Naudojimosi pavyzdys

Iškviečiame įrankį duotam pavyzdiniam duomenų bazių moduliui, kurio pirmas laboratorinis darbas įvyko vasario 3 d.:

```python main.py -c P175B602 -d 2025-02-03```

Gauname tokią išvestį:
```
Parsing 1 classes...
----------------------------------------
Class name: Duomenų bazės
Contains a total of 7 assignments:
Probleminių užduočių sprendimas (15.0%) assigned on 2025-02-03 and due on 2025-03-03
Probleminių užduočių sprendimas (15.0%) assigned on 2025-03-03 and due on 2025-04-28
Laboratorinio darbo gynimas (12.0%) assigned on 2025-02-03 and due on 2025-03-17
Laboratorinio darbo gynimas (9.0%) assigned on 2025-02-03 and due on 2025-04-14
Laboratorinio darbo gynimas (9.0%) assigned on 2025-04-14 and due on 2025-05-12
Studento aktyvumo (lygmens) įvertinimas (10.0%) assigned on 2025-02-03 and due on 2025-05-19
Egzaminas kompiuteriu (30.0%) assigned on 2025-02-03 and due on 2025-05-26
----------------------------------------
```

`duomenų-bazės.csv` atrodo taip:
```
Duomenų bazės;Probleminių užduočių sprendimas;0.15;2025/03/03
Duomenų bazės;Probleminių užduočių sprendimas;0.15;2025/04/28
Duomenų bazės;Laboratorinio darbo gynimas;0.12;2025/03/17
Duomenų bazės;Laboratorinio darbo gynimas;0.09;2025/04/14
Duomenų bazės;Laboratorinio darbo gynimas;0.09;2025/05/12
Duomenų bazės;Studento aktyvumo (lygmens) įvertinimas;0.1;2025/05/19
Duomenų bazės;Egzaminas kompiuteriu;0.3;2025/05/26
```

