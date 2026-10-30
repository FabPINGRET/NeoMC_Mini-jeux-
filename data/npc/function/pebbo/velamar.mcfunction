execute positioned 130 193 -2068 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 130 193 -2068 if score Inventory DominionRod matches 0 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Velamar of the Woken Spiral","color":"green"},{"text":"> The stones have told us news of the ","color":"white"},{"text":"Shrunken Temple","color":"green"},{"text":". They tell us it is sealed under a structure just north of the ","color":"white"},{"text":"Glooblin Tinker's workshop","color":"light_purple"},{"text":". The Cobblemancers behind me can teach you how to unseal it using","color":"white"},{"text":" 6 magic statues ","color":"green"},{"text":"standing watch across the Dark Isles.","color":"white"}]

execute positioned 130 193 -2068 if score Inventory DominionRod matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Velamar of the Woken Spiral","color":"green"},{"text":"> The stones have told us news of the ","color":"white"},{"text":"Lord of Stone's","color":"gray"},{"text":" rescue. I totally called it, I won a lot of money when the stones brought the news.","color":"white"}]

execute positioned 130 193 -2068 run kill @n[tag=quest_marker,distance=..3]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
