# Welder's Authorization

- We need to check if the expiry date of a welder's authorization is expiring 3 months from the current month.
- We need to contact the companies to inform them about the expiry
- The welders should be aggregated by company in the output
- If the authorization expired, ignore the welders

## Note:

Din lectia 12 s-au folosit:
- f-string in :
    - main.py
    - date_utils.py in functia read_date
- underscore in:
  - input_welder in functia read_welders

## Task-uri

### Tema 7

- Crearea unui nou Repository in GitHub pentru proiect și preluarea în Local 0.5p 
- Structurarea proiectului în pachete, module, fișiere auxiliare 1p
- Folosirea a cel puțin 2 dintre tipurile de date: integer, float, string, boolean 2p
- Folosirea a cel puțin 2 dintre structurile: IF, WHILE, FOR 2p
- Folosirea a cel puțin 2 dintre structurile de date: listă, tuplu și dicționar 2p
- Scrierea unui docstring și a unui comentariu 2p
- Add, commit, push către GitHub 0.5p 

### Tema 8

- Aplicarea a cel puțin 2 dintre cele 6 concepte prezentate la lecția 12, pe proiectul individual.
- Pentru validare, se vor specifica cele 2 concepe alese și se va trimite fie link cu GitHub Repository al proiectului, fie zip cu fișierele de cod

### Tema 9
- Introducerea unei excepții standard și a unei excepții proprii acolo unde există vulnerabilități în cod. (10p)
  - in utils/date_utils.py  este implementata InvalidDateException
  - in utils/date_utils.py in functia transform_date, ValueError si InvalidDateException sunt folosite
- Scrierea a 2 teste folosind pytest (10p)
  - Testarea unei date valide
  - Testarea diferentei dintre doua date
- Pentru validare, se vor specifica excepțiile folosite și se va trimite fie link cu GitHub Repository al proiectului, fie zip cu fișierele de cod

### Tema 10.

- Folosirea fișierelor în proiect - se va implementa la alegere o operațiune specifică fișierelor. E.g.: citirea ofertei de produse din fișier, salvarea dobânzii calculate în fișier etc.
- In utils/input_welder.py am implementat read_welders_from_file, care citeste din fisierul valabilitate autorizatii.csv urmatoarele: numele si prenumele sudorului; denumirea firmei si data expirarii autorizatiei.

### Tema 12

- In folderul input_welder.py s-a definit clasa Welder, pentru a gestiona si accesa mai usor informatiile fiecarui sudor
- Aceasta este folosita in:
  - functia read_welders_from_file
  - modulul main.py