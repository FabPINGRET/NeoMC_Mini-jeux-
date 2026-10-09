"""Fin de /function mg:setup : un message quand TOUTE la génération (y compris les constructions différées) est terminée.

    python tools/setup/gen_setup_watch.py .

mg:core/setup_build lance des constructions asynchrones (spawn en 11 tranches, kart, Mini Party, Élytra, course d'élytres,
Dropper aventure, buffet, hall, montagne russe…). Chacune pose un drapeau en storage à la fin : on les efface au début,
puis mg:core/setup_watch vérifie toutes les 2 s, affiche l'avancement toutes les 20 s et annonce la fin (ou, après 15 min,
ce qui manque).
"""
import json
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')


def js(o):
    return json.dumps(o, ensure_ascii=False, separators=(',', ':'))


def w(rel, lines):
    with open(os.path.join(F, rel + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def patch(rel, anchor, new, where='after'):
    p = os.path.join(F, rel + '.mcfunction')
    L = open(p, encoding='utf-8').read().split('\n')
    if all(l in L for l in new):
        return
    i = L.index(anchor) + (1 if where == 'after' else 0)
    L[i:i] = new
    open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))


# (libellé, [(storage, chemin)])
JOBS = [('Spawn', [('mg:lobby', 'v6')]), ('Buffet', [('mg:lobby', 'food1')]), ('Élytres du spawn', [('mg:lobby', 'ely1')]),
        ('Hall des scores', [('mg:hall', 'v8')]), ('Montagne russe', [('mg:lobby', 'coaster2')]), ('Plots', [('mg:setup', 'plot')]),
        ('Mini Party', [('mg:party', 'built')]), ('Kart', [('mg:kart', 'built'), ('mg:kart', 'built2'), ('mg:kart', 'built3')]),
        ('Dropper aventure', [('mg:dropadv', 'v3')]), ('Élytra', [('mg:sky', 'built')]),
        # drapeaux = FLAG de chaque tools/elyrace/course_*.py (gen_elyrace.py --check echoue s'ils divergent)
        ('Course d\'élytres', [('mg:elyrace', 'v2'), ('mg:elyrace', 'c2v2')])]
N = len(JOBS)

W = ['# Surveille la fin de la génération lancée par mg:setup (toutes les 2 s). Généré par tools/setup/gen_setup_watch.py.',
     'scoreboard players add $swt mg.st 1', 'scoreboard players set $swn mg.st 0']
for i, (lab, flags) in enumerate(JOBS):
    cond = ' '.join(f'if data storage {s} {k}' for s, k in flags)
    W.append(f'execute {cond} run scoreboard players add $swn mg.st 1')
W += [f'execute if score $swn mg.st matches {N}.. run return run function mg:core/setup_done',
      '# toutes les 20 s : avancement',
      'scoreboard players operation $swq mg.st = $swt mg.st', 'scoreboard players set #10 mg.st 10',
      'scoreboard players operation $swq mg.st %= #10 mg.st',
      'execute if score $swq mg.st matches 0 run function mg:core/setup_progress',
      '# 15 min sans tout terminer : on arrête de surveiller et on dit ce qui manque',
      'execute if score $swt mg.st matches 450.. run return run function mg:core/setup_timeout',
      'schedule function mg:core/setup_watch 2s']
w('core/setup_watch', W)
P = ['# Avancement de la génération (admins)',
     'tellraw @a[tag=mg.admin] ' + js([{'text': '[Mini-Jeux] ', 'color': 'gold'}, {'text': 'Génération en cours : ', 'color': 'gray'},
                                       {'score': {'name': '$swn', 'objective': 'mg.st'}, 'color': 'yellow', 'bold': True},
                                       {'text': f' / {N} — reste :', 'color': 'gray'}])]
