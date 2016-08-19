#!/usr/bin/python

import lingualeo
import random
import requests
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-ns', action='store_true', help='Play no sound')
parser.add_argument('-np', action='store_true', help='Show no picture')
parser.add_argument('-ne', action='store_true', help='Show no example')

MEDIA_DIR = os.path.abspath(os.path.join(os.path.curdir, 'media'))


def random_word(words):
    l = [words]
    page = 2
    while words['show_more']:
        words = lingualeo.user_dict(page=page)
        l.append(words)
        page += 1
    p = random.choice(l)
    g = random.choice(p['userdict3'])
    return random.choice(g['words'])


def word_count(response):
    return reduce(lambda x, y: x + y,
                  map(lambda x: x['count'], response['userdict3']))


def ensure_media_dir():
    if not os.path.exists(MEDIA_DIR):
        os.mkdir(MEDIA_DIR)


def save_file(url, filename):
    ensure_media_dir()
    path = os.path.join(MEDIA_DIR, filename)
    if os.path.isfile(path):
        return
    r = requests.get(url, stream=True)
    r.raise_for_status()
    with open(path, "wb") as f:
        for chunk in r:
            f.write(chunk)


def process_picture(word, translate_variant):
    if not args.np:
        picture_url = 'https:' + word['user_translates'][translate_variant]['picture_url']
        picture_filename = picture_url.split('/')[-1]
        save_file(picture_url, picture_filename)
        return picture_filename


def process_sound(word):
    if not args.ns:
        sound_url = word['sound_url']
        sound_filename = sound_url.split('/')[-1]
        save_file(sound_url, sound_filename)
        return sound_filename


if __name__ == '__main__':
    args = parser.parse_args()

    with open('credentials.txt', 'r') as c:
        cred = c.readlines()
        lingualeo.auth(cred[0], cred[1])
    words = lingualeo.user_dict()
    word = random_word(words)

    translate_variant = random.randint(0, len(word['user_translates']) - 1)
    title = '%s [%s] %s' % (word['word_value'],
                            word['transcription'],
                            word['user_translates'][translate_variant]['translate_value'])
    if not args.ne:
        message = random.choice(word['context'].split('|'))
    else:
        message = ''

    picture_filename = process_picture(word, translate_variant)
    if not args.np:
        picture = '-i ' + os.path.join(MEDIA_DIR, picture_filename)
    else:
        picture = ''

    cmd = 'notify-send "%s" "%s" %s' % (title, message, picture)
    os.system(cmd.encode('utf-8'))

    sound_filename = process_sound(word)
    if not args.ns:
        sound = os.path.join(os.path.abspath(os.path.curdir), 'media', sound_filename)
        os.system('mpg123 %s' % sound)