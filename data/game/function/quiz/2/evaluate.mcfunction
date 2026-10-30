playsound minecraft:entity.cow_moody.hurt neutral @a[tag=mg.flw] 10078 59 -244 1 1

execute if score quiz_answer_1 Value matches 4 if score quiz_answer_2 Value matches 1 if score quiz_answer_3 Value matches 1 if score quiz_answer_4 Value matches 3 run scoreboard players set quiz_2 bool 1

execute if score quiz_2 bool matches 1 run setblock 10082 60 -249 air
execute if score quiz_2 bool matches 1 run setblock 10082 59 -249 minecraft:lime_shulker_box[facing=up]{CustomName:"History Book",Items:[{Slot:13b,components:{"minecraft:custom_model_data":{strings:["11"]},"minecraft:custom_name":{color:"light_purple",text:"Brain Mesa History"},"minecraft:lore":["Can be opened","and read at the","Orc Library"]},count:1,id:"minecraft:armadillo_scute"}],components:{}}
execute if score quiz_2 bool matches 1 run particle block{block_state:"diamond_block"} 10082 59.5 -249 0.5 0.5 0.5 1 100
execute if score quiz_2 bool matches 1 run playsound minecraft:zelda.secret master @a[tag=mg.flw] 10082 59 -249 1 1 1 
execute if score quiz_2 bool matches 1 run scoreboard players set history_7 bool 1

execute if score quiz_2 bool matches 0 positioned 10078 59 -244 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> Sorry, you got one or more questions wrong! That's ok, you can ","color":"white"},{"text":"retake the quiz ","color":"light_purple"},{"text":"whenever you want!","color":"white"}]
execute if score quiz_2 bool matches 1 if score Inventory Honeyboost matches 0 positioned 10078 59 -244 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> You got every question correct! You've earned yourself a ","color":"white"},{"text":"prize","color":"aqua"},{"text":"! Come back after you've helped the ","color":"white"},{"text":"Glooblins","color":"light_purple"},{"text":" and I'll have another quiz for you!","color":"white"}]
execute if score quiz_2 bool matches 1 if score Inventory Honeyboost matches 1 positioned 10078 59 -244 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> You got every question correct! You've earned yourself a ","color":"white"},{"text":"prize","color":"aqua"},{"text":"! I actually have another quiz for you if you want to take it...","color":"white"}]

scoreboard players set doing_quiz Value 0
scoreboard players set quiz_question Value 0
