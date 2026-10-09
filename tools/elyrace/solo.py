"""Contre-la-montre solo de la Course d'elytres : tout joueur (admin ou non) peut lancer seul un parcours quand aucune partie ne
tourne. Acces par le trigger mg.xs (menus.SOLO_*), jamais par mg.go (reserve aux admins). Le solo occupe $game 66 et $state comme
une course de groupe, avec le drapeau $xs = 1 : build_wait se met donc en pause, et end / timeout / draw / finish / cleanup lisent
$xs. Fin sans victoire ni match nul ; le temps vient du chrono $xt (records.py). $xse = tick de la fin du dernier solo (delai de 30 s).
Fonctions generees : elyrace/solo/{cmd, start, announce, countdown, quit, end, menu} et elyrace/draw.
Branchements dans le moteur (core/tick, countdown, begin, reconnect) : wire_elyrace3.py.
Python stdlib uniquement (compatible 3.8).
"""
import menus as M

COOLDOWN = 600           # ticks (30 s) apres la fin du dernier solo, quel que soit le joueur (delai global, $xse) ; admins exemptes
COUNT = 100              # compte a rebours : 5 s
END_TIMER = 30           # ticks entre la fin et le retour au lobby : moins de 40, donc aucun son de fin de partie (core/ending joue a 100, 80, 60, 40)
ACTIVITY_TAGS = ('mg.ely', 'mg.elyf', 'mg.lk', 'mg.pkr')    # parcours d'elytra, elytres libres, kart libre, parkour du lobby
QUIT_LINK = ('{"text":"[✖ Abandonner]","color":"red","click_event":{"action":"run_command","command":"trigger mg.xs set %d"},'
             '"hover_event":{"action":"show_text","value":"Quitter le contre-la-montre"}}' % M.SOLO_QUIT)


def refuse(cond, text):
    """Refus : message au demandeur puis fin de la fonction, sans effet de bord."""
    return 'execute %s run return run tellraw @s [{"text":"⚠ ","color":"red"},{"text":"%s","color":"red"}]' % (cond, text)


def cmd_lines():
    return ['# @s = joueur qui a utilise /trigger mg.xs : %d = fenêtre, %d = abandon, %d = ses records, %d = solo au hasard, %d + NUM = solo sur le parcours NUM'
            % (M.SOLO_MENU, M.SOLO_QUIT, M.SOLO_RECORDS, M.SOLO_RANDOM, M.SOLO_RANDOM),
            '# la valeur est lue dans #xv, puis le trigger est remis à zéro d\'abord (core/tick le réactive à chaque tick)',
            'scoreboard players operation #xv mg.st = @s mg.xs',
            'scoreboard players reset @s mg.xs',
            'execute if score #xv mg.st matches %d run function mg:elyrace/solo/menu' % M.SOLO_MENU,
            'execute if score #xv mg.st matches %d run function mg:elyrace/solo/quit' % M.SOLO_QUIT,
            'execute if score #xv mg.st matches %d run function mg:elyrace/records' % M.SOLO_RECORDS,
            'execute if score #xv mg.st matches %d.. run function mg:elyrace/solo/start' % M.SOLO_RANDOM]


