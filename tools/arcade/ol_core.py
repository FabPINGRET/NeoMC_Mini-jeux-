"""🌙 Ombrelune : outils partagés par les modules du RPG (écriture, textes, dialogues, objets, bits).

Conventions :
  fonctions mg:ombre/…, dimension mg:ombrelune, stockage mg:ombre, scores mg.ol…,
  joueurs : tag mg.olw (dans le monde) + mg.surv ; entités de la session : tag mg.ol (retirées à la fin).
"""
import json
import os

import common as C

DIM = 'mg:ombrelune'
P = 'ombre'
ST = 'mg:ombre'
WF = 'minecraft:warped_fungus_on_a_stick'
TR = 'transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[%sf,%sf,%sf],scale:[%sf,%sf,%sf]}'
js = C.js


def w(rel, lines):
    C.w(f'{P}/{rel}', lines)


def fn(rel):
    return f'function mg:{P}/{rel}'


def TEXT(t, c='gray', **k):
    d = {'text': t, 'color': c}
    d.update(k)
    return d


def nm(t, c, bold=True):
    return js({'text': t, 'color': c, 'italic': False, 'bold': bold})


def lo(*ls):
    return '[' + ','.join(js({'text': l, 'color': 'gray', 'italic': False}) for l in ls) + ']'


def wjson(rel, obj):
    p = os.path.join(C.D, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write('\n')


def bit_test(score, i, who='@s'):
    """Lignes : $b = bit i du score (0/1). Constantes #p<i> posées par ombre/consts."""
    return [f'scoreboard players operation $b mg.st = {who} {score}', f'scoreboard players operation $b mg.st /= #p{i} mg.st',
            'scoreboard players operation $b mg.st %= #2 mg.st']


def bit_set(score, i, who='@s'):
    """Lignes : pose le bit i (sans effet s'il l'est déjà)."""
    return bit_test(score, i, who) + [f'execute if score $b mg.st matches 0 run scoreboard players operation {who} {score} += #p{i} mg.st']


def say(msg, col='gray'):
    return ['scoreboard players set @s mg.olal 40', f'title @s actionbar {js(TEXT(msg, col))}']


# ---------------------------------------------------------------- dialogues (fenêtre, sinon texte + liens dans le chat)
def dlg(title, col, text, buttons, close=True, body2=None):
    acts = [{'label': [TEXT(l, c, bold=True)], 'tooltip': [TEXT(t, 'gray')], 'action': {'type': 'minecraft:run_command', 'command': f'trigger mg.oltk set {v}'}}
            for (l, c, t, v) in buttons]
    if close:
        acts.append({'label': [TEXT('Au revoir', 'gray')], 'tooltip': [TEXT('Fermer', 'gray')],
                     'action': {'type': 'minecraft:run_command', 'command': 'trigger mg.oltk set 8'}})
    body = [{'type': 'minecraft:plain_message', 'contents': [TEXT(text, 'white')], 'width': 320}]
    if body2:
        body.append({'type': 'minecraft:plain_message', 'contents': [TEXT(body2, 'gray')], 'width': 320})
    return {'type': 'minecraft:multi_action', 'title': TEXT(title, col, bold=True), 'external_title': TEXT(title, col), 'pause': False,
            'can_close_with_escape': True, 'columns': 1, 'body': body, 'actions': acts}


def show(d):
    links = [TEXT(d['title']['text'] + ' : ', d['title']['color'], bold=True), TEXT(d['body'][0]['contents'][0]['text'] + ' ', 'gray')]
    for a in d['actions']:
        links.append({'text': f'[{a["label"][0]["text"]}] ', 'color': a['label'][0]['color'], 'bold': False,
                      'click_event': {'action': 'run_command', 'command': '/' + a['action']['command']}})
    return ['scoreboard players enable @s mg.oltk', 'scoreboard players set $dlg mg.st 0',
            f'execute store success score $dlg mg.st run dialog show @s {js(d)}', 'execute unless score $dlg mg.st matches 1 run tellraw @s ' + js(links)]


def tdisp(x, y, z, text, scale=1.0, bg=1140850688, tags='"mg.ol"', extra=''):
    return (f'summon minecraft:text_display {x} {y} {z} {{Tags:[{tags}],billboard:"vertical",text:{js(text)},background:{bg},'
            f'{TR % (0, 0, 0, scale, scale, scale)}{extra}}}')


def gain(gold=0, xp=0, why='', col='green'):
    L = []
    if gold:
        L.append(f'scoreboard players add @s mg.olg {gold}')
    if xp:
        L.append(f'function mg:{P}/xp {{n:{xp}}}')
    if why:
        L += ['scoreboard players set @s mg.olal 40',
              'title @s actionbar ' + js([TEXT(f'+{gold} 💰 ' if gold else '', 'gold', bold=True), TEXT(why, 'gray')])]
    return L
