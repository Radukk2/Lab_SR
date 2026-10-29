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

## 3. Popularea catalogului cu Item-uri (Lab 3)
Popularea catalogului s-a realizat prin parcurgerea fisierului CSV si trimiterea datelor catre Recombee utilizand cereri de tip **Batch** (`Batch` si `SetItemValues`) cu parametrul `cascade_create=True`.

- **Curatarea datelor:** Identificatoarele de tip `itemId` au fost curatate prin inlocuirea caracterelor speciale (cum ar fi `/` sau `\`) pentru a preveni erorile de encodare in calea URL-urilor din API-ul Recombee. De asemenea, a fost adaugata o regula care sa asigure ca anul lansarii este unul valid (exista doar numere in cazul nostru)
- **Optimizare:** Trimiterea item-urilor s-a realizat in batch-uri de cate 100 de elemente per request pentru eficientizarea apelurilor HTTP.