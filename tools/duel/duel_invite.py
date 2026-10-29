"""Duel sniper : liste des adversaires et invitations (défi, accepter, refuser, annuler, expirer), écrites par gen_duel.py.

Un défi = le défieur (tag mg.dlrq, numéro mg.dlid) pose sur l'invité mg.dlto = son numéro et mg.dlx = 600 ticks.
Tags temporaires : mg.dltg adversaire visé (challenge, expire, refuse), mg.dlt2 invité retrouvé par rq_check,
mg.dlca défieur retrouvé par accept / cancel, mg.dlq demandeur de la liste.
L'invité reçoit une fenêtre (dialog, inline : Accepter = trigger 2, Refuser = 3, Plus tard = 7) en plus d'une ligne de chat de secours
(la fenêtre se rouvre par le bouton [Répondre] = trigger 6) ; mg.dlui = fenêtre ouverte, fermée (dialog clear) à l'expiration,
au refus ou à l'annulation. Si une autre fenêtre la remplace (note de fin de partie mg.rate, invité devenu occupé), duel/tick retire
mg.dlui sans rien fermer (et fait expirer l'invitation d'un invité devenu occupé).
La déconnexion du défieur n'est pas détectée avant l'expiration : l'invité qui accepte entre-temps reçoit fail_gone.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'lib'))
import mcfn

INV = 600      # ticks de validité d'une invitation
js = mcfn.js


def tx(text, color='gray', **kw):
    return {'text': text, 'color': color, **kw}


def btn(label, color, n, hover):
    return {'text': label, 'color': color, 'bold': True,
            'click_event': {'action': 'run_command', 'command': f'trigger mg.duel set {n}'},
            'hover_event': {'action': 'show_text', 'value': hover}}


def sel(s, color='yellow', **kw):
    return {'selector': s, 'color': color, **kw}


def say(who, *parts):
    return f'tellraw {who} ' + js(list(parts))


def act(label, color, n):
    return {'label': {'text': label, 'color': color, 'bold': True},
            'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.duel set {n}'}}


# fenêtre d'invitation (inline : le pseudo du défieur est un trou de macro, remplacé par duel/inv_dlg)
DLG = {'type': 'minecraft:multi_action', 'title': {'text': '⚔ Duel sniper', 'color': 'gold', 'bold': True},
       'pause': False, 'can_close_with_escape': True, 'after_action': 'close', 'columns': 2,
       'body': [{'type': 'minecraft:plain_message', 'contents': [
           {'text': '@@p@@', 'color': 'yellow', 'bold': True},
           {'text': f' te défie en duel sniper 1v1 : premier à 3 manches. Invitation : {INV // 20} s au total.', 'color': 'gray'}]}],
       'actions': [act('✔ Accepter', 'green', 2), act('✘ Refuser', 'red', 3)],
       'exit_action': {'label': {'text': 'Plus tard', 'color': 'gray'},
                       'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.duel set 7'}}}
# fermeture de la fenêtre de @s si elle est ouverte (mg.dlui : on ne ferme pas la fenêtre d'une autre fonctionnalité)
CLOSE_DLG = ['execute if entity @s[tag=mg.dlui] run dialog clear @s', 'tag @s remove mg.dlui']


# @s a reçu une invitation : ligne de chat de secours + fenêtre rouverte (il doit répondre avant de défier)
PENDING = 'function mg:duel/pending'


# tags d'occupation (duel/busy, écrit par gen_duel.py ; spectateur et invitation en cours y sont testés à part)
BUSY = ['mg.play', 'mg.out', 'mg.surv', 'mg.inplot', 'mg.visit', 'mg.xso', 'mg.ely', 'mg.elyf', 'mg.pkr', 'mg.lk',
        'mg.mpp', 'mg.gtw', 'mg.tvw', 'mg.pvpc', 'mg.dl']
# occupés de la liste (duel/list_one) : première raison qui s'applique, dans cet ordre
BUSY_WHY = [
    ('tag=mg.mpp', 'en Mini Party'), ('tag=mg.play', 'en partie'), ('tag=mg.out', 'en partie'),
    ('tag=mg.gtw', 'dans GTA'), ('tag=mg.tvw', 'dans Terra Nova'), ('tag=mg.surv', 'en survie'),
    ('tag=mg.inplot', 'sur un plot'), ('tag=mg.visit', 'sur un plot'),
    ('tag=mg.ely', 'en course d\'élytres'), ('tag=mg.elyf', 'en course d\'élytres'),
    ('tag=mg.xso', 'en contre-la-montre'), ('tag=mg.pkr', 'en parcours'), ('tag=mg.lk', 'en kart'),
    ('tag=mg.pvpc', 'dans l\'arène PvP'), ('tag=mg.dl', 'en duel'), ('gamemode=spectator', 'spectateur'),
    ('tag=mg.dlrq', 'invitation en cours'), ('scores={mg.dlto=1..}', 'invitation en cours')]
BUSY_OTHER = 'occupé'
# chaque tag de BUSY a son libellé (même ensemble) : un tag ajouté à BUSY sans libellé fait échouer la génération
assert {c[4:] for c, _ in BUSY_WHY if c.startswith('tag=')} - {'mg.dlrq'} == set(BUSY), 'BUSY et BUSY_WHY divergent'


def busy_line(label):
    return say('@a[tag=mg.dlq]', tx('  ⚔ '), sel('@s', 'gray'), tx(' — ' + label))


def lists(w):
    w('duel/list', [
        '# Liste des adversaires (@s = joueur) : libres = lien cliquable (trigger mg.duel 1000 + id), occupés = ligne grise avec la raison (duel/list_one)',
        'function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return run ' + say('@s', tx('Tu ne peux pas défier maintenant (partie ou activité en cours).')),
        'execute if entity @s[tag=mg.dlrq] run return run ' + say('@s', tx('Tu as déjà une invitation en cours : '), btn('[Annuler]', 'red', 4, 'Annuler l\'invitation')),
        'execute if score @s mg.dlto matches 1.. run return run ' + PENDING,
        'execute unless data storage mg:duel {built:1b} run return run ' + say('@s', tx('Les arènes sont en construction, réessaie dans quelques minutes.')),
        say('@s', tx('— Duel sniper 1v1 : clique sur un adversaire —', 'gold')),
        'scoreboard players set $dlc mg.st 0',
        'tag @s add mg.dlq',
        'execute as @a[tag=!mg.dlq,tag=mg.init] run function mg:duel/list_one',
        'tag @s remove mg.dlq',
        'execute if score $dlc mg.st matches 0 run ' + say('@s', tx('Personne n\'est disponible pour un duel pour le moment.')),
    ])
    w('duel/list_one', [
        '# Un candidat (@s = joueur listé ; le demandeur porte mg.dlq) : occupé ? (ligne grise non cliquable + raison), sinon numéro et ligne cliquable',
        'function mg:duel/busy',
        *['execute if entity @s[' + cond + '] run return run ' + busy_line(label) for cond, label in BUSY_WHY],
        'execute if score $dlb mg.st matches 1 run return run ' + busy_line(BUSY_OTHER),
        'execute unless score @s mg.dlid matches 1.. run function mg:duel/new_id',
        'scoreboard players add $dlc mg.st 1',
        'scoreboard players operation #dll mg.st = @s mg.dlid',
        'scoreboard players add #dll mg.st 1000',
        'execute store result storage mg:duel m.v int 1 run scoreboard players get #dll mg.st',
        'function mg:duel/list_line with storage mg:duel m',
    ])
    w('duel/list_line', [
        '# Ligne de la liste (macro : $(v) = 1000 + id ; @s = joueur listé, destinataire = demandeur mg.dlq)',
        '$tellraw @a[tag=mg.dlq] ' + js([tx('  ⚔ ', 'red'),
                                        sel('@s', 'white', click_event={'action': 'run_command', 'command': 'trigger mg.duel set $(v)'},
                                            hover_event={'action': 'show_text', 'value': 'Défier ce joueur en duel sniper'}),
                                        tx('  ← clique pour défier')]),
    ])


def invitations(w):
    w('duel/challenge', [
        '# Défi (@s = défieur ; #dlv = 1000 + id de l\'adversaire)',
        'scoreboard players operation $dlt mg.st = #dlv mg.st',
        'scoreboard players remove $dlt mg.st 1000',
        'execute as @a if score @s mg.dlid = $dlt mg.st run tag @s add mg.dltg',
        'function mg:duel/challenge_chk',
        'tag @a remove mg.dltg',
    ])
    w('duel/challenge_chk', [
        '# Contrôles puis invitation (@s = défieur ; l\'adversaire porte mg.dltg)',
        'execute if entity @s[tag=mg.dlrq] run function mg:duel/rq_check',
        'execute if entity @s[tag=mg.dlrq] run return run ' + say('@s', tx('Tu as déjà une invitation en cours : '), btn('[Annuler]', 'red', 4, 'Annuler l\'invitation')),
        'execute if score @s mg.dlto matches 1.. run return run ' + PENDING,
        'function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return run ' + say('@s', tx('Tu ne peux pas défier maintenant (partie ou activité en cours).')),
        'execute unless entity @a[tag=mg.dltg] run return run ' + say('@s', tx('Ce joueur n\'est plus là.')),
        'execute if entity @s[tag=mg.dltg] run return run ' + say('@s', tx('Tu ne peux pas te défier toi-même.')),
        'execute as @a[tag=mg.dltg,limit=1] run function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run return run ' + say('@s', sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' est occupé (partie ou activité en cours).')),
        'execute if entity @a[tag=mg.dltg,tag=mg.dlrq] run return run ' + say('@s', sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' a déjà une invitation en cours.')),
        'execute if entity @a[tag=mg.dltg,scores={mg.dlto=1..}] run return run ' + say('@s', sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' a déjà reçu une invitation.')),
        'function mg:duel/pick',
        'execute if score $dli mg.st matches 0 run return run ' + say('@s', tx('Aucune arène n\'est libre pour le moment (ou elles sont en construction).')),
        'execute unless score @s mg.dlid matches 1.. run function mg:duel/new_id',
        'scoreboard players operation @a[tag=mg.dltg,limit=1] mg.dlto = @s mg.dlid',
        f'scoreboard players set @a[tag=mg.dltg,limit=1] mg.dlx {INV}',
        'tag @s add mg.dlrq',
        say('@a[tag=mg.dltg,limit=1]', sel('@s', 'yellow', bold=True), tx(' te défie en duel sniper 1v1 (30 s) : '),
            btn('[✔ Accepter]', 'green', 2, 'Relever le défi'), tx(' '), btn('[✘ Refuser]', 'red', 3, 'Refuser le défi'),
            tx(' '), btn('[Répondre]', 'gold', 6, 'Rouvrir la fenêtre')),
        '# pas de fenêtre d\'office pendant la note de fin de partie (mg.rate) : la ligne de chat et [Répondre] suffisent',
        'execute as @a[tag=mg.dltg,tag=!mg.rate,limit=1] run function mg:duel/inv_show',
        say('@s', tx('⚔ Défi envoyé à '), sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' (30 s) '), btn('[Annuler]', 'red', 4, 'Annuler l\'invitation')),
    ])
    w('duel/pending', [
        '# Invitation déjà reçue (@s = invité) : ligne de chat de secours, puis la fenêtre est rouverte',
        say('@s', tx('Tu as reçu une invitation de duel : '), btn('[✔ Accepter]', 'green', 2, 'Relever le défi'),
            tx(' '), btn('[✘ Refuser]', 'red', 3, 'Refuser le défi'), tx(' avant d\'en lancer une.')),
        'function mg:duel/inv_show',
    ])
    w('duel/inv_busy', [
        '# Invité en attente (@s, appelé chaque tick par duel/tick) : devenu occupé, son invitation expire ;',
        '# sa fenêtre a été remplacée par une autre : mg.dlui est retiré sans dialog clear',
        'function mg:duel/busy',
        'execute if score $dlb mg.st matches 1 run tag @s remove mg.dlui',
        'execute if score $dlb mg.st matches 1 run function mg:duel/expire',
    ])
    w('duel/inv_show', [
        '# Ouvre (ou rouvre) la fenêtre d\'invitation (@s = invité) ; le pseudo du défieur vient de duel/inv_name (repli : « Un joueur »)',
        'execute unless score @s mg.dlto matches 1.. run return 0',
        'data modify storage mg:duel inv set value {p:"Un joueur"}',
        'scoreboard players operation #dln mg.st = @s mg.dlto',
        'execute as @a[tag=mg.dlrq] if score @s mg.dlid = #dln mg.st at @s run function mg:duel/inv_name',
        'tag @s add mg.dlui',
        'function mg:duel/inv_dlg with storage mg:duel inv',
    ])
    w('duel/inv_name', [
        '# Pseudo du défieur (@s = défieur, à sa position) -> mg:duel inv.p : lu sur sa tête (loot mg:plot_head), comme kart/cam_new',
        'summon minecraft:item_display ~ ~ ~ {Tags:["mg.dlnm"]}',
        'loot replace entity @e[type=minecraft:item_display,tag=mg.dlnm,limit=1] contents loot mg:plot_head',
        'data modify storage mg:duel inv.p set from entity @e[type=minecraft:item_display,tag=mg.dlnm,limit=1] item.components."minecraft:profile".name',
        'kill @e[type=minecraft:item_display,tag=mg.dlnm]',
    ])
    w('duel/inv_dlg', ['# Fenêtre d\'invitation (macro : $(p) = pseudo du défieur)',
                       '$dialog show @s ' + js(DLG).replace('@@p@@', '$(p)')])
    w('duel/cancel', [
        '# Annuler son invitation (@s = défieur) ; ignoré pendant un duel (bouton périmé : l\'abandon est le trigger 5)',
        'execute if entity @s[tag=mg.dl] run return 0',
        'execute unless entity @s[tag=mg.dlrq] run return run ' + say('@s', tx('Tu n\'as aucune invitation à annuler.')),
        'scoreboard players operation $dlt mg.st = @s mg.dlid',
        'tag @s add mg.dlca',
        'execute as @a[scores={mg.dlto=1..}] if score @s mg.dlto = $dlt mg.st run function mg:duel/cancel_t',
        'tag @s remove mg.dlca',
        'tag @s remove mg.dlrq',
        say('@s', tx('⚔ Invitation annulée.')),
    ])
    w('duel/cancel_t', [
        '# L\'invité apprend l\'annulation (@s = invité ; le défieur porte mg.dlca)',
        say('@s', sel('@a[tag=mg.dlca,limit=1]', 'white'), tx(' a annulé son invitation au duel.')),
        *CLOSE_DLG,
        'scoreboard players reset @s mg.dlto',
        'scoreboard players reset @s mg.dlx',
    ])
    w('duel/rq_check', [
        '# Le défieur (@s, tag mg.dlrq) a-t-il encore un invité en ligne ? Sinon l\'invitation est périmée',
        'scoreboard players operation $dlt mg.st = @s mg.dlid',
        'execute as @a[scores={mg.dlto=1..}] if score @s mg.dlto = $dlt mg.st run tag @s add mg.dlt2',
        'execute unless entity @a[tag=mg.dlt2] run ' + say('@s', tx('⚔ Invitation annulée : l\'invité s\'est déconnecté.')),
        'execute unless entity @a[tag=mg.dlt2] run tag @s remove mg.dlrq',
        'tag @a remove mg.dlt2',
    ])
    for name, k, to_t, to_c in (
            ('expire', 1, tx('⚔ L\'invitation au duel a expiré.'), [sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' n\'a pas répondu : invitation expirée.')]),
            ('refuse', 2, tx('⚔ Tu as refusé le duel.'), [sel('@a[tag=mg.dltg,limit=1]', 'white'), tx(' a refusé ton duel.')])):
        w(f'duel/{name}', [
            f'# Invitation {"expirée" if k == 1 else "refusée"} (@s = invité)',
            'execute unless score @s mg.dlto matches 1.. run return run ' + say('@s', tx('Tu n\'as aucune invitation de duel en attente.')),
            'scoreboard players operation $dlt mg.st = @s mg.dlto',
            'tag @s add mg.dltg',
            'execute as @a[tag=mg.dlrq] if score @s mg.dlid = $dlt mg.st run function mg:duel/' + name + '_c',
            'tag @s remove mg.dltg',
            say('@s', to_t),
            *CLOSE_DLG,
            'scoreboard players reset @s mg.dlto',
            'scoreboard players reset @s mg.dlx',
        ])
        w(f'duel/{name}_c', ['# (@s = défieur ; l\'invité porte mg.dltg)', 'tag @s remove mg.dlrq', say('@s', *to_c)])
