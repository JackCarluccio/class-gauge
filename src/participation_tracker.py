import requests

participation_scores = {}


def set_participation_score(name, score):
    if not participation_scores.get(name):
        requests.post('http://127.0.0.1:5000/addPerson', json={'name': name, 'questionsAnswered': score})
    
    participation_scores[name] = score
    requests.post('http://127.0.0.1:5000/updateScore', json={'name': name, 'questionsAnswered': score})


def increment_participation_score(name):
    set_participation_score(name, participation_scores.get(name, 0) + 1)
