"""Mob Arena : nombre de monstres selon le nombre de joueurs (équilibré pour 4 ; +25 % par joueur au-delà).

    python tools/mobarena/scale_waves.py .        (depuis la racine du dépôt ; idempotent)

Les fichiers de vague (mobarena/<thème>/w<N>) peuvent être rejoués en « mode doublon » ($wdup = 1) :
seuls les monstres ordinaires sont invoqués à nouveau ; messages, titres, sons et boss sont ignorés.
mobarena/scale rejoue la vague autant que nécessaire (passes complètes + passe partielle tirée au sort).
"""
import os
import re
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function/mobarena')
GUARD = 'execute unless score $wdup mg.st matches 1 run '
n = 0
for d in sorted(os.listdir(F)):
    p = os.path.join(F, d)
    if not os.path.isdir(p):
        continue
    for f in sorted(os.listdir(p)):
        if not re.fullmatch(r'w\d+\.mcfunction', f):
            continue
        fp = os.path.join(p, f)
        out = []
        for line in open(fp, encoding='utf-8').read().split('\n'):
            s = line.strip()
            skip = (s.startswith(('tellraw', 'title', 'function', 'playsound'))
                    or ('playsound' in s and s.startswith('execute'))
                    or 'boss' in s)
            if skip and not s.startswith(GUARD) and not s.startswith('#'):
                line = GUARD + line
                n += 1
            out.append(line)
        with open(fp, 'w', encoding='utf-8', newline='\n') as fo:
            fo.write('\n'.join(out))


def w(name, lines):
    with open(os.path.join(F, name + '.mcfunction'), 'w', encoding='utf-8', newline='\n') as fo:
        fo.write('\n'.join(lines) + '\n')


w('scale', [
    '# Mob Arena — plus de monstres au-delà de 4 joueurs (+25 % par joueur), appelé juste après la vague de base',
    'execute store result score $mnp mg.st if entity @a[tag=mg.play]',
    'scoreboard players operation $mex mg.st = $mnp mg.st',
    'scoreboard players remove $mex mg.st 4',
    'execute if score $mex mg.st matches ..0 run return 0',
    'execute store result score $mb0 mg.st if entity @e[tag=mg.mob]',
    'scoreboard players set $wdup mg.st 1',
    'function mg:mobarena/scale_pass',
    'execute if score $mex mg.st matches 1..3 run function mg:mobarena/scale_part',
    'scoreboard players set $wdup mg.st 0',
    'tag @e remove mg.mb0',
    'execute store result score $mb1 mg.st if entity @e[tag=mg.mob]',
    'tellraw @a [{"text":"  ➜ ","color":"gray"},{"score":{"name":"$mnp","objective":"mg.st"},"color":"gold"},{"text":" joueurs : ","color":"gray"},'
    '{"score":{"name":"$mb1","objective":"mg.st"},"color":"red"},{"text":" monstres au lieu de ","color":"gray"},{"score":{"name":"$mb0","objective":"mg.st"},"color":"yellow"}]'])
w('scale_pass', [
    '# Passes complètes : la vague est rejouée une fois par tranche de 4 joueurs en plus (récursif, 5 passes max = 24 joueurs)',
    'execute unless score $mex mg.st matches 4.. run return 0',
    'function mg:mobarena/wave with storage mg:mw',
    'scoreboard players remove $mex mg.st 4',
    'function mg:mobarena/scale_pass'])
w('scale_part', [
    '# Passe partielle : la vague est rejouée, on ne garde que $mex quarts des nouveaux monstres (tirés au sort)',
    'tag @e[tag=mg.mob] add mg.mb0',
    'function mg:mobarena/wave with storage mg:mw',
    'execute store result score $mnc mg.st if entity @e[tag=mg.mob,tag=!mg.mb0]',
    '# à retirer = nouveaux − nouveaux × $mex / 4',
    'scoreboard players operation $mnk mg.st = $mnc mg.st',
    'scoreboard players operation $mnk mg.st *= $mex mg.st',
    'scoreboard players set #4 mg.st 4',
    'scoreboard players operation $mnk mg.st /= #4 mg.st',
    'scoreboard players operation $mnc mg.st -= $mnk mg.st',
    'function mg:mobarena/scale_cull'])
w('scale_cull', [
    '# Retire un monstre en trop au hasard (sans butin), $mnc fois',
    'execute unless score $mnc mg.st matches 1.. run return 0',
    'tp @e[tag=mg.mob,tag=!mg.mb0,sort=random,limit=1] ~ -100 ~',
    'kill @e[tag=mg.mob,tag=!mg.mb0,sort=random,limit=1,y=-200,dy=150]',
    'scoreboard players remove $mnc mg.st 1',
    'function mg:mobarena/scale_cull'])
# crochet dans next_wave
p = os.path.join(F, 'next_wave.mcfunction')
t = open(p, encoding='utf-8').read()
hook = 'function mg:mobarena/wave with storage mg:mw\nfunction mg:mobarena/scale\n'
if 'function mg:mobarena/scale\n' not in t:
    assert t.count('function mg:mobarena/wave with storage mg:mw\n') == 1
    t = t.replace('function mg:mobarena/wave with storage mg:mw\n', hook)
    with open(p, 'w', encoding='utf-8', newline='\n') as fo:
        fo.write(t)
print(f'{n} lignes protégées')
