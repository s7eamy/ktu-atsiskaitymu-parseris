# KTU atsiskaitymų parseris

Įrankis iš KTU suteikiamų studijų modulio kortelių geba ištraukti modulio pavadinimą, atsiskaitymus, jų galutinio pažymio dalis ir atsiskaitymo dieną, kuomet nurodama užsiėmimų diena.

### Instaliacijos instrukcijos

Parsisiųsk šitą repozitoriją į norimą direktoriją, pavyzdžiui, su komanda `git clone https://github.com/s7eamy/ktu-atsiskaitymu-parseris.git`

Toje direktorijoje susikurk Python virtualią aplinką:
`python -m venv .venv`

Aktyvuok virtualią aplinką:
`source .venv/bin/activate` (Linux)
`./.venv/Scripts/activate` (Windows)

Parsisiųsk reikiamą biblioteką:
`pip install beautifulsoup4`

### Naudojimosi instrukcijos

Įrankis iškviečiamas taip:
`python main.py <modulio kortelės html> <pirmojo modulio praktinio užsiėmimo data`

Išvestis bus atspausdinama ir konsolėje, ir išvedama kabliataškiais atskirtu formatu faile `assignments.csv`

### Naudojimosi pavyzdys

Iškviečiame įrankį duotam pavyzdiniam duomenų bazių moduliui, kurio pirmas laboratorinis darbas įvyko vasario 3 d.:
`python main.py 2025p/duombazes.html 2025-02-03`

Gauname tokią išvestį:
```
Class name: Duomen� baz�s
Contains a total of 7 assignments:
Problemini� u�duo�i� sprendimas (15.0%) assigned on 2025-02-03 and due on 2025-03-03
Problemini� u�duo�i� sprendimas (15.0%) assigned on 2025-03-03 and due on 2025-04-28
Laboratorinio darbo gynimas (12.0%) assigned on 2025-02-03 and due on 2025-03-17
Laboratorinio darbo gynimas (9.0%) assigned on 2025-02-03 and due on 2025-04-14
Laboratorinio darbo gynimas (9.0%) assigned on 2025-04-14 and due on 2025-05-12
Studento aktyvumo (lygmens) �vertinimas (10.0%) assigned on 2025-02-03 and due on 2025-05-19
Egzaminas kompiuteriu (30.0%) assigned on 2025-02-03 and due on 2025-05-26
```

`assignments.csv` atrodo taip:
```
Duomen� baz�s;Problemini� u�duo�i� sprendimas;0.15;2025/03/03
Duomen� baz�s;Problemini� u�duo�i� sprendimas;0.15;2025/04/28
Duomen� baz�s;Laboratorinio darbo gynimas;0.12;2025/03/17
Duomen� baz�s;Laboratorinio darbo gynimas;0.09;2025/04/14
Duomen� baz�s;Laboratorinio darbo gynimas;0.09;2025/05/12
Duomen� baz�s;Studento aktyvumo (lygmens) �vertinimas;0.1;2025/05/19
Duomen� baz�s;Egzaminas kompiuteriu;0.3;2025/05/26
```

