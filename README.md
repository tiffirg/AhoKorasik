# Достижение покрытия алгоритма AhoKorasik

## Statement Coverage < Decision Coverage:
test_empty_trie, test_no_match - Не покрывают все statements, поэтому сохраняется неравенство 

## Decision Coverage < MC/DC Coverage:
Здесь для нужного равенства должны быть логические условия, Decision Coverage достигается, но не обеспечивается независимое влияние каждой части условия, что требует MC/DC.

Только test_complex_condition покрывает все возможные комбинации
