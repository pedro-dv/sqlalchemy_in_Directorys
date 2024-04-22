from infra.repository.filmesRepository import Filmes_Repository

repo = Filmes_Repository()

repo.insert('mmmmm', 'comedia', 2010)

repo.delete('batman 2')

data = repo.select()

print(data)
