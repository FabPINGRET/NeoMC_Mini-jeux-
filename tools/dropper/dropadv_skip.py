# ================================================================== DROPPER : « PASSER CE NIVEAU » (Aventure id 64 et Essais id 228)
# Exécuté par gen_dropper_adv.py (exec, avant prepare/go/tick/hud) : utilise wr, N, R, PLAY. Défi (id 65) n'est pas concerné.
# Objet en hotbar.8 (clic droit 2 fois en 3 s) : le joueur passe au niveau suivant, qui compte comme NON réussi.
# Le classement se fait sur les niveaux réussis (mg.dok) ; un joueur qui finit après une passe (mg.dsk) n'est jamais déclaré
# vainqueur et ne met pas fin à la partie : il passe spectateur (tag mg.ddone). Le code ne lit que mg.dlv, jamais L.k ni L.n.
# Objectifs : mg.dok niveaux réussis, mg.dsk nombre de passes, mg.dkc fenêtre de confirmation (ticks), mg.dku anti-maintien (ticks).
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'arcade'))
import common as C

ITEM = ('minecraft:warped_fungus_on_a_stick[custom_data={mg_dskip:1b},item_model="minecraft:spectral_arrow",unbreakable={},'
        'custom_name=[{"text":"⏭ Passer ce niveau","color":"gold","bold":true,"italic":false}],'
        'lore=[[{"text":"Clic droit 2 fois (en 3 s) : niveau suivant,","color":"gray","italic":false}],'
        '[{"text":"mais il ne compte pas comme réussi","color":"gray","italic":false}]]]')
HAS = '*[custom_data~{mg_dskip:1b}]'
CLEAR = f'clear @s minecraft:warped_fungus_on_a_stick{HAS[1:]}'       # retire l'objet (arrivée, spectateur)
PROMPT = '"⏭ Clic droit encore pour passer (ne comptera pas)"'
# objets jetés (Q) : supprimés dans la zone des puits (mêmes bornes que fl_add : x -WALL-6 .. (N-1)*SPACING+WALL+6, z CZ±(WALL+6), y 0 .. TOP+8)
KKILL_AS = (f'as @e[type=minecraft:item,x={-WALL - 6},y=0,z={CZ - WALL - 6},dx={(N - 1) * SPACING + 2 * WALL + 12},dy={TOP + 8},dz={2 * WALL + 12}] '
            f'if items entity @s contents {HAS} run kill @s')
KKILL = 'execute ' + KKILL_AS
# donné seulement s'il n'est ni dans l'inventaire, ni dans la seconde main, ni sur le curseur (inventaire ouvert)
KHUD = [f'execute unless items entity @s container.* {HAS} unless items entity @s weapon.offhand {HAS} unless items entity @s player.cursor {HAS} run function mg:dropadv/k_give',
        f'execute if score @s mg.dkc matches 1.. run return run title @s actionbar {PROMPT}']
# objectifs de partie (créés par prepare / s_prepare) et leur remise à zéro ; mg.dok porte le même nom affiché dans les deux modes
KPREP = ['scoreboard objectives add mg.dok dummy [{"text":"⬇ Dropper : niveaux réussis","color":"aqua","bold":true}]',
         'scoreboard objectives add mg.dsk dummy', 'scoreboard objectives add mg.dkc dummy', 'scoreboard objectives add mg.dku dummy']
KRESET = [f'scoreboard players set @a[tag=mg.play] {o} 0' for o in ('mg.dok', 'mg.dsk', 'mg.dkc', 'mg.dku')]
KGO = ('tellraw @a[tag=mg.play] [{"text":"⏭ ","color":"gold","bold":true},{"text":"Objet « Passer ce niveau » (dernier emplacement) : clic droit 2 fois en 3 s '
       'pour aller au niveau suivant. Il ne compte pas comme réussi : sans niveau réussi, pas de victoire !","color":"gray"}]')

wr('k_give', ['# Redonne l\'objet « Passer ce niveau » (jeté, perdu ou déplacé)', f'item replace entity @s hotbar.8 with {ITEM}'])
wr('k_tick', ['# Passer un niveau : clic droit sur l\'objet (mg.qs), puis décompte de la confirmation (mg.dkc) et de l\'anti-maintien (mg.dku)',
              f'execute as {PLAY[:-1]},scores={{mg.qs=1..}}] if items entity @s weapon.mainhand {HAS} run function mg:dropadv/k_use',
              'scoreboard players reset @a[tag=mg.play,scores={mg.qs=1..}] mg.qs',
              'scoreboard players remove @a[tag=mg.play,scores={mg.dkc=1..}] mg.dkc 1',
              'scoreboard players remove @a[tag=mg.play,scores={mg.dku=1..}] mg.dku 1',
              f'execute if score $dam mg.st matches 0 {KKILL_AS}'])      # $dam : cadence de 10 ticks calculée par tick / s_tick
