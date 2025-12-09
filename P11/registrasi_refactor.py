# LANGKAH 1: KODE BERMASALAH
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Set

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

class ValidatorManager:   # Melanggar SRP, OCP, DIP
    def process_validation(self, data: RegistrationData) -> bool:
        print(f"Memulai validasi registrasi untuk {data.student_name}...")

        total_sks = sum(course.sks for course in data.requested_courses)
        if total_sks > 24:
            print("Gagal: Total SKS melebihi batas 24.")
            return False

        for course in data.requested_courses:
            for req in course.prerequisites:
                if req not in data.completed_courses:
                    print(f"Gagal: Prasyarat {req} untuk {course.code} belum diambil.")
                    return False

        print("Registrasi berhasil (kode buruk).")
        return True

# LANGKAH 2: REFACTORING SRP & DIP
class IValidationRule(ABC):
    """Kontrak: semua rule validasi punya method validate() dan error_message."""

    @abstractmethod
    def validate(self, data: RegistrationData) -> bool:
        ...

    @property
    @abstractmethod
    def error_message(self) -> str:
        ...

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
                    self._error_message = (
                        f"Prasyarat {req} untuk {course.code} belum diambil."
                    )
                    return False
        return True

class JadwalBentrokRule(IValidationRule):
    """Rule untuk mengecek bentrok jadwal antar mata kuliah."""

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
                            return False
        return True

class RegistrationService:
    """
    Tanggung jawab tunggal: mengkoordinasi proses registrasi.

    Dependency Injection (DIP): menerima daftar IValidationRule,
    tidak bergantung pada implementasi konkret.
    """

    def __init__(self, rules: list[IValidationRule]):
        self.rules = rules

    def run_registration(self, data: RegistrationData) -> bool:
        all_ok = True
        for rule in self.rules:
            if not rule.validate(data):
                all_ok = False
                print(f"[GAGAL] {rule.error_message}")
        if all_ok:
            print("[SUKSES] Registrasi berhasil.")
        else:
            print("[INFO] Registrasi gagal.")
        return all_ok

# LANGKAH 3: EKSEKUSI & PEMBUKTIAN OCP
if __name__ == "__main__":
    completed_andi = {"IF101"}
    requested_andi = [
        Course(
            code="IF201",
            sks=3,
            prerequisites=["IF101"],
            slots=[TimeSlot("Mon", 9, 11)],
        ),
        Course(
            code="IF202",
            sks=3,
            prerequisites=["IF102"], 
            slots=[TimeSlot("Tue", 9, 11)],
        ),
    ]
    data_andi = RegistrationData(
        student_name="Andi",
        completed_courses=completed_andi,
        requested_courses=requested_andi,
    )

    sks_rule = SksLimitRule(max_sks=24)
    prereq_rule = PrerequisiteRule()
    service_andi = RegistrationService(rules=[sks_rule, prereq_rule])

    print("=== Skenario 1: Validasi SKS + Prasyarat ===")
    service_andi.run_registration(data_andi)

    completed_budi = {"IF101", "IF102"}
    requested_budi = [
        Course(
            code="IF201",
            sks=3,
            prerequisites=["IF101"],
            slots=[TimeSlot("Mon", 9, 11)],
        ),
        Course(
            code="IF202",
            sks=3,
            prerequisites=["IF102"],
            slots=[TimeSlot("Mon", 10, 12)], 
        ),
    ]
    data_budi = RegistrationData(
        student_name="Budi",
        completed_courses=completed_budi,
        requested_courses=requested_budi,
    )

    jadwal_rule = JadwalBentrokRule()
    service_budi = RegistrationService(
        rules=[SksLimitRule(24), PrerequisiteRule(), jadwal_rule]
    )

    print("\n=== Skenario 2: Pembuktian OCP (Tambah JadwalBentrokRule) ===")
    service_budi.run_registration(data_budi)