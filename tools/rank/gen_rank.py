"""🏅 Classement général : score et niveau par joueur.

    python tools/rank/gen_rank.py .

Score général (mg.gen) = 10 × parties jouées (mg.stp) + 50 × victoires (mg.wins) + 2 × kills (mg.stk).
Niveau (mg.lvl) : il faut 25 × L × (L + 1) points pour le niveau L (50, 150, 300, 500… : chaque niveau coûte 50 de plus).
- Recalcul toutes les secondes pour les joueurs connectés (rien n'est fait si le score n'a pas bougé).
- Barre d'XP = niveau général + progression vers le suivant, dans le lobby seulement (pas en partie, pas en survie :
  la survie a sa propre XP, sauvegardée par survie/save). Réappliquée au retour au lobby.
- Passage de niveau : message + son ; nouveau meilleur niveau → plaque du hall (hall/top, clé « gen »).
- Tableau à droite : mg.lvl fait partie de la rotation (hall/rot_next), plaque « 🏅 Meilleur niveau général » au hall.
"""
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')


def w(rel, lines):
    p = os.path.join(F, rel + '.mcfunction')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        f.write('\n'.join(lines) + '\n')


def patch(rel, anchor, new, where='after'):
    p = os.path.join(F, rel + '.mcfunction')
    L = open(p, encoding='utf-8').read().split('\n')
    if all(l in L for l in new):
        return
    i = L.index(anchor) + (1 if where == 'after' else 0)
    L[i:i] = new
    open(p, 'w', encoding='utf-8', newline='\n').write('\n'.join(L))


w('rank/tick', ['# Classement général : chaque seconde (core/tick). Généré par tools/rank/gen_rank.py.',
                'scoreboard players set #10 mg.st 10', 'scoreboard players set #50 mg.st 50', 'scoreboard players set #2 mg.st 2',
                'scoreboard players set #25 mg.st 25',
                'execute as @a[tag=mg.init] run function mg:rank/update'])
w('rank/update', ['# @s : score général, niveau, barre d\'XP',
                  'execute unless score @s mg.stp matches -2147483648.. run scoreboard players set @s mg.stp 0',
                  'execute unless score @s mg.wins matches -2147483648.. run scoreboard players set @s mg.wins 0',
                  'execute unless score @s mg.stk matches -2147483648.. run scoreboard players set @s mg.stk 0',
                  'scoreboard players operation $rg mg.st = @s mg.stp', 'scoreboard players operation $rg mg.st *= #10 mg.st',
                  'scoreboard players operation $rw mg.st = @s mg.wins', 'scoreboard players operation $rw mg.st *= #50 mg.st',
                  'scoreboard players operation $rg mg.st += $rw mg.st',
                  'scoreboard players operation $rw mg.st = @s mg.stk', 'scoreboard players operation $rw mg.st *= #2 mg.st',
                  'scoreboard players operation $rg mg.st += $rw mg.st',
                  'scoreboard players operation @s mg.gen = $rg mg.st',
                  'execute unless score @s mg.lvl matches 0.. run scoreboard players set @s mg.lvl 0',
                  # score inchangé et XP déjà posée : rien à faire
                  'execute if score @s mg.gen = @s mg.genc if entity @s[tag=mg.xpok] run return 0',
                  'tag @s remove mg.rkfirst', 'execute unless score @s mg.genc matches -2147483648.. run tag @s add mg.rkfirst',
                  'scoreboard players operation @s mg.genc = @s mg.gen',
                  'scoreboard players operation $rl0 mg.st = @s mg.lvl',
                  'function mg:rank/level_up',
                  'execute if score @s mg.lvl > $rl0 mg.st unless entity @s[tag=mg.rkfirst] run function mg:rank/announce',
                  'execute if entity @s[tag=mg.rkfirst] run function mg:hall/top {obj:"mg.lvl",key:"gen",lbl:"🏅 Meilleur niveau général",col:"aqua",unit:" niv."}',
                  'tag @s remove mg.xpok',
                  'execute unless entity @s[tag=mg.play] unless entity @s[tag=mg.surv] run function mg:rank/xp'])
w('rank/need', ['# $rn = points nécessaires pour le niveau ($rl + 1) = 25 × (L+1) × (L+2)',
                'scoreboard players operation $rn mg.st = @s mg.lvl', 'scoreboard players add $rn mg.st 1',
                'scoreboard players operation $rm mg.st = $rn mg.st', 'scoreboard players add $rm mg.st 1',
                'scoreboard players operation $rn mg.st *= $rm mg.st', 'scoreboard players operation $rn mg.st *= #25 mg.st'])
