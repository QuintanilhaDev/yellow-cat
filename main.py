import git

repo = git.Repo('pythonSecJourney-https')
repo.remotes.origin.set_url('https://github.com/QuintanilhaDev/pythonSecJourney.git')

archieve = open("pythonSecJourney-https/bla.txt", "r+")
archieve.truncate(0)
archieve.write('Yellow cat is here!')

if repo.is_dirty(untracked_files=True):
    print('*' * 50)
    print('Meow! This repository have changes.🙀')
    print(repo.untracked_files)
    print('-' * 50)
    print(f'Remote name: {repo.remotes.origin.name}')
    print(f'Remote URL: {repo.remotes.origin.url}')
    print('\nI am pushing the changes for you, wait a moment... 😼')

    repo.index.add(repo.untracked_files)
    repo.index.commit('Yellow cat is working here...🐱')
    repo.git.push('--set-upstream', 'origin', 'main')


    print('Meow! All is done here, i will back to sleep😽')

else:
    print('Calm down, human... Have no changes here.😾')
