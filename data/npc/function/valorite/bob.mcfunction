execute at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run playsound minecraft:entity.armadillo.death neutral @a[tag=mg.flw] ~ ~ ~ 1 0.5
execute if block 9884 57 -126 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dark Bob Saget","color":"#D47453"},{"text":"> Hey there, you look like you have a funny mind! We're trying to develop a theatrical performance for the next season of ","color":"white"},{"text":"Dark Isles's Funniest Home Plays","color":"gold"},{"text":", but we've been running into writer's block. You can press either button to start the performance and ","color":"white"},{"text":"guide the actors","color":"gold"},{"text":" through what you think should happen next. If you help us make a perfect play, it would make me ","color":"white"},{"text":"very, very happy","color":"red"},{"text":"!","color":"white"}]

execute unless block 9884 57 -126 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1 ~ run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dark Bob Saget","color":"#D47453"},{"text":"> Hey there, thanks for lending me your funny mind! The next season of ","color":"white"},{"text":"Dark Isles's Funniest Home Plays","color":"gold"},{"text":" is going to be incredible thanks to you. You can press either button to start a performance and ","color":"white"},{"text":"guide the actors","color":"gold"},{"text":" again if you want. You've made me ","color":"white"},{"text":"very, very happy","color":"red"},{"text":" producer!","color":"white"}]

execute unless block 9884 57 -126 air at @e[sort=nearest,limit=1,tag=npc,distance=0..] positioned ~ ~1.75 ~ run particle minecraft:heart ~ ~ ~ 0.3 0.3 0.3 0 10 force


setblock 9884 61 -133 minecraft:mangrove_sign[rotation=3,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"white",has_glowing_text:1b,messages:["",{bold:1b,text:"A"},"",""]},is_waxed:0b}
setblock 9884 61 -130 minecraft:mangrove_sign[rotation=5,waterlogged=false]{back_text:{color:"black",has_glowing_text:0b,messages:["","","",""]},components:{},front_text:{color:"white",has_glowing_text:1b,messages:["",{bold:1b,text:"B"},"",""]},is_waxed:0b}
setblock 9883 61 -132 minecraft:stone_button[face=floor,facing=east,powered=false]
setblock 9883 61 -131 minecraft:stone_button[face=floor,facing=east,powered=false]

#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
