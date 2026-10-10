# @s = bateau tamponneur
scoreboard players set @s mg.atc 20
execute on passengers if entity @s[type=minecraft:player,tag=mg.play] run scoreboard players add @s mg.atp 1
execute on passengers if entity @s[type=minecraft:player,tag=mg.play] run title @s actionbar {"text":"💥 Tamponné ! +1","color":"green","bold":true}
