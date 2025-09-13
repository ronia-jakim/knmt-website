# knmt-website
Website for academic club of mathematicians at University of Wrocław

# instrukcja obsługi

**dependencies:** 

- python packages: jinja2, python-frontmatter, markdown
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

## dodawanie podstrony

Żeby dodać podstronę można skopiować istniejący folder z odpowiedniego folderu `subpages` (w `base` albo `wss`) i edytować jego plik `index.html` oraz `src/main.py`. Następnie należy dodać informacje o podstronie do pliku `subpages/list.md` zgodnie z poniższym schematem

```
subpages:
    - { name: 'nazwa nowej podstrony wyświetlana na pasku nawigacji', 
        url: 'ścieżka do nowej podstrony musi zgadzać się z nazwą foldera tworzonego przez build.sh',
        special: true/false nieobowiązkowe pole pozwalające wyróżnić zakładkę na pasku nawigacji
        }
```

