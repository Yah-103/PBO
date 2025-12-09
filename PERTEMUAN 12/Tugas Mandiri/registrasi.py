from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Set

# MODEL DATA
@dataclass
class TimeSlot:
    day: str
    start: int
    end: int

    def overlaps(self, other: "TimeSlot") -> bool:
        return self.day == other.day and self.start < other.end and other.start < self.end

@dataclass
class Course:
    code: str
    sks: int
    prerequisites: List[str]
    slots: List[TimeSlot]

@dataclass
class RegistrationData:
    student_name: str
    completed_courses: Set[str]
    requested_courses: List[Course]

# ABSTRAKSI RULE
class IValidationRule(ABC):
    @abstractmethod
    def validate(self, data: RegistrationData) -> bool:
        pass

    @property
    @abstractmethod
    def error_message(self) -> str:
        pass


# IMPLEMENTASI RULE
class SksLimitRule(IValidationRule):
    def __init__(self, max_sks: int):
        self.max_sks = max_sks
        self._error_message = ""

    @property
    def error_message(self) -> str:
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        total = sum(c.sks for c in data.requested_courses)
        if total > self.max_sks:
            self._error_message = f"Total SKS {total} melebihi batas {self.max_sks}."
            print(self._error_message)
            return False
        return True

class PrerequisiteRule(IValidationRule):
    def __init__(self):
        self._error_message = ""

    @property
    def error_message(self) -> str:
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        for course in data.requested_courses:
            for req in course.prerequisites:
                if req not in data.completed_courses:
                    self._error_message = f"Prasyarat {req} untuk {course.code} belum diambil."
                    print(self._error_message)
                    return False
        return True

class JadwalBentrokRule(IValidationRule):
    def __init__(self):
        self._error_message = ""

    @property
    def error_message(self) -> str:
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        courses = data.requested_courses
        for i in range(len(courses)):
            for j in range(i + 1, len(courses)):
                a = courses[i]
                b = courses[j]
                for sa in a.slots:
                    for sb in b.slots:
                        if sa.overlaps(sb):
                            self._error_message = (
                                f"Jadwal {a.code} dan {b.code} bentrok "
                                f"({sa.day} {sa.start}-{sa.end} vs {sb.start}-{sb.end})"
                            )
                            print(self._error_message)
                            return False
        return True


# REGISTRATION SERVICE
class RegistrationService:
    def __init__(self, rules: list[IValidationRule]):
        self.rules = rules

    def run_registration(self, data: RegistrationData) -> bool:
        print(f"\nMemulai registrasi untuk {data.student_name}")
        all_ok = True

        for rule in self.rules:
            if not rule.validate(data):
                all_ok = False

        if all_ok:
            print("Registrasi berhasil.")
        else:
            print("Registrasi gagal.")

        return all_ok


# PROGRAM UTAMA
if __name__ == "__main__":
    completed = {"IF101"}

    requested = [
        Course("IF201", 3, ["IF101"], [TimeSlot("Mon", 9, 11)]),
        Course("IF202", 3, ["IF102"], [TimeSlot("Mon", 10, 12)]),
    ]

    data = RegistrationData("Andi", completed, requested)

    rules = [
        SksLimitRule(24),
        PrerequisiteRule(),
        JadwalBentrokRule(),
    ]

    service = RegistrationService(rules)
    service.run_registration(data)