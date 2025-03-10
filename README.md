# Алгоритм с Statement Coverage < Decision Coverage < MC/DC Coverage

```
def func(a, b, c):
    if (a or b) and c:  # Сложное условие с двумя операторами
        return "Acc"
    else:
        return "Rej"
```

## Statement Coverage:
Минимальный набор тестов для прохода по всем операторам
```(True, False, True)   # Выполнится "Accepted"```

## Decision Coverage:
Минимальный набор для прохода по всем исходам
```
(True, False, True)    # `if` выполняется - "Accepted"
(False, False, False)  # `if` НЕ выполняется - "Rejected"
```

##  MC/DC Coverage:
Здесь для нужного равенства должны быть логические условия, Decision Coverage достигается, но не обеспечивается независимое влияние каждой части условия, что требует MC/DC.
```
(True, False, True)    #  a=True влияет на результат
(False, True, True)    #  b=True влияет на результат
(False, False, True)   #  (a or b)=False, но c=True, значит влияет
(False, False, False)  #  c=False` влияет
```
