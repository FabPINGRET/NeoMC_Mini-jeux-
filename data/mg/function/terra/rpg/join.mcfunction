# @s : scores du RPG à la première visite
execute unless score @s mg.trlv matches 1.. run scoreboard players set @s mg.trlv 1
execute unless score @s mg.trxp matches -2147483648.. run scoreboard players set @s mg.trxp 0
execute unless score @s mg.trch matches -2147483648.. run scoreboard players set @s mg.trch 0
execute unless score @s mg.trqp matches -2147483648.. run scoreboard players set @s mg.trqp 0
execute unless score @s mg.trbs matches -2147483648.. run scoreboard players set @s mg.trbs 0
execute unless score @s mg.trpo matches -2147483648.. run scoreboard players set @s mg.trpo 0
execute unless score @s mg.trtv matches -2147483648.. run scoreboard players set @s mg.trtv 1
execute unless score @s mg.treg matches -2147483648.. run scoreboard players set @s mg.treg 0
execute unless score @s mg.trwp matches -2147483648.. run scoreboard players set @s mg.trwp 1
execute unless score @s mg.trml matches -2147483648.. run scoreboard players set @s mg.trml 1
execute unless score @s mg.trar matches -2147483648.. run scoreboard players set @s mg.trar 0
execute unless score @s mg.trmt matches -2147483648.. run scoreboard players set @s mg.trmt 0
execute unless score @s mg.trgr matches -2147483648.. run scoreboard players set @s mg.trgr 0
execute unless score @s mg.trdn matches -2147483648.. run scoreboard players set @s mg.trdn 0
execute unless score @s mg.trvn matches -2147483648.. run scoreboard players set @s mg.trvn 0
execute unless score @s mg.trec matches -2147483648.. run scoreboard players set @s mg.trec 0
execute unless score @s mg.trai matches -2147483648.. run scoreboard players set @s mg.trai 0
execute unless score @s mg.trrx matches -2147483648.. run scoreboard players set @s mg.trrx 0
execute unless score @s mg.trcl matches -2147483648.. run scoreboard players set @s mg.trcl 0
execute unless score @s mg.trcd matches -2147483648.. run scoreboard players set @s mg.trcd 0
execute unless score @s mg.trdg matches -2147483648.. run scoreboard players set @s mg.trdg 0
execute unless score @s mg.trs1 matches -2147483648.. run scoreboard players set @s mg.trs1 0
execute unless score @s mg.trs2 matches -2147483648.. run scoreboard players set @s mg.trs2 0
execute unless score @s mg.trs3 matches -2147483648.. run scoreboard players set @s mg.trs3 0
execute unless score @s mg.trs4 matches -2147483648.. run scoreboard players set @s mg.trs4 0
execute unless score @s mg.trkt matches -2147483648.. run scoreboard players set @s mg.trkt 0
execute unless score @s mg.trel matches -2147483648.. run scoreboard players set @s mg.trel 0
execute unless score @s mg.trac matches -2147483648.. run scoreboard players set @s mg.trac 0
execute unless score @s mg.trtc matches -2147483648.. run scoreboard players set @s mg.trtc 0
execute unless score @s mg.trsq matches -2147483648.. run scoreboard players set @s mg.trsq 0
execute unless score @s mg.trsa matches -2147483648.. run scoreboard players set @s mg.trsa 0
execute unless score @s mg.trq4 matches -2147483648.. run scoreboard players set @s mg.trq4 0
# points de caractéristique : 1 par niveau gagné (rattrapage pour les colons déjà avancés)
execute unless score @s mg.trsp matches -2147483648.. run function mg:terra/rpg/st/backfill
scoreboard players set @s mg.trrg 0
scoreboard players set @s mg.trpk 0
scoreboard players set @s mg.trsc 0
scoreboard players set @s mg.trdt 0
scoreboard players enable @s mg.trtk
function mg:terra/rpg/stats
