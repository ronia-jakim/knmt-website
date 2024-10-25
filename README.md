# knmt-website
Website for academic club of mathematicians at University of Wrocław

# instrukcja obsługi

**dependencies:** 

- sass

- python packages: jinja2, python-frontmatter, markdown

## zarządzanie wpisami

Wszystkie wpisypojawiające się na stronie Aktualności są przechowywane w folderze `content/news` jako folder z głównym plikiem `*.md` zawierającym informacje takie jak

- tytuł posta
- autor (dotyczy referatu)
- data (format `YYYY.MM.DD`)
- godzina (dotyczy referatów, format `HH:MM`)
- obrazek poglądowy (jeśli nie jest dołączony, to użyty jest domyślny plik w `assets/img/post_preview.jpg`

Wszystkie zdjęcia, które mają być zawarte w poście muszą być w folderze posta, a ścieżki w pliku `*.md` mają być względem tegoż foldera.

```yaml
---
    title: 'tytuł posta/referatu'
    author: 'autor referatu'
    date: 'data wpisu lub data referatu w formacie YYYY.MM.DD'
    time: 'godzina referatu w formacie HH:MM'
    preview_image: 'ścieżka do pliku pokazującego się na stronie głównej względem folderu w którym się znajdujemy'
    description: 'opis posta, który pokazuje się na stronie głównej, jeśli pozostawione pustym użyte zostanie pierwsze 100 znaków głównego tekstu posta'
---

Główna treść posta, pisana jak w markdownie możliwe jest użycie latexa, powinna pojawić się tylko w tym miejscu.

```
