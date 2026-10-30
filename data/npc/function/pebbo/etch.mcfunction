execute positioned 10101 195 1208 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10101 195 1208 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Etch Metalscratch","color":"dark_purple"},{"text":"> You found your way to our ","color":"white"},{"text":"Armor Trim Workshop","color":"light_purple"},{"text":"! To decorate a piece of armor, simply ","color":"white"},{"text":"throw it onto the golden plate in front of the trim you want","color":"gold"},{"text":". We'll do the rest!","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
