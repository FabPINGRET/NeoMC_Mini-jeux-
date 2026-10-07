"""Le compte à rebours du kart attend que tous les pilotes aient choisi leur kart (1 minute au plus) : python wire_kart4.py <racine>. Une seule fois."""
import os, sys
F = os.path.join(sys.argv[1], 'data/mg/function')
p = os.path.join(F, 'core/countdown.mcfunction')
s = open(p, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
a = '# Compte à rebours (chaque tick, état 1)' + nl
assert s.count(a) == 1
s = s.replace(a, a + '# Kart : retenu tant que les pilotes choisissent leur kart' + nl +
              'execute if score $game mg.st matches 61 if function mg:kart/hold run return 0' + nl)
open(p, 'w', encoding='utf-8', newline='').write(s)
print('ok')
