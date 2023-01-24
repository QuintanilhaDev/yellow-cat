import git
import os

repo = git.Repo('pythonSecJourney-https')
repo.remotes.origin.set_url('https://github.com/QuintanilhaDev/pythonSecJourney.git')
archive = open("pythonSecJourney-https/bla.txt", "r+")
archive.write('tag:1.0.8')


def push_changes(url, tag):

    if repo.is_dirty(untracked_files=True):
        print('*' * 50)
        print('Meow! This repository have changes.🙀')
        print(repo.untracked_files)
        print('-' * 50)
        print(f'Remote name: {repo.remotes.origin.name}')
        print(f'Remote URL: {repo.remotes.origin.url}')
        print('\nI am pushing the changes for you, wait a moment... 😼')
        repo.index.add(['bla.txt'])
        repo.index.commit('Yellow cat is working here...🐱')
        repo.git.push('-u', 'origin', 'main')


        print('Meow! All is done here, i will back to sleep😽')

    else:
        print('Calm down, human... Have no changes here.😾')


push_changes()
