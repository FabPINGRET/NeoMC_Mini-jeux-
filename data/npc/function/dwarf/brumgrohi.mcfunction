execute positioned -232 71 -87 run playsound minecraft:entity.piglin.jealous neutral @a[tag=mg.flw] ~ ~ ~ 1 1.2
execute positioned -232 71 -87 if score traded_with_4 bool matches 0 unless items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['4']}] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brumgrohi","color":"dark_aqua"},{"text":"> AHH! My pants! My little pants keep falling down, and I don't have anything to hold them up! Do you have anything I could use to keep my little pants on? Like a","color":"white"},{"text":" Small Belt ","color":"gold"},{"text":"or something? If you do, I'll ","color":"white"},{"text":"trade","color":"yellow"},{"text":" you something interesting I found under a rock for it. Please!","color":"white"}]

execute positioned -232 71 -87 if score traded_with_4 bool matches 1 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brumgrohi","color":"dark_aqua"},{"text":"> Thanks again for finding my","color":"white"},{"text":" Small Belt","color":"gold"},{"text":". My little pants are oh so snug, and now they only fall down when I want them to! Do you like the ","color":"white"},{"text":"Mushroom ","color":"green"},{"text":"I gave you? I bet a hundred dwarf bucks","color":"white"},{"text":" someone with mandibles","color":"green"},{"text":" would smile so wide at it.","color":"white"}]

execute if score traded_with_4 bool matches 0 positioned -232 71 -87 if items entity @p[tag=mg.flw] weapon.mainhand minecraft:clay_ball[minecraft:custom_model_data={strings:['4']}] run tag @p[tag=mg.flw] add trade_complete

execute positioned -232 71 -87 as @p[tag=mg.flw] if entity @s[tag=trade_complete] run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brumgrohi","color":"dark_aqua"},{"text":"> Oh my stones! That","color":"white"},{"text":" Small Belt","color":"gold"},{"text":" would hold my pants right up! I'll put it on later, I want to keep my pants down for just a few more minutes. Here, you can take this","color":"white"},{"text":" Green Mushroom","color":"green"},{"text":" I discovered under a rock. I bet a hundred dwarf bucks ","color":"white"},{"text":"someone with mandibles","color":"green"},{"text":" would smile so wide at it.","color":"white"}]
execute positioned -232 71 -87 as @p[tag=mg.flw] if entity @s[tag=trade_complete] run item replace entity @s weapon.mainhand from block -233 68 -86 container.0
execute positioned -232 71 -87 as @p[tag=mg.flw] if entity @s[tag=trade_complete] run playsound minecraft:zelda.itemget master @p[tag=mg.flw] ~ ~ ~ 1 1
execute positioned -232 71 -87 as @p[tag=mg.flw] if entity @s[tag=trade_complete] run scoreboard players set traded_with_4 bool 1

tag @a[tag=mg.flw] remove trade_complete

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
