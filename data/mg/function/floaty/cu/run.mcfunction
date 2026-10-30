# Rattrape la partie commune pour @s (contexte quelconque) ; # généré par tools/floaty/fl_catchup.py : ne pas éditer
execute unless score $flsp mg.st matches 1.. in mg:floaty run spawnpoint @s 1274 209 181
execute if score $flsp mg.st matches 1 in mg:floaty run spawnpoint @s 9900 57 -241 0 0
execute if score $flsp mg.st matches 2 in mg:floaty run spawnpoint @s -12342 128 355 90 0
execute if score $flsp mg.st matches 3 in mg:floaty run spawnpoint @s -12354 -28 355 90 0
execute if score $flsp mg.st matches 4 in mg:floaty run spawnpoint @s -9885 191 272 90 0
execute if score $flsp mg.st matches 5 in mg:floaty run spawnpoint @s -11492 132 410
execute if score $flsp mg.st matches 6 in mg:floaty run spawnpoint @s -9923 147 -11
execute if score $flsp mg.st matches 7 in mg:floaty run spawnpoint @s -9907 155 -161
execute if score $flsp mg.st matches 8 in mg:floaty run spawnpoint @s -9919 108 -355
execute if score $flsp mg.st matches 9 in mg:floaty run spawnpoint @s -10139 84 299
execute if score $flsp mg.st matches 10 in mg:floaty run spawnpoint @s -10302 23 -71
execute if score $flsp mg.st matches 11 in mg:floaty run spawnpoint @s -10189 95 -378 90 0
execute if score $flsp mg.st matches 12 in mg:floaty run spawnpoint @s -10618 1 382 90 0
execute if score $flsp mg.st matches 13 in mg:floaty run spawnpoint @s -10799 80 -57 90 0
execute if score $flsp mg.st matches 14 in mg:floaty run spawnpoint @s -12239 184 -171 90 0
execute if score $flsp mg.st matches 15 in mg:floaty run spawnpoint @s -12134 55 336
execute if score $flsp mg.st matches 16 in mg:floaty run spawnpoint @s -2 57 -26 180 0
execute if score $flsp mg.st matches 17 in mg:floaty run spawnpoint @s -341 57 -246 0 0
execute if score $flsp mg.st matches 18 in mg:floaty run spawnpoint @s 283 57 -166 180 0
execute if score $flsp mg.st matches 19 in mg:floaty run spawnpoint @s 10468 52 110 0 -30
execute if score $flsp mg.st matches 20 in mg:floaty run spawnpoint @s 10440 58 -379 0 0
execute if score $flsp mg.st matches 21 in mg:floaty run spawnpoint @s 10085 187 1280 180 0
execute if score $flsp mg.st matches 22 in mg:floaty run spawnpoint @s 9799 57 77 -90 0
execute if score $flsp mg.st matches 23 in mg:floaty run spawnpoint @s -9832 249 566 0 0
execute if score $flsp mg.st matches 24 in mg:floaty run spawnpoint @s 9997 59 242 180 0
execute if score $flsp mg.st matches 25 in mg:floaty run spawnpoint @s 94 47 53 90 0
execute if score $flsp mg.st matches 26 in mg:floaty run spawnpoint @s 152 58 -12
execute if score $flsp mg.st matches 27 in mg:floaty run spawnpoint @s -10441 84 429 0 0
execute if score $flsp mg.st matches 28 in mg:floaty run spawnpoint @s -10060 116 322 0 0
execute if score $flsp mg.st matches 29 in mg:floaty run spawnpoint @s -10066 123 179 135 -20
execute if score $flsp mg.st matches 30 in mg:floaty run spawnpoint @s -10682 72 89 90 0
execute if score $flsp mg.st matches 31 in mg:floaty run spawnpoint @s -9960 100 358 0 0
execute if score $flsp mg.st matches 32 in mg:floaty run spawnpoint @s -11760 173 -184 180 0
execute if score $flsp mg.st matches 33 in mg:floaty run spawnpoint @s -10340 88 435 0 0
execute if score $flsp mg.st matches 34 in mg:floaty run spawnpoint @s 10525 42 -168 90 0
execute if score $flsp mg.st matches 35 in mg:floaty run spawnpoint @s -11144 58 448 180 0
execute if score $flsp mg.st matches 36 in mg:floaty run spawnpoint @s 285 80 1454 180 0
execute if score $flsp mg.st matches 37 in mg:floaty run spawnpoint @s 10022 94 -87 180 0
execute if score $flsp mg.st matches 38 in mg:floaty run spawnpoint @s -11146 68 347 180 0
execute if score $flsp mg.st matches 39 in mg:floaty run spawnpoint @s -9864 109 557 0 0
execute if score $flsp mg.st matches 40 in mg:floaty run spawnpoint @s 214 43 117
execute if score $flsp mg.st matches 41 in mg:floaty run spawnpoint @s -10210 68 131 -90 0
# partie pas commencée : rien d'autre à rattraper (mainstory Story = -1 à l'installation)
execute unless score mainstory Story matches 0.. run return 0
# vie max = 2 x cœurs du groupe
execute if score Inventory HeartContainers matches 1.. store result storage mg:floaty cu.h int 2 run scoreboard players get Inventory HeartContainers
execute if score Inventory HeartContainers matches 1.. run function mg:floaty/cu/hp with storage mg:floaty cu
# avancements déjà accordés au groupe
execute if score $fla1 mg.fla matches 1 run advancement grant @s only main_quest:first_dungeon
execute if score $fla2 mg.fla matches 1 run advancement grant @s only main_quest:tenth_dungeon
execute if score $fla3 mg.fla matches 1 run advancement grant @s only main_quest:second_dungeon
execute if score $fla4 mg.fla matches 1 run advancement grant @s only main_quest:third_dungeon
execute if score $fla5 mg.fla matches 1 run advancement grant @s only main_quest:fourth_dungeon
execute if score $fla6 mg.fla matches 1 run advancement grant @s only main_quest:fifth_dungeon
execute if score $fla7 mg.fla matches 1 run advancement grant @s only main_quest:sixth_dungeon
execute if score $fla8 mg.fla matches 1 run advancement grant @s only main_quest:seventh_dungeon
execute if score $fla9 mg.fla matches 1 run advancement grant @s only main_quest:eighth_dungeon
execute if score $fla10 mg.fla matches 1 run advancement grant @s only main_quest:ninth_dungeon
execute if score $fla11 mg.fla matches 1 run advancement grant @s only main_quest:game_finish
execute if score $fla12 mg.fla matches 1 run advancement grant @s only sidequest:undercroft_boss
execute if score $fla13 mg.fla matches 1 run advancement grant @s only main_quest:root
execute if score $fla14 mg.fla matches 1 run advancement grant @s only main_quest:floaty_isles
execute if score $fla15 mg.fla matches 1 run advancement grant @s only main_quest:dungeons
execute if score $fla16 mg.fla matches 1 run advancement grant @s only sidequest:root
execute if score $fla17 mg.fla matches 1 run advancement grant @s only sidequest_2:root
execute if score $fla18 mg.fla matches 1 run advancement grant @s only sidequest_2:collection
execute if score $fla19 mg.fla matches 1 run advancement grant @s only sidequest_2:exploration
execute if score $fla20 mg.fla matches 1 run advancement grant @s only sidequest_2:encounters
execute if score $fla21 mg.fla matches 1 run advancement grant @s only sidequest_2:misc
execute if score $fla22 mg.fla matches 1 run advancement grant @s only sidequest_2:minibosses
execute if score $fla23 mg.fla matches 1 run advancement grant @s only sidequest_2:npcs
execute if score $fla24 mg.fla matches 1 run advancement grant @s only sidequest_2:forgemuzzle
execute if score $fla25 mg.fla matches 1 run advancement grant @s only sidequest:netherite_start
execute if score $fla26 mg.fla matches 1 run advancement grant @s only sidequest:netherite_complete
execute if score $fla27 mg.fla matches 1 run advancement grant @s only sidequest_2:nacre
execute if score $fla28 mg.fla matches 1 run advancement grant @s only main_quest:quest_10
execute if score $fla29 mg.fla matches 1 run advancement grant @s only main_quest:quest_8
execute if score $fla30 mg.fla matches 1 run advancement grant @s only sidequest_2:npc_s18
execute if score $fla31 mg.fla matches 1 run advancement grant @s only sidequest:lovebug_2
execute if score $fla32 mg.fla matches 1 run advancement grant @s only sidequest:lovebug_4
execute if score $fla33 mg.fla matches 1 run advancement grant @s only sidequest:lovebug_6
execute if score $fla34 mg.fla matches 1 run advancement grant @s only sidequest:lovebug_9
execute if score $fla35 mg.fla matches 1 run advancement grant @s only sidequest:lovebug_12
execute if score $fla36 mg.fla matches 1 run advancement grant @s only sidequest:lovebug_15
execute if score $fla37 mg.fla matches 1 run advancement grant @s only sidequest:lovebug_18
execute if score $fla38 mg.fla matches 1 run advancement grant @s only sidequest:lovebug_24
execute if score $fla39 mg.fla matches 1 run advancement grant @s only sidequest_2:yommod_complete
execute if score $fla40 mg.fla matches 1 run advancement grant @s only main_quest:quest_1
execute if score $fla41 mg.fla matches 1 run advancement grant @s only main_quest:quest_6
execute if score $fla42 mg.fla matches 1 run advancement grant @s only sidequest_2:bard_start
execute if score $fla43 mg.fla matches 1 run advancement grant @s only sidequest_2:bard_finish
execute if score $fla44 mg.fla matches 1 run advancement grant @s only sidequest_2:library_complete
execute if score $fla45 mg.fla matches 1 run advancement grant @s only main_quest:quest_11
execute if score $fla46 mg.fla matches 1 run advancement grant @s only main_quest:quest_4
execute if score $fla47 mg.fla matches 1 run advancement grant @s only main_quest:quest_5
execute if score $fla48 mg.fla matches 1 run advancement grant @s only sidequest:potion_complete