for lab, flags in JOBS:
    cond = ' '.join(f'if data storage {s} {k}' for s, k in flags)
    P.append(f'execute unless function mg:core/setup_ok_{JOBS.index((lab, flags))} run tellraw @a[tag=mg.admin] ' + js([{'text': '   • ' + lab, 'color': 'yellow'}]))
w('core/setup_progress', P)
for i, (lab, flags) in enumerate(JOBS):
    w(f'core/setup_ok_{i}', [f'# {lab} terminé ?', 'return run execute ' + ' '.join(f'if data storage {s} {k}' for s, k in flags)])
w('core/setup_done', ['# Toute la génération est terminée',
                      'tellraw @a ' + js([{'text': '[Mini-Jeux] ', 'color': 'gold'}, {'text': '✔ Génération terminée ', 'color': 'green', 'bold': True},
                                          {'text': '(spawn, arènes, circuits, parcours, hall…). Le serveur est prêt !', 'color': 'gray'}]),
                      'title @a[tag=mg.admin] title {"text":"✔ Génération terminée","color":"green","bold":true}',
                      'title @a[tag=mg.admin] subtitle {"text":"le serveur est prêt","color":"gray"}',
                      'execute as @a at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
w('core/setup_timeout', ['# 15 min : la génération n\'a pas tout terminé',
                         'tellraw @a[tag=mg.admin] ' + js([{'text': '[Mini-Jeux] ', 'color': 'gold'},
                                                           {'text': '⚠ Génération pas terminée après 15 min (souvent : une partie en cours bloque la course d\'élytres). Reste :', 'color': 'red'}]),
                         'function mg:core/setup_progress'])

# câblage dans setup_build : effacer les drapeaux, construire aussi hall et montagne russe, surveiller
CLEAR = [f'data remove storage {s} {k}' for lab, flags in JOBS for s, k in flags if (s, k) not in (('mg:dropadv', 'v3'),)]
_p = os.path.join(F, 'core/setup_build.mcfunction')
_L = open(_p, encoding='utf-8').read().split('\n')
_cut = _L.index('function mg:lobby/build')
_head = [l for l in _L[:_cut] if not (l.startswith('# Drapeaux de fin') or (l.startswith('data remove storage ') and l != 'data remove storage mg:kart built2'))]
open(_p, 'w', encoding='utf-8', newline='\n').write('\n'.join(_head + _L[_cut:]))
patch('core/setup_build', 'function mg:lobby/build', ['# Drapeaux de fin de chaque construction : effacés ici, reposés à la fin de chacune (suivi : core/setup_watch)'] +
      [c for c in CLEAR if c not in ('data remove storage mg:kart built2', 'data remove storage mg:kart built3')], where='before')
patch('core/setup_build', 'schedule function mg:sky/build 40s', ['schedule function mg:hall/build 25s', 'schedule function mg:coaster/build_start 50s'])
patch('core/setup_build', 'scoreboard players set $setup mg.st 1', ['scoreboard players set $swt mg.st 0', 'schedule function mg:core/setup_watch 5s'])
# plots : pas de drapeau de fin → on en pose un
p = os.path.join(F, 'plot/build_all.mcfunction')
t = open(p, encoding='utf-8').read()
if 'storage mg:setup plot' not in t:
    open(p, 'w', encoding='utf-8', newline='\n').write(t.rstrip('\n') + '\ndata modify storage mg:setup plot set value 1b\n')
# message « Installation terminée » trompeur : les constructions continuent
p = os.path.join(F, 'core/setup_build.mcfunction')
t = open(p, encoding='utf-8').read()
t = t.replace('{"text":"Installation terminée !","color":"green"}',
              '{"text":"Installation lancée : génération du spawn et des arènes en cours (quelques minutes). Un message annoncera la fin.","color":"yellow"}')
open(p, 'w', encoding='utf-8', newline='\n').write(t)
patch('desinstaller', 'scoreboard objectives remove mg.bw', ['schedule clear mg:core/setup_watch', 'data remove storage mg:setup plot'])
print('setup_watch OK :', N, 'constructions suivies')