wr('k_use', ['# @s a fait un clic droit avec l\'objet : 1er clic = demande de confirmation (3 s), 2e clic = on passe le niveau',
             'scoreboard players reset @s mg.qs',
             'execute unless score $state mg.st matches 2 run return 0',
             '# bouton maintenu : l\'utilisation se répète toutes les 4 ticks, mg.dku l\'absorbe (seul un vrai nouveau clic confirme)',
             'execute if score @s mg.dku matches 1.. run return run scoreboard players set @s mg.dku 6',
             'scoreboard players set @s mg.dku 6',
             'execute if score @s mg.dkc matches 1.. run return run function mg:dropadv/k_skip',
             'scoreboard players set @s mg.dkc 60',
             f'title @s actionbar {PROMPT}',
             'execute at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 1.2'])
wr('k_skip', ['# @s passe son niveau (mg.dlv) : niveau suivant, sans point de réussite (mg.dok inchangé)',
              'scoreboard players set @s mg.dkc 0', 'scoreboard players add @s mg.dsk 1',
              'tellraw @a[tag=mg.play] [{"text":"⏭ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" passe le niveau ","color":"gray"},{"score":{"name":"@s","objective":"mg.dlv"},"color":"aqua","bold":true},{"text":" (non réussi)","color":"gray"}]',
              'execute at @s run playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 0.8 1.2',
              'scoreboard players add @s mg.dlv 1',
              f'execute if score @s mg.dlv matches {N + 1}.. if score $game mg.st matches 228 run return run function mg:dropadv/s_done',
              f'execute if score @s mg.dlv matches {N + 1}.. run return run function mg:dropadv/finish',
              'execute if score $game mg.st matches 228 run scoreboard players add @s mg.dtt 1',
              'execute if score $game mg.st matches 228 run scoreboard players set @s mg.dtr 1',
              'function mg:dropadv/spawn', 'function mg:dropadv/show_level'])
wr('k_done', ['# Aventure : @s arrive au bout après au moins une passe : pas de victoire, spectateur, la partie continue',
              'tag @s add mg.ddone', 'gamemode spectator @s', CLEAR,
              f'tellraw @a[tag=!mg.surv] [{{"text":"🏁 ","color":"gold"}},{{"selector":"@s","color":"gold","bold":true}},{{"text":" arrive au bout : ","color":"yellow"}},{{"score":{{"name":"@s","objective":"mg.dok"}},"color":"white","bold":true}},{{"text":"/{N} réussis, ","color":"yellow"}},{{"score":{{"name":"@s","objective":"mg.dsk"}},"color":"white"}},{{"text":" passé(s) — pas de victoire à l\'arrivée (classement final aux niveaux réussis)","color":"yellow"}}]',
              'execute at @s run playsound minecraft:ui.toast.challenge_complete master @s ~ ~ ~ 1 1'])
wr('k_end', ['# Aventure : plus personne en jeu (tous ont fini, avec des passes) : même résultat qu\'au temps écoulé, scores figés',
             'execute unless score $state mg.st matches 2 run return 0',
             'tellraw @a[tag=!mg.surv] [{"text":"🏁 Tout le monde est arrivé au bout !","color":"gold"}]',
             'function mg:dropadv/k_rank'])
wr('k_rank', ['# Aventure : classement aux niveaux réussis (puis le moins d\'échecs) ; personne n\'a réussi de niveau : match nul',
              'execute unless score $state mg.st matches 2 run return 0',
              f'execute as @a[tag=mg.play] run tellraw @a[tag=!mg.surv] [{{"selector":"@s","color":"yellow"}},{{"text":" : ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.dok"}},"color":"white","bold":true}},{{"text":"/{N} réussis, ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.dsk"}},"color":"white"}},{{"text":" passé(s), ","color":"gray"}},{{"score":{{"name":"@s","objective":"mg.dfl"}},"color":"white"}},{{"text":" échec(s)","color":"gray"}}]',
              'execute unless entity @a[tag=mg.play,scores={mg.dok=1..}] run return run function mg:core/draw',
              'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t = @s mg.dok',
              'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st',
              'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t *= #k1000 mg.st',
              'execute as @a[tag=mg.play] run scoreboard players operation @s mg.t -= @s mg.dfl',
              'scoreboard players set $dbest mg.st -999999999',
              'execute as @a[tag=mg.play] if score @s mg.t > $dbest mg.st run scoreboard players operation $dbest mg.st = @s mg.t',
              'execute as @a[tag=mg.play] if score @s mg.t = $dbest mg.st run tag @s add mg.dwin',
              'execute as @a[tag=mg.dwin,limit=1] run function mg:core/win_player',
              'tag @a remove mg.dwin'])

C.init(R)
for _o in ('mg.dok', 'mg.dsk', 'mg.dkc', 'mg.dku'):              # objectifs de partie (créés par prepare / s_prepare)
    C.patch('desinstaller', 'scoreboard objectives remove mg.bw', [f'scoreboard objectives remove {_o}'])
