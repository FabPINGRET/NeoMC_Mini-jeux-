playsound minecraft:entity.cow_moody.hurt neutral @a[tag=mg.flw] 10078 59 -244 1 1

execute if score quiz_answer_1 Value matches 4 if score quiz_answer_2 Value matches 3 if score quiz_answer_3 Value matches 2 run scoreboard players set quiz_1 bool 1

execute if score quiz_1 bool matches 1 run setblock 10080 60 -249 air
execute if score quiz_1 bool matches 1 run setblock 10080 59 -249 minecraft:purple_shulker_box[facing=up]{CustomName:"Secret Key",Items:[{Slot:13b,components:{"minecraft:custom_name":{color:"dark_purple",italic:0b,text:"Secret Key"},"minecraft:lore":[{color:"aqua",text:"Bring it to"},{color:"gray",italic:1b,text:"*checks notes*"},{color:"aqua",text:"Quarsheesha!"}]},count:1,id:"minecraft:iron_nugget"}],components:{}}
execute if score quiz_1 bool matches 1 run particle block{block_state:"diamond_block"} 10080 59.5 -249 0.5 0.5 0.5 1 100
execute if score quiz_1 bool matches 1 run playsound minecraft:zelda.secret master @a[tag=mg.flw] 10080 59 -249 1 1 1 
execute if score quiz_1 bool matches 1 run scoreboard players set key_28 bool 1

execute if score quiz_1 bool matches 0 positioned 10078 59 -244 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> Sorry, you got one or more questions wrong! That's ok, you can ","color":"white"},{"text":"retake the quiz ","color":"light_purple"},{"text":"whenever you want!","color":"white"}]
execute if score quiz_1 bool matches 1 if score Inventory TomeOfTongues matches 0 positioned 10078 59 -244 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> You got every question correct! You've earned yourself a ","color":"white"},{"text":"prize","color":"aqua"},{"text":"! Come back after you've helped the ","color":"white"},{"text":"Pygmies","color":"green"},{"text":" and I'll have another quiz for you!","color":"white"}]
execute if score quiz_1 bool matches 1 if score Inventory TomeOfTongues matches 1 positioned 10078 59 -244 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> You got every question correct! You've earned yourself a ","color":"white"},{"text":"prize","color":"aqua"},{"text":"! I actually have another quiz for you if you want to take it...","color":"white"}]

scoreboard players set doing_quiz Value 0
scoreboard players set quiz_question Value 0
