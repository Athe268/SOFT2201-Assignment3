from abc import ABC, abstractmethod


class Result:
    def __init__(self, question_id: str, earned: float, possible: float):
        self.question_id = question_id
        self.earned = earned
        self.possible = possible


class ResultSource(ABC):
    @abstractmethod
    def results(self) -> tuple[Result, ...]:
        pass


class NativeResults(ResultSource):
    def __init__(self, records: list[Result]):
        self.records = tuple(records)

    def results(self) -> tuple[Result, ...]:
        return self.records


class PercentageExport:
    def __init__(self, payload: dict):
        self.payload = payload

    def download(self) -> dict:
        return self.payload


class PercentageAdapter(ResultSource):
    def __init__(self, source: PercentageExport):
        self.source = source

    def results(self) -> tuple[Result, ...]:
        payload = self.source.download()
        output = []
        for question in payload['questions']:
            question_id = question['id']
            if question_id in payload['submissions']:
                earned = payload['submissions'][question_id] * question['weight'] / 100
            else:
                earned = 0
            output.append(Result(question_id, earned, question['weight']))
        return tuple(output)


def build_report(source: ResultSource) -> dict:
    records = source.results()
    earned = sum(record.earned for record in records)
    possible = sum(record.possible for record in records)
    if possible == 0:
        percentage = None
    else:
        percentage = earned * 100 / possible
    return {'earned': earned, 'possible': possible, 'percentage': percentage}
