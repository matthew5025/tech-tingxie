import click
import json
import os
import hashlib
import random
import time
random.seed(time.time())

data = dict()

if not os.path.isfile("notes.json"):
    # Initialise
    data['tags'] = []
    data['notes'] = []
    with open('notes.json', 'w') as f:
        json.dump(data, f)

else:
    with open('notes.json',) as f:
        data = json.load(f)


def rand_guid():
    return random.randint(0, 1 << 31)


@click.command()
def add():
    """Utility to help easily add words into JSON file."""
    note = dict()
    note['engWord'] = ''
    note['engWord'] = click.prompt('Input English word')
    note['chiWord'] = ''
    note['chiWord'] = click.prompt('Input Chinese translation')
    note['pinyin'] = ''
    note['pinyin'] = click.prompt('Input pinyin (Optional)', default='')
    note['engEg1'] = ''
    note['engEg1'] = click.prompt(
        'Input example English sentence (Optional)', default='')
    note['chiEg1'] = ''
    note['engEg2'] = ''
    note['chiEg2'] = ''
    note['comments'] = ''
    note['Guid'] = str(rand_guid())
    note['tags'] = []
    if note['engEg1']:
        note['chiEg1'] = click.prompt('Input Chinese translation.', default='')
        note['engEg2 '] = click.prompt(
            'Input another example English sentence (Optional)', default='')
        if note['engEg2']:
            note['chiEg2'] = click.prompt(
                'Input Chinese translation.', default='')
    while True:
        tag = click.prompt(
            'Input tag (press enter to stop inputting tags)', default='')
        if tag:
            tags.append(tag)
        else:
            break
    data['notes'].append(note)
    with open('notes.json', 'w') as f:
        json.dump(data, f)

    if click.confirm('Continue adding?', default='y', abort=True):
        click.echo("===============================")
        add()


if __name__ == '__main__':
    add()
