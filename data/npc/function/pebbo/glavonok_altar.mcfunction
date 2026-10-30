execute positioned 10121 67 175 run playsound minecraft:entity.goat.milk neutral @a[tag=mg.flw] ~ ~ ~ 1 1
execute positioned 10128 68 184 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Glavonok the Monk of Shh","color":"red"},{"text":"> ","color":"white"},{"text":"Shhhhhhhhhhhhhhhhhhhhh","color":"dark_red","italic":true},{"text":" this blessing will let you use magic circles, though there exist only a few. Now simply","color":"white","italic":false},{"text":" go down the stairs, stand on the magic circle, and sneak","color":"red"}]

#set magic circle
#cobblemancer
setblock -9773 252 424 minecraft:redstone_block
#main kingdom
setblock 10127 60 200 minecraft:emerald_ore

scoreboard players set @a[tag=mg.flw] grow_timer -1
scoreboard players set @a[tag=mg.flw] shrink_timer -1

particle dust{color:[1.000,0.000,0.000],scale:2} 10128 69 184 1 1 1 0 45 normal

playsound minecraft:ambient.warped_forest.mood master @a[tag=mg.flw] 10128 69 184 1 1
playsound minecraft:entity.evoker.prepare_summon master @a[tag=mg.flw] 10128 69 184 1 1


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
