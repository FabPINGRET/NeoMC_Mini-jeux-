# Retour au lobby de tous les participants + nettoyage du monde

# Classements par jeu et hall des scores : crédit des vainqueurs (avant la remise à zéro des tags)
execute as @a[tag=mg.win] run function mg:hall/credit

# Mini Party : pièces du mini-jeu (avant la remise à zéro des tags), ou fin de la partie si c'est le plateau qui s'arrête
execute if score $mp mg.st matches 1 unless score $game mg.st matches 59 run function mg:party/reward
execute if score $game mg.st matches 59 run function mg:party/end

execute if score $game mg.st matches 61 run function mg:kart/cleanup
execute if score $game mg.st matches 64..65 run function mg:dropadv/cleanup
execute if score $game mg.st matches 66 run function mg:elyrace/cleanup
kill @e[tag=mg.ib]
execute if score $game mg.st matches 57..58 run function mg:bb/cleanup
execute as @a[tag=mg.play] run function mg:core/reset_player
execute as @a[tag=mg.out] run function mg:core/reset_player

tag @a remove mg.prot
tag @a remove mg.qdd
tag @a remove mg.qsh
kill @e[type=minecraft:marker,tag=mg.grm]
tag @a remove mg.top
tag @a remove mg.osh

# Nettoyage des entités de jeu
kill @e[tag=mg.mob]
kill @e[tag=mg.sheep]
kill @e[tag=mg.npc]
kill @e[tag=mg.proj]
kill @e[tag=mg.fx]
kill @e[distance=0..,type=minecraft:item]
kill @e[distance=0..,type=minecraft:arrow]
kill @e[distance=0..,type=minecraft:snowball]
kill @e[distance=0..,type=minecraft:tnt]
kill @e[distance=0..,type=minecraft:experience_orb]
kill @e[distance=0..,type=minecraft:ender_pearl]
kill @e[distance=0..,type=minecraft:egg]
kill @e[tag=mg.sh]
kill @e[tag=mg.anv]
kill @e[tag=mg.hl]
kill @e[tag=mg.alembic]
kill @e[tag=mg.cloud]
kill @e[tag=mg.meteor]
kill @e[distance=0..,type=minecraft:chicken]


# Règles remises à la normale (régénération / grief modifiés par PvP et Mob Arena)
function mg:core/regen_on
function mg:core/grief_on

function mg:core/hp_display
bossbar remove mg:boss
execute if score $sb mg.st matches 1 run scoreboard objectives setdisplay sidebar mg.wins
execute unless score $sb mg.st matches 1 run scoreboard objectives setdisplay sidebar
scoreboard players set $state mg.st 0
scoreboard players set $game mg.st 0
function mg:vote/refresh

execute if score $mp mg.st matches 1 run return run function mg:party/resume
tellraw @a [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Retour au lobby — choisis le prochain jeu !","color":"gray"}]
