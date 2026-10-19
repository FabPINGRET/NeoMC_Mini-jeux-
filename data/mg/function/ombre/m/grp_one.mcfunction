# $(k) ×$g ici
$function mg:ombre/m/$(k)
tag @e[tag=mg.ollast] add mg.olnew
scoreboard players remove $g mg.st 1
$execute if score $g mg.st matches 1.. positioned ~1.5 ~ ~1 run function mg:ombre/m/grp_one {k:"$(k)"}
