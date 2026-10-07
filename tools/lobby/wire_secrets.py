"""Branche les secrets du spawn (secrets/, advancement mg:secrets/*) : python wire_secrets.py <racine du dépôt>. Une seule fois."""
import os, sys

R = sys.argv[1]
F = os.path.join(R, 'data/mg/function')

def patch(rel, old, new):
    path = os.path.join(F, rel + '.mcfunction')
    s = open(path, encoding='utf-8', newline='').read(); nl = '\r\n' if '\r\n' in s else '\n'
    o, n = old.replace('\n', nl), new.replace('\n', nl)
    assert s.count(o) == 1, (rel, old[:60], s.count(o))
    open(path, 'w', encoding='utf-8', newline='').write(s.replace(o, n))

if 'mg.esn' not in open(os.path.join(F, 'core/load.mcfunction'), encoding='utf-8').read():
    patch('core/load', 'scoreboard objectives add mg.lcd dummy\n',
          'scoreboard objectives add mg.lcd dummy\n' + ''.join(f'scoreboard objectives add mg.{o} dummy\n' for o in ('esn', 'esc', 'est', 'eup', 'ebl', 'ept')))
patch('core/void_catch', 'function mg:core/fall_heal\n', 'function mg:core/fall_heal\nadvancement grant @s only mg:secrets/vide\n')
patch('parkour/finish', '# Fin de course\n',
      'advancement grant @s only mg:secrets/sommet\nexecute if score @s mg.ppt matches ..1199 run advancement grant @s only mg:secrets/ecureuil\n# Fin de course\n')
print('ok')
