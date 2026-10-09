# Départ : 1 zombie pour 5 joueurs (au moins 1)
scoreboard players set $ift mg.st 0
scoreboard players set @a mg.deaths 0
execute as @a[tag=mg.play] run function mg:inf3/kit
execute store result score $inn mg.st if entity @a[tag=mg.play]
scoreboard players set #5 mg.st 5
scoreboard players operation $inn mg.st /= #5 mg.st
execute if score $inn mg.st matches ..0 run scoreboard players set $inn mg.st 1
execute if score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 run function mg:inf3/pick
execute if score $infm mg.st matches 1 run function mg:inf3/mstart
tellraw @a[tag=mg.play] [{"text":"🧪 INFECTION : ","color":"dark_green","bold":true},{"text":"les zombies infectent les survivants qu'ils tuent. Survivants : tenez 3 minutes (clic droit = tirer, accroupi = recharger) ! Zombies : contaminez tout le monde.","color":"gray"}]
execute unless score $n0 mg.st matches 2.. unless score $infm mg.st matches 1 run tellraw @a[tag=mg.play] [{"text":"🧪 Mode entraînement (seul) : pas de zombie, essaie les armes (clic droit = tirer, accroupi = recharger). Pas de victoire ; il faut au moins 2 joueurs pour une vraie partie.","color":"yellow"}]
