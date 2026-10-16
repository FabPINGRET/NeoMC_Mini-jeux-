# @s : affiche son ordre (mg.mo / mg.mv)
execute if score @s mg.mo matches 1 if score @s mg.mv matches 1 run function mg:master/say {t:"Sautez !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 1 if score @s mg.mv matches 0 run function mg:master/say {t:"Sautez !",m:""}
execute if score @s mg.mo matches 2 if score @s mg.mv matches 1 run function mg:master/say {t:"Accroupissez-vous !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 2 if score @s mg.mv matches 0 run function mg:master/say {t:"Accroupissez-vous !",m:""}
execute if score @s mg.mo matches 3 if score @s mg.mv matches 1 run function mg:master/say {t:"Sprintez !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 3 if score @s mg.mv matches 0 run function mg:master/say {t:"Sprintez !",m:""}
execute if score @s mg.mo matches 4 if score @s mg.mv matches 1 run function mg:master/say {t:"Regardez le ciel !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 5 if score @s mg.mv matches 1 run function mg:master/say {t:"Regardez le sol !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 6 if score @s mg.mv matches 1 run function mg:master/say {t:"Ne bougez plus !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 7 if score @s mg.mv matches 1 run function mg:master/say {t:"Sur le ROUGE !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 8 if score @s mg.mv matches 1 run function mg:master/say {t:"Sur le BLEU !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 9 if score @s mg.mv matches 1 run function mg:master/say {t:"Sur le VERT !",m:"👑 Master dit : "}
execute if score @s mg.mo matches 10 if score @s mg.mv matches 1 run function mg:master/say {t:"Sur le JAUNE !",m:"👑 Master dit : "}
