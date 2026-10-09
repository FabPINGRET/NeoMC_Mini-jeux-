# @s arrête de braquer
execute if score @s mg.grob matches 15.. run title @s actionbar {"text":"✋ Braquage interrompu","color":"gray"}
scoreboard players set @s mg.grob 0