w('rank/level_up', ['# Monte de niveau tant que le score le permet (récursif ; les stats ne baissent jamais)',
                    'function mg:rank/need',
                    'execute if score @s mg.gen >= $rn mg.st run scoreboard players add @s mg.lvl 1',
                    'execute if score @s mg.gen >= $rn mg.st if score @s mg.lvl matches ..999 run function mg:rank/level_up'])
w('rank/xp', ['# @s (au lobby) : barre d\'XP = niveau général, remplie selon la progression vers le suivant',
              # points du niveau L = 25 L (L+1) ; écart jusqu'au suivant = 50 (L+1)
              'scoreboard players operation $rp mg.st = @s mg.lvl', 'scoreboard players operation $rq mg.st = @s mg.lvl',
              'scoreboard players add $rq mg.st 1', 'scoreboard players operation $rp mg.st *= $rq mg.st',
              'scoreboard players operation $rp mg.st *= #25 mg.st',
              'scoreboard players operation $rd mg.st = @s mg.gen', 'scoreboard players operation $rd mg.st -= $rp mg.st',
              'scoreboard players operation $rq mg.st *= #50 mg.st',
              # capacité de la barre vanilla au niveau L : 2L+7 (L<16), 5L-38 (L<31), 9L-158
              'scoreboard players operation $rc mg.st = @s mg.lvl', 'scoreboard players operation $rc mg.st *= #2 mg.st',
              'scoreboard players add $rc mg.st 7',
              'execute if score @s mg.lvl matches 16..30 run scoreboard players operation $rc mg.st = @s mg.lvl',
              'scoreboard players set #5 mg.st 5', 'scoreboard players set #9 mg.st 9',
              'execute if score @s mg.lvl matches 16..30 run scoreboard players operation $rc mg.st *= #5 mg.st',
              'execute if score @s mg.lvl matches 16..30 run scoreboard players remove $rc mg.st 38',
              'execute if score @s mg.lvl matches 31.. run scoreboard players operation $rc mg.st = @s mg.lvl',
              'execute if score @s mg.lvl matches 31.. run scoreboard players operation $rc mg.st *= #9 mg.st',
              'execute if score @s mg.lvl matches 31.. run scoreboard players remove $rc mg.st 158',
              'scoreboard players operation $rd mg.st *= $rc mg.st', 'scoreboard players operation $rd mg.st /= $rq mg.st',
              'execute if score $rd mg.st >= $rc mg.st run scoreboard players operation $rd mg.st = $rc mg.st',
              'execute if score $rd mg.st >= $rc mg.st run scoreboard players remove $rd mg.st 1',
              'execute store result storage mg:rank x.l int 1 run scoreboard players get @s mg.lvl',
              'execute store result storage mg:rank x.p int 1 run scoreboard players get $rd mg.st',
              'function mg:rank/xp_set with storage mg:rank x', 'tag @s add mg.xpok'])
w('rank/xp_set', ['$xp set @s $(l) levels', '$xp set @s $(p) points'])
w('rank/announce', ['# @s a gagné au moins un niveau général',
                    'tellraw @s [{"text":"🏅 Niveau général ","color":"aqua","bold":true},{"score":{"name":"@s","objective":"mg.lvl"},"color":"yellow","bold":true},{"text":" !","color":"aqua","bold":true},{"text":"  (score ","color":"gray","bold":false},{"score":{"name":"@s","objective":"mg.gen"},"color":"gray"},{"text":")","color":"gray"}]',
                    'execute at @s run playsound minecraft:entity.player.levelup master @s ~ ~ ~ 0.8 1.2',
                    'execute if score @s mg.lvl matches 5.. run tellraw @a[tag=!mg.surv] [{"text":"🏅 ","color":"aqua"},{"selector":"@s","color":"yellow"},{"text":" passe niveau général ","color":"gray"},{"score":{"name":"@s","objective":"mg.lvl"},"color":"aqua","bold":true}]',
                    'function mg:hall/top {obj:"mg.lvl",key:"gen",lbl:"🏅 Meilleur niveau général",col:"aqua",unit:" niv."}'])

# câblage
patch('core/tick', 'execute if score $setup mg.st matches 1 if score $lan mg.t matches 10 unless block 24 63 19 minecraft:gold_block run function mg:lobby/food_build',
      ['execute if score $lan mg.t matches 15 run function mg:rank/tick'])
patch('core/return_lobby', 'execute as @a[tag=mg.win] run function mg:hall/credit', ['tag @a remove mg.xpok'])
p = os.path.join(F, 'survie/leave.mcfunction')
if 'tag @s remove mg.xpok' not in open(p, encoding='utf-8').read():
    with open(p, 'a', encoding='utf-8', newline='\n') as f:
        f.write('\ntag @s remove mg.xpok\n')
patch('core/load', 'scoreboard objectives add mg.bw trigger', ['scoreboard players set #1 mg.st 1'])
print('Classement général OK')
