class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, vote):
        self.votes += vote
        return self


class Election:
    def __init__(self, candidates):
        self.candidates = candidates

    def _get_winner(self):
        votes = [candidate.votes for candidate in self.candidates]
        total = sum(votes)
        maximum_vote = max(votes)
        for candidate in self.candidates:
            if candidate.votes == maximum_vote:
                print(f"{candidate.name} won: {((candidate.votes/total)*100):.1f}% of votes")
                return

    def results(self):
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")
        print()
        self._get_winner()


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()