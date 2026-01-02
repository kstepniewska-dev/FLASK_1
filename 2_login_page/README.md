### Register / Login ###

1. Stwórz stronę www z widokami
   - ```/``` – Strona główna (lista użytkowników)
   - ```/register``` – Rejestracja
   - ```/login``` – Logowanie
   - ```/dashboard```
2. Stwórz formularz logowania i rejestracji, po zarejestrowaniu użytkownika dopisz jego dane do słownika
```python 
users = {
    "alice": { "name" : "Alice", "pass": "alice123"},
    "dave": { "name" : "Dave", "pass": "dave123"},
    "eve": { "name" : "Eve", "pass": "eve123"}
}
```
* Na razie nie zapisujemy użytkownika do bazy danych więc zniknie po zrestatowaniu serwera

- [x] Zrobione