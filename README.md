# Laborator 2

## 1. Descrierea setului de date
Setul de date ales contine lista filmelor din **IMDb Top 1000** si include informatii despre filme apreciate la nivel global (titlu, anul lansarii, gen, rating, regizor, distributie si detalii financiare).

## 2. Proprietatile inregistrate in catalog
Avem coloana `Series_Title` (sau indexul unic al filmului) este utilizata ca identificator nativ (`itemId`).

Proprietatile definite si transmise prin intermediul API-ului Recombee sunt:
- `genre` de tipul **string** -> genul filmului (Drama, Comedie, etc)
- `released_year`de tipul **int** -> anul in care a fost lansat filmul
- `imdb_rating` de tipul **double** -> nota acordata de utilizatorii IMDb (ex.: 9.3, 8.5)
- `director`  de tipul **string** -> numele regizorului filmului