import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Set

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)
logger = logging.getLogger(__name__)

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

class IValidationRule(ABC):
    @abstractmethod
    def validate(self, data: RegistrationData) -> bool:
        pass

    @property
    @abstractmethod
    def error_message(self) -> str:
        pass

class SksLimitRule(IValidationRule):
    def __init__(self, max_sks: int):
        self.max_sks = max_sks
        self._error_message = ""

    @property
    def error_message(self) -> str:
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        total = sum(c.sks for c in data.requested_courses)
        logger.info("Validasi SKS: %s", total)
        if total > self.max_sks:
            self._error_message = f"Total SKS {total} melebihi batas {self.max_sks}."
            logger.warning(self._error_message)
            return False
        return True

class PrerequisiteRule(IValidationRule):
    def __init__(self):
        self._error_message = ""

    @property
    def error_message(self) -> str:
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        logger.info("Validasi prasyarat")
        for course in data.requested_courses:
            for req in course.prerequisites:
                if req not in data.completed_courses:
                    self._error_message = f"Prasyarat {req} untuk {course.code} belum diambil."
                    logger.warning(self._error_message)
                    return False
        return True

class JadwalBentrokRule(IValidationRule):
    def __init__(self):
        self._error_message = ""

    @property
    def error_message(self) -> str:
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        logger.info("Validasi jadwal")
        courses = data.requested_courses
        for i in range(len(courses)):
            for j in range(i + 1, len(courses)):
                a = courses[i]
                b = courses[j]
                for sa in a.slots:
                    for sb in b.slots:
                        if sa.overlaps(sb):
                            self._error_message = f"Jadwal {a.code} dan {b.code} bentrok."
                            logger.warning(self._error_message)
                            return False
        return True

class RegistrationService:
    def __init__(self, rules: list[IValidationRule]):
        self.rules = rules
        self._logger = logging.getLogger(self.__class__.__name__)

    def run_registration(self, data: RegistrationData) -> bool:
        self._logger.info("Memulai registrasi untuk %s", data.student_name)
        all_ok = True

        for rule in self.rules:
            self._logger.info("Menjalankan rule: %s", rule.__class__.__name__)
            if not rule.validate(data):
                all_ok = False
                self._logger.warning("Validasi gagal: %s", rule.error_message)

        if all_ok:
            self._logger.info("Registrasi berhasil")
        else:
            self._logger.warning("Registrasi gagal")

        return all_ok

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