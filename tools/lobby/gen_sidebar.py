"""📊 Tableau de droite automatique (hors mini-jeu) — sb/auto, chaque seconde (core/tick, $lan mg.t = 5).

    python tools/lobby/gen_sidebar.py .        (idempotent)

- Mini-jeu en cours ($state ≠ 0) : on ne touche à rien, chaque jeu affiche son tableau.
- Sinon, là où il y a le plus de joueurs connectés (égalité : le spawn l'emporte) :
    spawn (ni survie, ni GTA, ni Terra Nova) → tableaux généraux qui tournent (hall/board_tick, votes compris) ;
    Neo GTA (tag mg.gtw)                    → 💵 Dollars (mg.gta) ;
    Terra Nova (tag mg.tvw)                 → ₵ Terra Nova (mg.tvc) ;
    Survie (mg.surv sans mg.gtw / mg.tvw / mg.olw / mg.fnw) → ⛏ Survie — niveau (mg.svl, niveau d'XP recopié chaque seconde).
    Filon (tag mg.fnw)                      → ⛏ Filon — saison (mg.fns, points gagnés à la vente).
  Ombrelune (mg.olw) : pas de tableau propre, ses joueurs ne comptent dans aucun des quatre (ils ne faussent plus le niveau de survie).
- $sbm = affichage en cours (−1 inconnu, 0 spawn, 1 GTA, 2 Terra Nova, 3 survie, 4 Filon, 9 masqué).
- Menu « Classement à droite » (core/opt_sidebar) : $sbo = 1 masque le tableau hors mini-jeu, 0 (défaut) = automatique.
"""
import os
import sys

R = sys.argv[1] if len(sys.argv) > 1 else '.'
F = os.path.join(R, 'data/mg/function')
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
import mcfn
_fn = mcfn.Fn(F)
w, sub = _fn.write, _fn.replace


SPAWN = '@a[tag=!mg.surv]'
GTA = '@a[tag=mg.gtw]'
TV = '@a[tag=mg.tvw]'
SV = '@a[tag=mg.surv,tag=!mg.gtw,tag=!mg.tvw,tag=!mg.olw,tag=!mg.fnw]'
FN = '@a[tag=mg.fnw]'
w('sb/auto', [
    '# 📊 Tableau de droite hors mini-jeu : celui de l\'endroit où sont le plus de joueurs (généré : tools/lobby/gen_sidebar.py)',
    'execute unless score $state mg.st matches 0 run return run scoreboard players set $sbm mg.st -1',
    'execute if score $sbo mg.st matches 1 unless score $sbm mg.st matches 9 run scoreboard objectives setdisplay sidebar',
    'execute if score $sbo mg.st matches 1 run return run scoreboard players set $sbm mg.st 9',
    f'execute store result score $sbc0 mg.st if entity {SPAWN}', f'execute store result score $sbc1 mg.st if entity {GTA}',
    f'execute store result score $sbc2 mg.st if entity {TV}', f'execute store result score $sbc3 mg.st if entity {SV}',
    f'execute store result score $sbc4 mg.st if entity {FN}',
    'scoreboard players set $sbn mg.st 0', 'scoreboard players operation $sbx mg.st = $sbc0 mg.st',
    'execute if score $sbc1 mg.st > $sbx mg.st run scoreboard players set $sbn mg.st 1',
    'execute if score $sbc1 mg.st > $sbx mg.st run scoreboard players operation $sbx mg.st = $sbc1 mg.st',
    'execute if score $sbc2 mg.st > $sbx mg.st run scoreboard players set $sbn mg.st 2',
    'execute if score $sbc2 mg.st > $sbx mg.st run scoreboard players operation $sbx mg.st = $sbc2 mg.st',
    'execute if score $sbc3 mg.st > $sbx mg.st run scoreboard players set $sbn mg.st 3',
    'execute if score $sbc3 mg.st > $sbx mg.st run scoreboard players operation $sbx mg.st = $sbc3 mg.st',
    'execute if score $sbc4 mg.st > $sbx mg.st run scoreboard players set $sbn mg.st 4',
    f'execute if score $sbn mg.st matches 3 as {SV} store result score @s mg.svl run experience query @s levels',
    # retour au spawn : rotation des tableaux généraux tout de suite
    'execute if score $sbn mg.st matches 0 unless score $sbm mg.st matches 0 run scoreboard players set $hrt mg.st 0',
    'execute if score $sbn mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.gta',
    'execute if score $sbn mg.st matches 2 run scoreboard objectives setdisplay sidebar mg.tvc',
    'execute if score $sbn mg.st matches 3 run scoreboard objectives setdisplay sidebar mg.svl',
    'execute if score $sbn mg.st matches 4 run scoreboard objectives setdisplay sidebar mg.fns',
    'scoreboard players operation $sbm mg.st = $sbn mg.st'])
