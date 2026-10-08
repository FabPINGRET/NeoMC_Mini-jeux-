# (OP) Efface tout le décor Élytra (pour reconstruire après une modification du générateur)
execute if score $skbm mg.st matches 1.. run return run tellraw @a[tag=mg.admin] [{"text":"[Mini-Jeux] ","color":"gold"},{"text":"Élytra : construction en cours, réessaie plus tard.","color":"yellow"}]
data remove storage mg:sky built
scoreboard players set $skbm mg.st 2
scoreboard players set $skbs mg.st 0
scoreboard players set $skw mg.st 0
scoreboard players set $skbn mg.st 112
schedule function mg:sky/b_next 1t
