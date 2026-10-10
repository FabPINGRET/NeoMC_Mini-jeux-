tellraw @a[tag=mg.play] {"text":"👑 Tout le monde a raté : tour annulé !","color":"yellow"}
tag @a remove mg.msk
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.villager.no master @s ~ ~ ~ 1 1
