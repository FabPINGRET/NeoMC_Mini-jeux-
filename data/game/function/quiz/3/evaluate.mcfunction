playsound minecraft:entity.cow_moody.hurt neutral @a[tag=mg.flw] 10078 59 -244 1 1

execute if score quiz_answer_1 Value matches 1 if score quiz_answer_2 Value matches 5 if score quiz_answer_3 Value matches 1 if score quiz_answer_4 Value matches 3 if score quiz_answer_5 Value matches 2 run scoreboard players set quiz_3 bool 1

execute if score quiz_3 bool matches 1 run setblock 10084 60 -249 air
execute if score quiz_3 bool matches 1 run setblock 10084 59 -249 minecraft:chest[facing=south,type=single,waterlogged=false]{Items:[{Slot:13b,components:{"minecraft:custom_model_data":{strings:["17"]},"minecraft:custom_name":{bold:1b,color:"gold",text:"Sweet Sigil"},"minecraft:lore":["Aprentix can use this","to upgrade the","Honeyboost spell!"]},count:1,id:"minecraft:flint"}],components:{}}
execute if score quiz_3 bool matches 1 run particle block{block_state:"diamond_block"} 10084 59.5 -249 0.5 0.5 0.5 1 100
execute if score quiz_3 bool matches 1 run playsound minecraft:zelda.secret master @a[tag=mg.flw] 10084 59 -249 1 1 1 

execute if score quiz_3 bool matches 0 positioned 10078 59 -244 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> Sorry, you got one or more questions wrong! That's ok, you can ","color":"white"},{"text":"retake the quiz ","color":"light_purple"},{"text":"whenever you want!","color":"white"}]
execute if score quiz_3 bool matches 1 positioned 10078 59 -244 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Brainzo","color":"aqua"},{"text":"> You got every question correct! You've earned yourself a ","color":"white"},{"text":"prize","color":"aqua"},{"text":"! That's the last of my quizzes, I hope they grew your brain!","color":"white"}]

scoreboard players set doing_quiz Value 0
scoreboard players set quiz_question Value 0
