"""Objectif de la roulette d'objet du kart (mg.krl) : python wire_kart5.py <racine>. Une seule fois."""
import os, sys
F = os.path.join(sys.argv[1], 'data/mg/function')
for rel, old, new in (('core/load', 'scoreboard objectives add mg.kch trigger\n', 'scoreboard objectives add mg.kch trigger\nscoreboard objectives add mg.krl dummy\n'),
                      ('desinstaller', 'scoreboard objectives remove mg.kch\n', 'scoreboard objectives remove mg.kch\nscoreboard objectives remove mg.krl\n')):
    p = os.path.join(F, rel + '.mcfunction')
    s = open(p, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    assert s.count(o) == 1, rel
    open(p, 'w', encoding='utf-8', newline='').write(s.replace(o, n))
print('ok')
