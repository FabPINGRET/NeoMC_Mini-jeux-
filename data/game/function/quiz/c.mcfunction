execute if score quiz_question Value matches 1 run scoreboard players set quiz_answer_1 Value 3
execute if score quiz_question Value matches 2 run scoreboard players set quiz_answer_2 Value 3
execute if score quiz_question Value matches 3 run scoreboard players set quiz_answer_3 Value 3
execute if score quiz_question Value matches 4 run scoreboard players set quiz_answer_4 Value 3
execute if score quiz_question Value matches 5 run scoreboard players set quiz_answer_5 Value 3

execute if score doing_quiz Value matches 1 if score quiz_question Value matches 1 run schedule function floaty:sched/game/quiz/1/2 1s
execute if score doing_quiz Value matches 1 if score quiz_question Value matches 2 run schedule function floaty:sched/game/quiz/1/3 1s
execute if score doing_quiz Value matches 1 if score quiz_question Value matches 3 run schedule function floaty:sched/game/quiz/1/evaluate 1s

execute if score doing_quiz Value matches 2 if score quiz_question Value matches 1 run schedule function floaty:sched/game/quiz/2/2 1s
execute if score doing_quiz Value matches 2 if score quiz_question Value matches 2 run schedule function floaty:sched/game/quiz/2/3 1s
execute if score doing_quiz Value matches 2 if score quiz_question Value matches 3 run schedule function floaty:sched/game/quiz/2/4 1s
execute if score doing_quiz Value matches 2 if score quiz_question Value matches 4 run schedule function floaty:sched/game/quiz/2/evaluate 1s

execute if score doing_quiz Value matches 3 if score quiz_question Value matches 1 run schedule function floaty:sched/game/quiz/3/2 1s
execute if score doing_quiz Value matches 3 if score quiz_question Value matches 2 run schedule function floaty:sched/game/quiz/3/3 1s
execute if score doing_quiz Value matches 3 if score quiz_question Value matches 3 run schedule function floaty:sched/game/quiz/3/4 1s
execute if score doing_quiz Value matches 3 if score quiz_question Value matches 4 run schedule function floaty:sched/game/quiz/3/5 1s
execute if score doing_quiz Value matches 3 if score quiz_question Value matches 5 run schedule function floaty:sched/game/quiz/3/evaluate 1s

fill 10080 59 -245 10084 59 -245 air
scoreboard players set quiz_question Value -1

execute if score Inventory Amulet matches 1 if score quiz_1 bool matches 0 if score doing_quiz Value matches 0 run schedule function floaty:sched/game/quiz/1/start 1s
execute if score Inventory TomeOfTongues matches 1 if score quiz_1 bool matches 1 if score quiz_2 bool matches 0 if score doing_quiz Value matches 0 run schedule function floaty:sched/game/quiz/2/start 1s
execute if score Inventory Honeyboost matches 1 if score quiz_2 bool matches 1 if score quiz_3 bool matches 0 if score doing_quiz Value matches 0 run schedule function floaty:sched/game/quiz/3/start 1s
