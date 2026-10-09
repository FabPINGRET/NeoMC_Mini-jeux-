# @s : toutes les 15 s, une étoile de moins
scoreboard players remove @s mg.gwl 1
scoreboard players set @s mg.gwt 300
execute if score @s mg.gwl matches 0 run team join mg_gciv @s
execute if score @s mg.gwl matches 0 run scoreboard players set @s mg.gal 40
execute if score @s mg.gwl matches 0 run title @s actionbar {"text":"☆ La police a perdu ta trace","color":"green"}
