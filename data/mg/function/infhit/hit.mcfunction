# Avancement mg:infhit : @s touché par un zombie (mob) ou un joueur infecté (équipe verte)
advancement revoke @s only mg:infhit
execute if score $state mg.st matches 2 if score $infm mg.st matches 1 if entity @s[tag=mg.play,tag=!mg.inf] run tag @s add mg.zhit
