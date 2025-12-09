from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Set

@dataclass
class TimeSlot:
    """Representasi waktu jadwal mata kuliah."""
    day: str
    start: int
    end: int

    def overlaps(self, other: "TimeSlot") -> bool:
        """Mengecek apakah dua jadwal saling bertabrakan."""
        return self.day == other.day and self.start < other.end and other.start < self.end

@dataclass
class Course:
    """Representasi mata kuliah."""
    code: str
    sks: int
    prerequisites: List[str]
    slots: List[TimeSlot]

@dataclass
class RegistrationData:
    """Data registrasi mahasiswa."""
    student_name: str
    completed_courses: Set[str]
    requested_courses: List[Course]

class IValidationRule(ABC):
    """Interface untuk semua rule validasi."""

    @abstractmethod
    def validate(self, data: RegistrationData) -> bool:
        """Menjalankan proses validasi."""
        pass

    @property
    @abstractmethod
    def error_message(self) -> str:
        """Mengembalikan pesan error jika validasi gagal."""
        pass

class SksLimitRule(IValidationRule):
    """Rule untuk memvalidasi batas maksimum SKS."""

    def __init__(self, max_sks: int):
        """Inisialisasi dengan batas maksimum SKS."""
        self.max_sks = max_sks
        self._error_message = ""

    @property
    def error_message(self) -> str:
        """Pesan kesalahan validasi."""
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        """Validasi total SKS."""
        total = sum(c.sks for c in data.requested_courses)
        if total > self.max_sks:
            self._error_message = f"Total SKS {total} melebihi batas {self.max_sks}."
            print(self._error_message)
            return False
        return True

class PrerequisiteRule(IValidationRule):
    """Rule untuk memvalidasi prasyarat mata kuliah."""

    def __init__(self):
        """Inisialisasi rule prasyarat."""
        self._error_message = ""

    @property
    def error_message(self) -> str:
        """Pesan error validasi."""
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        """Validasi prasyarat."""
        for course in data.requested_courses:
            for req in course.prerequisites:
                if req not in data.completed_courses:
                    self._error_message = f"Prasyarat {req} untuk {course.code} belum diambil."
                    print(self._error_message)
                    return False
        return True

class JadwalBentrokRule(IValidationRule):
    """Rule untuk memvalidasi bentrok jadwal."""

    def __init__(self):
        """Inisialisasi rule jadwal."""
        self._error_message = ""

    @property
    def error_message(self) -> str:
        """Pesan error jadwal."""
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        """Validasi jadwal bentrok."""
        courses = data.requested_courses
        for i in range(len(courses)):
            for j in range(i + 1, len(courses)):
                a = courses[i]
                b = courses[j]
                for sa in a.slots:
                    for sb in b.slots:
                        if sa.overlaps(sb):
                            self._error_message = f"Jadwal {a.code} dan {b.code} bentrok."
                            print(self._error_message)
                            return False
        return True

class RegistrationService:
    """Koordinator proses registrasi mahasiswa."""

    def __init__(self, rules: list[IValidationRule]):
        """Menerima daftar rule melalui Dependency Injection."""
        self.rules = rules

    def run_registration(self, data: RegistrationData) -> bool:
        """Menjalankan semua validasi."""
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