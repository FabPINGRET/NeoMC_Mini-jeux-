# @s tire au lobby : les autres joueurs du lobby deviennent des cibles le temps du tir (un demi-cœur, voir gun/hit_player)
tag @a[tag=!mg.play,tag=!mg.surv,tag=!mg.gtw,gamemode=!spectator,gamemode=!creative,tag=!mg.gtg] add mg.lgt
tag @a[tag=mg.lgt] add mg.gtg
tag @s add mg.lsh
tag @s add mg.ghd
function mg:gun/use
tag @s remove mg.lsh
tag @s remove mg.ghd
tag @a[tag=mg.lgt] remove mg.gtg
tag @a remove mg.lgt
