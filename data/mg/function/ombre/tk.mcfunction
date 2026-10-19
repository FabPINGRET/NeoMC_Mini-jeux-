# @s : choix dans une fenêtre (trigger mg.oltk)
scoreboard players operation $tk mg.st = @s mg.oltk
scoreboard players reset @s mg.oltk
scoreboard players enable @s mg.oltk
execute if score $tk mg.st matches 9 run function mg:ombre/q/say
execute if score $tk mg.st matches 9 run function mg:ombre/qloc
execute if score $tk mg.st matches 500 run function mg:ombre/cl/menu
execute if score $tk mg.st matches 601 run function mg:ombre/cl/pick_1
execute if score $tk mg.st matches 602 run function mg:ombre/cl/pick_2
execute if score $tk mg.st matches 603 run function mg:ombre/cl/pick_3
execute if score $tk mg.st matches 604 run function mg:ombre/cl/pick_4
execute if score $tk mg.st matches 701 run function mg:ombre/st/add_1
execute if score $tk mg.st matches 702 run function mg:ombre/st/add_2
execute if score $tk mg.st matches 703 run function mg:ombre/st/add_3
execute if score $tk mg.st matches 704 run function mg:ombre/st/add_4
execute if score $tk mg.st matches 709 run function mg:ombre/st/reset
execute if score $tk mg.st matches 710 run function mg:ombre/sheet
execute if score $tk mg.st matches 720 run function mg:ombre/ach_list
execute if score $tk mg.st matches 721 run function mg:ombre/bestiary
execute if score $tk mg.st matches 722 run function mg:ombre/sq_list
execute if score $tk mg.st matches 723 run function mg:ombre/mats
execute if score $tk mg.st matches 724 run function mg:ombre/travel
execute if score $tk mg.st matches 801 run function mg:ombre/sh/801
execute if score $tk mg.st matches 802 run function mg:ombre/sh/802
execute if score $tk mg.st matches 850 run function mg:ombre/ct/menu
execute if score $tk mg.st matches 399 in minecraft:overworld run function mg:ombre/leave
execute if score $tk mg.st matches 651 run function mg:ombre/sh/651
execute if score $tk mg.st matches 652 run function mg:ombre/sh/652
execute if score $tk mg.st matches 653 run function mg:ombre/sh/653
execute if score $tk mg.st matches 654 run function mg:ombre/sh/654
execute if score $tk mg.st matches 655 run function mg:ombre/sh/655
execute if score $tk mg.st matches 656 run function mg:ombre/sh/656
execute if score $tk mg.st matches 657 run function mg:ombre/sh/657
execute if score $tk mg.st matches 658 run function mg:ombre/sh/658
execute if score $tk mg.st matches 659 run function mg:ombre/sh/659
execute if score $tk mg.st matches 300 run function mg:ombre/ws/go0
execute if score $tk mg.st matches 301 run function mg:ombre/ws/go1
execute if score $tk mg.st matches 302 run function mg:ombre/ws/go2
execute if score $tk mg.st matches 303 run function mg:ombre/ws/go3
execute if score $tk mg.st matches 304 run function mg:ombre/ws/go4
execute if score $tk mg.st matches 305 run function mg:ombre/ws/go5
execute if score $tk mg.st matches 306 run function mg:ombre/ws/go6
execute if score $tk mg.st matches 307 run function mg:ombre/ws/go7
execute if score $tk mg.st matches 308 run function mg:ombre/ws/go8
execute if score $tk mg.st matches 1000 if score @s mg.olch matches 0 run function mg:ombre/q/ok0
execute if score $tk mg.st matches 1002 if score @s mg.olch matches 2 run function mg:ombre/q/ok2
execute if score $tk mg.st matches 1004 if score @s mg.olch matches 4 run function mg:ombre/q/ok4
execute if score $tk mg.st matches 1005 if score @s mg.olch matches 5 run function mg:ombre/q/ok5
execute if score $tk mg.st matches 1007 if score @s mg.olch matches 7 run function mg:ombre/q/ok7
execute if score $tk mg.st matches 1009 if score @s mg.olch matches 9 run function mg:ombre/q/ok9
execute if score $tk mg.st matches 1010 if score @s mg.olch matches 10 run function mg:ombre/q/ok10
execute if score $tk mg.st matches 1011 if score @s mg.olch matches 11 run function mg:ombre/q/ok11
execute if score $tk mg.st matches 1013 if score @s mg.olch matches 13 run function mg:ombre/q/ok13
execute if score $tk mg.st matches 1015 if score @s mg.olch matches 15 run function mg:ombre/q/ok15
execute if score $tk mg.st matches 1016 if score @s mg.olch matches 16 run function mg:ombre/q/ok16
execute if score $tk mg.st matches 1017 if score @s mg.olch matches 17 run function mg:ombre/q/ok17
execute if score $tk mg.st matches 1018 if score @s mg.olch matches 18 run function mg:ombre/q/ok18
execute if score $tk mg.st matches 1020 if score @s mg.olch matches 20 run function mg:ombre/q/ok20
execute if score $tk mg.st matches 1022 if score @s mg.olch matches 22 run function mg:ombre/q/ok22
execute if score $tk mg.st matches 1023 if score @s mg.olch matches 23 run function mg:ombre/q/ok23
execute if score $tk mg.st matches 1024 if score @s mg.olch matches 24 run function mg:ombre/q/ok24
execute if score $tk mg.st matches 1025 if score @s mg.olch matches 25 run function mg:ombre/q/ok25
execute if score $tk mg.st matches 1028 if score @s mg.olch matches 28 run function mg:ombre/q/ok28
execute if score $tk mg.st matches 1029 if score @s mg.olch matches 29 run function mg:ombre/q/ok29
execute if score $tk mg.st matches 1031 if score @s mg.olch matches 31 run function mg:ombre/q/ok31
execute if score $tk mg.st matches 1034 if score @s mg.olch matches 34 run function mg:ombre/q/ok34
execute if score $tk mg.st matches 1035 if score @s mg.olch matches 35 run function mg:ombre/q/ok35
execute if score $tk mg.st matches 1036 if score @s mg.olch matches 36 run function mg:ombre/q/ok36
execute if score $tk mg.st matches 1039 if score @s mg.olch matches 39 run function mg:ombre/q/ok39
execute if score $tk mg.st matches 1040 if score @s mg.olch matches 40 run function mg:ombre/q/ok40
execute if score $tk mg.st matches 1044 if score @s mg.olch matches 44 run function mg:ombre/q/ok44
execute if score $tk mg.st matches 1045 if score @s mg.olch matches 45 run function mg:ombre/q/ok45
execute if score $tk mg.st matches 1046 if score @s mg.olch matches 46 run function mg:ombre/q/ok46
execute if score $tk mg.st matches 1051 if score @s mg.olch matches 51 run function mg:ombre/q/ok51
execute if score $tk mg.st matches 402 run function mg:ombre/sq/1_acc
execute if score $tk mg.st matches 403 run function mg:ombre/sq/1_turn
execute if score $tk mg.st matches 404 run function mg:ombre/sq/2_acc
execute if score $tk mg.st matches 405 run function mg:ombre/sq/2_turn
execute if score $tk mg.st matches 406 run function mg:ombre/sq/3_acc
execute if score $tk mg.st matches 407 run function mg:ombre/sq/3_turn
execute if score $tk mg.st matches 408 run function mg:ombre/sq/4_acc
execute if score $tk mg.st matches 409 run function mg:ombre/sq/4_turn
execute if score $tk mg.st matches 410 run function mg:ombre/sq/5_acc
execute if score $tk mg.st matches 411 run function mg:ombre/sq/5_turn
execute if score $tk mg.st matches 412 run function mg:ombre/sq/6_acc
execute if score $tk mg.st matches 413 run function mg:ombre/sq/6_turn
execute if score $tk mg.st matches 414 run function mg:ombre/sq/7_acc
execute if score $tk mg.st matches 415 run function mg:ombre/sq/7_turn
execute if score $tk mg.st matches 416 run function mg:ombre/sq/8_acc
execute if score $tk mg.st matches 417 run function mg:ombre/sq/8_turn
execute if score $tk mg.st matches 418 run function mg:ombre/sq/9_acc
execute if score $tk mg.st matches 419 run function mg:ombre/sq/9_turn
execute if score $tk mg.st matches 420 run function mg:ombre/sq/10_acc
execute if score $tk mg.st matches 421 run function mg:ombre/sq/10_turn
execute if score $tk mg.st matches 422 run function mg:ombre/sq/11_acc
execute if score $tk mg.st matches 423 run function mg:ombre/sq/11_turn
execute if score $tk mg.st matches 424 run function mg:ombre/sq/12_acc
execute if score $tk mg.st matches 425 run function mg:ombre/sq/12_turn
execute if score $tk mg.st matches 426 run function mg:ombre/sq/13_acc
execute if score $tk mg.st matches 427 run function mg:ombre/sq/13_turn
execute if score $tk mg.st matches 428 run function mg:ombre/sq/14_acc
execute if score $tk mg.st matches 429 run function mg:ombre/sq/14_turn
execute if score $tk mg.st matches 430 run function mg:ombre/sq/15_acc
execute if score $tk mg.st matches 431 run function mg:ombre/sq/15_turn
execute if score $tk mg.st matches 432 run function mg:ombre/sq/16_acc
execute if score $tk mg.st matches 433 run function mg:ombre/sq/16_turn
