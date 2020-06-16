class Time:
    def __init__(self, time: str):
        val = list(map(int, time.split(':')))
        self.hours = val[0]
        self.minutes = val[1]

    def get_hours(self):
        return self.hours

    def get_minutes(self):
        return self.minutes

    def __int__(self):
        return self.hours * 3600 + self.minutes * 60

    def __sub__(self, val):
        return int(self) - int(val)

    def __str__(self):
        return f"{self.hours} hours {self.minutes} minutes"


class Report:
    def __init__(self, name, speaker, duration, starts):
        self.name = name if isinstance(name, str) else None
        self.speaker = speaker if isinstance(speaker, str) else None
        self.duration = duration if isinstance(duration, Time) else None
        self.starts = starts if isinstance(starts, Time) else None

        if not (self.name and self.speaker and self.duration and self.starts):
            print("Something went wrong")

    def __str__(self):
        return f"{self.name} will begin through {self.starts}\n" + \
               f"Speaker – {self.speaker}" + '\n' + '-' * 30 + '\n'


def is_intersect(first: Report, second: Report):
    """ проверка, пересекаются ли два доклада по времени """
    lhs = min(first, second, key=lambda x: int(x.starts))
    rhs = max(first, second, key=lambda x: int(x.starts))
    if str(lhs.starts) == str(rhs.starts) or \
            int(lhs.starts) + int(lhs.duration) >= int(rhs.starts):
        return True
    return False


class Conferention:
    def __init__(self, name, starts, reports=[]):
        self.name = name if isinstance(name, str) else None
        self.starts = starts if isinstance(starts, Time) else None
        self.reports = []
        for i in reports:
            self.add_report(i)
        if not (self.name and self.reports and self.starts):
            print("Something went wrong")

    def add_report(self, report):
        """ дбавить доклад """
        if not isinstance(report, Report):
            print("Given wrong report")
            return

        # нельзя добавить пересекающийся с другими докладами доклад
        if any([is_intersect(i, report) for i in self.reports]) or \
                int(report.starts) < int(self.starts):
            print(f"Given in '{self.name}' conferention report '{report.name}' is wrong")
        else:
            print(f"Report '{report.name}' has been added to conferention '{self.name}'")
            self.reports.append(report)
        self.reports = list(sorted(self.reports, key=lambda x: x.starts.hours))

    def remove_report(self, report):
        """ удалить доклад """
        choice = input(f"Are you sure to remove '{report.name} from '{self.name}'? Answer yes or no")
        if 'yes' in choice:
            if report in self.reports:
                self.reports.remove(report)
                print(f"Report '{report.name}' have been removed")
            else:
                print(f"There is no '{report.name}' in '{self.name}'")
        elif 'no' in choice:
            print(f"'{report.name}' don't remove from '{self.name}'")
        else:
            print(f"Wrong answer – {choice}")

    def get_conferention_diration(self):
        """ получить продолжительность конференции """
        if len(self.reports) == 0:
            return
        val = (int(self.reports[-1].starts) + int(self.reports[-1].duration) -
               int(self.reports[0].starts))
        return f"{val // 3600} hours {val % 3600 // 60} minutes"

    def get_longest_pause(self):
        """ получить время самой долгой паузы """
        ret = []
        for i in range(1, len(self.reports)):
            ret += (int(self.reports[i].starts) - int(self.reports[i - 1].starts)
                    - int(self.reports[i - 1].duration))
        return max(ret) // 60

    def __str__(self):
        ret = '\n\n'
        for i in self.reports:
            ret += str(i) + '\n\n\n'
        return ret