w('core/opt_sidebar', ['# Tableau de droite hors mini-jeu : automatique (défaut) ou masqué ($sbo)',
                       'execute if score $sbo mg.st matches 1 run tellraw @s [{"text":"📊 Tableau de droite automatique : celui du spawn, de GTA, de Terra Nova ou de la survie selon où sont la plupart des joueurs (re-clique pour masquer).","color":"gold"}]',
                       'execute if score $sbo mg.st matches 1 run scoreboard players set $sbm mg.st -1',
                       'execute if score $sbo mg.st matches 1 run return run scoreboard players set $sbo mg.st 0',
                       'scoreboard players set $sbo mg.st 1',
                       'tellraw @s [{"text":"📊 Tableau de droite masqué hors mini-jeu.","color":"gray"}]'])
# rotation des tableaux généraux seulement quand le spawn l'emporte ; appel chaque seconde
sub('core/tick', 'execute if score $setup mg.st matches 1 if score $state mg.st matches 0 if score $sb mg.st matches 1 run function mg:hall/board_tick',
    'execute if score $setup mg.st matches 1 if score $state mg.st matches 0 if score $sbm mg.st matches 0 run function mg:hall/board_tick\n'
    'execute if score $setup mg.st matches 1 if score $lan mg.t matches 5 run function mg:sb/auto')
# votes : affichés par la rotation (hall/rot_votes) quand le spawn l'emporte
sub('vote/sidebar', 'execute if score $state mg.st matches 0 if score $vn mg.st matches 1.. run scoreboard objectives setdisplay sidebar mg.vb\n'
    'execute if score $state mg.st matches 0 if score $vn mg.st matches 0 if score $sb mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.wins\n'
    'execute if score $state mg.st matches 0 if score $vn mg.st matches 0 unless score $sb mg.st matches 1 run scoreboard objectives setdisplay sidebar',
    'execute if score $state mg.st matches 0 if score $vn mg.st matches 1.. if score $sbm mg.st matches 0 run scoreboard objectives setdisplay sidebar mg.vb\n'
    'execute if score $state mg.st matches 0 if score $vn mg.st matches 0 if score $sbm mg.st matches 0 run scoreboard players set $hrt mg.st 0')
# fin de partie : le tableau automatique reprend (à la seconde suivante)
sub('core/return_lobby', 'execute if score $sb mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.wins\n'
    'execute unless score $sb mg.st matches 1 run scoreboard objectives setdisplay sidebar',
    'scoreboard objectives setdisplay sidebar\nscoreboard players set $sbm mg.st -1')
sub('core/load', 'scoreboard objectives add mg.wins dummy',
    'scoreboard objectives add mg.svl dummy {"text":"⛏ Survie — niveau","color":"green"}\nscoreboard players set $sbm mg.st -1\nscoreboard objectives add mg.wins dummy')
sub('desinstaller', 'scoreboard objectives remove mg.wins', 'scoreboard objectives remove mg.svl\nscoreboard objectives remove mg.wins')
print('Tableau de droite automatique OK')
