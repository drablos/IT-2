## Penger tjent per sang

### Pseudokode i "naturlig språk"
```pseudo
Hent inn land fra bruker (input)
Hvis land er lik Norge:
    Print $0.44 per sang
Ellers hvis land er lik Sverige:
    Print $0.34 per sang
Ellers:
    Print $0.22 per sang
```
### Pseudokode som følger UDIRs standard
```pseudo
SET land TO READ "Hvilket land er du fra?"
IF land EQUAL TO Norge
    THEN DISPLAY "$0.44 per sang"
ELSE IF land EQUAL TO "Sverige"
    THEN DISPLAY "$0.34 per sang"
ELSE
    THEN DISPLAY "$0.22 per sang"
ENDIF
```
### Python-kode
```python
land = input("Hvilket land er du fra?")
if land.lower() == "Norge":
    print("$0.44 per sang")
elif land.lower() == "Sverige":
    print("$0.34 per sang")
else:
    print("$0.22 per sang")
```
## Andel penger tjent per sang

### Pseudokode i "naturlig språk"
```pseudo
Hent inn antall streams fra bruker (input)
Hvis antall streams er større enn 30 000 000
    Print "Penger tjent per sang lik 70%"
Ellers hvis antall streams er større enn 1 400 000
    Print "Penger tjent per sang lik 40%"
Ellers
    Print "Penger tjent per sang lik 0%"
```
### Pseudokode som følger UDIRs standard
```pseudo
SET antall_streams TO READ "Hvor mange streams har du?"
IF antall_streams GREATER THAN 30 000 000
    THEN DISPLAY "Penger tjent per sang lik 70%"
ELSE IF antall_streams GREATER THAN 1 400 000
    THEN DISPLAY "Penger tjent per sang lik 40%"
ELSE
    THEN DISPLAY "Penger tjent per sang lik 0%"
ENDIF
```
### Python-kode
```python
antall_streams = input("Hva er dine antall streams?")
if antall_streams > 30000000:
    print("Penger tjent per sang lik 70%")
elif antall_streams > 1400000:
    print("Penger tjent per sang lik 40%")
else:
    print("Penger tjent per sang lik 0%")
```