def checks_lines(specs):
    """Refus dans l'ordre : installation, joueur, partie en cours, delai, puis parcours construit (le seul qui touche a $xc)."""
    out = [refuse('unless score $setup mg.st matches 1', 'Installation manquante : un OP doit d\'abord lancer /function mg:setup.'),
           refuse('unless entity @s[tag=mg.init]', 'Pas encore prêt : réessaie dans un instant.'),
           refuse('if entity @s[tag=mg.surv]', 'Impossible depuis la survie : reviens d\'abord au lobby (/trigger mg.sv set 2).'),
           refuse('if entity @s[tag=mg.spectate]', 'Impossible en mode spectateur : repasse en joueur (/trigger mg.opt set 1).')]
    out += [refuse('if entity @s[tag=%s]' % t, 'Termine d\'abord ton activité en cours (parcours d\'élytra, élytres libres, kart libre ou parkour).') for t in ACTIVITY_TAGS]
    out += [refuse('unless score $state mg.st matches 0', 'Une partie est déjà en cours : attends sa fin.'),
            refuse('if score $mp mg.st matches 1', 'La Mini Party est en cours.'),
            refuse('if score $vat mg.st matches 1..', 'Un vote est sur le point de lancer un jeu : attends-le.'),
            '# délai depuis la fin du dernier solo ($xse, en ticks de $tc) : #xd = ticks écoulés (600 = pas d\'attente) ; les admins en sont exemptés',
            'scoreboard players set #xd mg.st %d' % COOLDOWN,
            'execute if score $xse mg.st matches 1.. run scoreboard players operation #xd mg.st = $tc mg.st',
            'execute if score $xse mg.st matches 1.. run scoreboard players operation #xd mg.st -= $xse mg.st',
            'scoreboard players set #xr mg.st %d' % COOLDOWN,
            'scoreboard players operation #xr mg.st -= #xd mg.st',
            'scoreboard players operation #xr mg.st /= #k20 mg.st',
            'scoreboard players add #xr mg.st 1',
            'execute unless entity @s[tag=mg.admin] if score #xd mg.st matches 0..%d run return run tellraw @s '
            '[{"text":"⚠ Attends encore ","color":"red"},{"score":{"name":"#xr","objective":"mg.st"},"color":"red"},{"text":" s avant un nouveau solo.","color":"red"}]' % (COOLDOWN - 1),
            '# parcours : #xv = 10 (au hasard, tiré parmi les construits par pick) ou 10 + NUM ; refusé s\'il n\'est pas construit',
            'scoreboard players set $xc mg.st 0',
            'execute if score #xv mg.st matches %d.. run scoreboard players operation $xc mg.st = #xv mg.st' % (M.SOLO_RANDOM + 1),
            'execute if score #xv mg.st matches %d.. run scoreboard players remove $xc mg.st %d' % (M.SOLO_RANDOM + 1, M.SOLO_RANDOM),
            'execute if score $xc mg.st matches 0 run function mg:elyrace/pick',
            refuse('if score $xc mg.st matches 0', 'Aucun parcours n\'est construit pour le moment : réessaie plus tard.')]
    out += [refuse('if score $xc mg.st matches %d unless data storage mg:elyrace %s' % (s.NUM, s.FLAG),
                   'Le parcours %d (%s) n\'est pas encore construit : réessaie plus tard.' % (s.NUM, s.NAME)) for s in specs]
    return out


def start_lines(specs):
    top = M.SOLO_RANDOM + len(specs)
    out = ['# @s = joueur qui lance un contre-la-montre solo (#xv = %d : parcours au hasard, %d + NUM : parcours NUM). Le lancement minimal de core/request :' % (M.SOLO_RANDOM, M.SOLO_RANDOM),
           '# ni vote effacé, ni objets retirés aux autres, ni annonce de jeu ; seul @s est participant',
           'execute unless score #xv mg.st matches %d..%d run return 0' % (M.SOLO_RANDOM, top)]
    out += checks_lines(specs)
    out += ['# lancement : $xs avant $state (les gardes de end, timeout, draw, finish et cleanup lisent $xs)',
            'scoreboard players set $xs mg.st 1',
            'scoreboard players set $game mg.st 66',
            'scoreboard players set $ar mg.st 0',
            'tag @s add mg.play',
            'tag @a remove mg.out',
            'tag @a remove mg.win',
            'scoreboard players set $n0 mg.st 1',
            'execute if entity @s[tag=mg.inplot] run function mg:plot/leave_game',
            'execute if entity @s[tag=mg.visit] run function mg:plot/leave_game',
            'scoreboard players set $state mg.st 1',
            'scoreboard players set $timer mg.st %d' % COUNT,
            'scoreboard players set @s mg.deaths 0',
            'scoreboard players reset @s mg.qs', 'scoreboard players reset @s mg.fw', 'scoreboard players reset @s mg.wc',
            'scoreboard players reset @s mg.wd', 'scoreboard players reset @s mg.us',
            'function mg:elyrace/solo/announce',
            'function mg:elyrace/prepare',
            '# prepare a annulé (parcours pas construit : CANCEL → elyrace/draw → solo/end) : pas de gel ni de titre',
            'execute if score $state mg.st matches 3 run return 0',
            'function mg:core/freeze',
            'effect give @s minecraft:resistance 7 255 true',
            'title @s title [{"text":"Prépare-toi !","color":"gold"}]',
            'title @s subtitle [{"text":"Début dans 5 secondes...","color":"gray"}]',
            'execute at @s run playsound minecraft:block.note_block.pling master @s ~ ~ ~ 1 0.8']
    return out


