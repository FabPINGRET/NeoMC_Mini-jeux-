# +1 victoire dans le classement d'un jeu (@s) — macro
$scoreboard players add @s $(obj) 1
$scoreboard players set #any $(obj) 1
$function mg:hall/top {obj:"$(obj)",key:"$(key)",lbl:"$(lbl)",col:"$(col)",unit:""}
$function mg:hall/t3 {k:"$(key)",obj:"$(obj)",lbl:"$(lbl)",col:"$(col)"}
