execute positioned 10085 187 1306 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10085 187 1306 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Pebith the Namer","color":"red"},{"text":"> This archive is where we safeguard our knowledge for future generations. We also proudly display the banner of ","color":"white"},{"text":"each of the 5 Pebbo castes ","color":"red"},{"text":"to celebrate each one's contributions to our kingdom.","color":"white"}]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