def announce_lines(specs):
    head = ('tellraw @a [{"selector":"@s","color":"yellow"},{"text":" lance un ","color":"gray"},{"text":"⏱ CONTRE-LA-MONTRE","color":"aqua","bold":true},'
            '{"text":" solo : %s","color":"gray"}]')
    out = ['# Annonce du solo (@s = joueur ; le parcours $xc est déjà tiré) et lien d\'abandon pour lui seul']
    out += ['execute if score $xc mg.st matches %d run %s' % (s.NUM, head % ('%s (%d anneaux) !' % (s.NAME, len(s.RINGS)))) for s in specs]
    out.append('tellraw @s [{"text":"⏱ Seul en piste : ton meilleur temps est enregistré. ","color":"gray"},%s]' % QUIT_LINK)
    return out


def countdown_lines():
    out = ['# Compte à rebours du solo (état 1, appelé par core/countdown) : titres et sons pour le joueur seulement',
           '# déconnexion pendant le compte à rebours : fin immédiate',
           'execute unless entity @a[tag=mg.play] run return run function mg:elyrace/solo/end',
           'scoreboard players remove $timer mg.st 1']
    for t, n, col, pitch in ((80, 4, 'yellow', '1'), (60, 3, 'gold', '1.2'), (40, 2, 'red', '1.4'), (20, 1, 'dark_red', '1.6')):
        out.append('execute if score $timer mg.st matches %d run title @a[tag=mg.play] title [{"text":"%d","color":"%s","bold":true}]' % (t, n, col))
        out.append('execute if score $timer mg.st matches %d as @a[tag=mg.play] at @s run playsound minecraft:block.note_block.hat master @s ~ ~ ~ 1 %s' % (t, pitch))
    return out + ['execute if score $timer mg.st matches ..0 run function mg:core/begin']


def quit_lines():
    return ['# @s = joueur qui abandonne (mg.xs %d, lien du message de lancement)' % M.SOLO_QUIT,
            'execute unless score $xs mg.st matches 1 run return run tellraw @s [{"text":"⚠ Aucun contre-la-montre en cours.","color":"red"}]',
            'execute unless entity @s[tag=mg.play] run return run tellraw @s [{"text":"⚠ Ce n\'est pas ton contre-la-montre.","color":"red"}]',
            'execute unless score $state mg.st matches 1..2 run return 0',
            'tellraw @a [{"selector":"@s","color":"yellow"},{"text":" abandonne le contre-la-montre.","color":"gray"}]',
            'function mg:elyrace/solo/end']


def end_lines():
    return ['# Fin du contre-la-montre (appelé par end, timeout et draw quand $xs vaut 1) : ni victoire ni match nul ; retour au lobby par core/ending',
            '# (return_lobby appelle elyrace/cleanup, qui note $xse et remet $xs à 0). L\'arrivée a déjà été annoncée par finish.',
            'execute unless entity @a[tag=mg.play,scores={mg.xf=1..}] run tellraw @a [{"text":"⏱ Contre-la-montre terminé sans arrivée.","color":"gray"}]',
            'scoreboard players set $state mg.st 3',
            'scoreboard players set $timer mg.st %d' % END_TIMER]


def draw_lines():
    return ['# Fin sans vainqueur de la Course d\'élytres (plus de participant, partie annulée) : en solo, fin du contre-la-montre ; sinon le match nul habituel',
            'execute if score $xs mg.st matches 1 run return run function mg:elyrace/solo/end',
            'function mg:core/draw']


def menu_lines(specs):
    return (['# @s = joueur : fenêtre du contre-la-montre solo (ouverte à tous), sinon menu texte',
             'scoreboard players set $dlg mg.st 0',
             'execute store success score $dlg mg.st run dialog show @s mg:sub_elyrace_solo',
             'execute if score $dlg mg.st matches 1 run return 0']
            + M.solo_text_lines(specs)
            + ['tellraw @s ["",{"text":" [« Retour]","color":"yellow","click_event":{"action":"run_command","command":"%s"}}]' % M.SOLO_BACK_MENU])


def functions(specs):
    return {'draw': draw_lines(), 'solo/cmd': cmd_lines(), 'solo/start': start_lines(specs), 'solo/announce': announce_lines(specs),
            'solo/countdown': countdown_lines(), 'solo/quit': quit_lines(), 'solo/end': end_lines(), 'solo/menu': menu_lines(specs)}
