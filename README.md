# knmt-website
Website for academic club of mathematicians at University of Wrocław

# instrukcja obsługi

**dependencies:** 

- python packages: [jinja2](https://jinja.palletsprojects.com/en/stable/), python-frontmatter, markdown
- caddy for local testing

## zarządzanie informacjami ze strony

Zawartość strony znajduje się w osobnym repozytorium [knmt-website-content](https://github.com/ronia-jakim/knmt-website-content). Po instrukcje jak dodać post/zmodyfikować informacje umieszczone na stronie należy odnieść się do README w tamtym repozytorium.

## struktura strony

```
|- knmt-website 
   |- build.sh          # a script to build it all
   |- local_server.sh   # run in the background to see 
   |                    # results at http://localhost:8080/
   |- Caddyfile         # local server configuration
   |- requirements.txt  # python libraries
   |- assets
      |- fonts
      |- img
      |- stylesheets
   |- base
      |- base.html      # jinja2 template for all knmt 
      |                 # subpages
      |- index.html     # jinja2 template for the main page
      |- post.html      # jinja2 template for post subpages
      |- build.sh       # script that builds all of base website
      |- src            # stores all python scripts used 
      |                 # to build the main knmt website
         |- main.py     # the main build script for the 
         |              # knmt website
         |- other python scripts
      |- subpages
         |- list.md     # a file containing the list of 
         |              # all subpages and how they should 
         |              # appear in the navigation menu 
         |- books
            |- build.sh # MUST HAVE a script to build the subpage
            |- index.html
            |- src
               |- main.py
         |- other subpage folders
   |- wss               # Wrocławskie Spotkania Szkockie
   |                    # analogous structure to base/
      |- src
      |- subpages
      |- base.html
      |- index.html
      |- build.sh
   |- content           # see knmt-content repo linked above
```

Główna strona knmt znajduje się w folderze `base`, który jest rozpisany wyżej. Analogicznie wygląda strona Wrocławskich Spotkań Szkockich, która znajduje się w folderze `wss`.

Każda strona i podstrona musi mieć swój plik `build.sh`, który jest wołany z `build.sh` znajdującego się poziom wyżej. Np. `base/subpages/books/build.sh` jest wołany z `base/build.sh`. Dlatego konieczne jest, aby każda podstrona posiadała własny skrypt budujący.

## przed rozpoczęciem pracy

Świeżo zklonowane repozytorium nie ma dobrze zainicjowanego podmodułu `content`. Aby to naprawić należy wejść do folderu z repo i wykonać polecenie
```bash
git submodule update --init --recursive
```
Po tym poleceniu repozytorium `content` będzie w stanie detached. Musimy więc tam wejść i przeskoczyć na branch main
```bash
cd content
git checkout main
```
Commity i pulle repozytorium `content` domyślnie są niezależne od repozytorium `knmt-website`. Aby więc zaktualizować zawartość `content/` należy do niego wejść i wykonać proste `git pull`.

## testowanie

Jeśli chcesz pracować nad stroną na Windowsie - wyjdź.

Stronę lokalnie można budować korzystając ze skryptu `build.sh` uruchomionego z roota projektu.

W repozytorium znajduje się gotowa konfiguracja serwera Caddy. Aby go uruchomić wystarczy uruchomić skrypt `local_server.sh`, strona pojawi się na [`localhost:8080`](http://localhost:8080/).

## dodawanie podstrony

### base

Dobrym punktem wyjścia jest skopiowanie folderu `base/subpages/template/` do `base/subpages/TWOJA_PODSTRONA`. W następnym kroku należy poinformować projekt, że chcemy mieć nową podstronę wyświetloną na pasku zakładek. Aby to osiągnąć wystarczy dodać informacje o podstronie do pliku `subpages/list.md` zgodnie z poniższym schematem

```
subpages:
    - { name: 'NAZWA', url: '/URL/', special: true/false }
```
- `NAZWA` to nazwa podstrony wyświetlana na pasku nawigacji
- `URL` to nazwa folderu podstrony, czyli np. podstrona zawarta w folderze `books` powinna mieć `url: "/books/"`; ilość / jest bardzo ważna
- `special` to wartość boolowska mówiąca, czy podstrona ma być wyróżniona na pasku nawigacji, czy ma wyglądać jak wszystkie pozostałe.

Wytłumaczmy co zawiera każdy z plików zawartych w folderze `template`

#### `index.html`

Plik zawierający strukturę strony. Jest pisany według schematu Jinja2 (czyli HTML z brokatem). Przejdźmy szybko po najbardziej przydatnych elementach:

- **zmienne**: zmienną w jinja definiujemy w podwójnych nawiasach klamrowych, np: `{{ moja_zmienna }}`; możemy również przekazać do templatki słownik, np. `samochod = { kolor: 'czerwony', ilosc_drzwi: 3 }`, wtedy jeśli chcemy w pewnym miejsciu wyświetlić kolor samochodu piszemy `{{ samochod.kolor }}`, albo zwykłą listę (o tym niżej)
- **zdania warunkowe**: są to bloki, które zaczynają się `{% if warunek %}` i kończą `{% endif %}`, poniżej przykład nieco bardziej skomplikowanego zdania warunkowego:
```
{% if warunek1 %}
    <b> warunek 1</b>
{% elif warunek2 %}
    <i> warunek 2</i>
{% else %}
    <u> ani warunek 1 ani warunek 2</u>
{% endif %}
```
- **pętla for**: przy przekazaniu listy może okazać się użyteczna; tak jak zdania warunkowe pętle są blokami, syntaks podobny do Pythonowego:
```
{% for i in list %}
    element z listy: <b>i</b>
{% endfor %}
```

#### `build.sh`

Skrypt odpalający budowanie podstrony. Należy w nim zmienić każde wystąpienie `TEMPLATE` na nazwę folderu podstrony.

#### `src/main.py`

Plik `main.py` to główny plik odpowiadający za budowanie podstrony. Można oczywiście tworzyć dodatkowe pliki w folderze `src`, które będą wołane z `main.py`.

W podstawowej wersji należy zmienić w `main.py` wszystkie wystąpienia `TEMPLATE` na nazwę folderu podstrony oraz odpowiednio uzupełnić przekazywanie zmiennaych do templatki w `html_cnt = template.render(..., subpages=subpages)`. Nie należy usuwać przekazywania zmiennej `subpages` - ona odpowiada za poprawne wyświetlanie paska nawigacji.


