import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Set

# Konfigurasi Logging (LANGKAH 2)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
)

LOGGER = logging.getLogger("registration")

@dataclass
class TimeSlot:
    """Representasi satu blok waktu perkuliahan.

    Attributes:
        day: Hari kuliah (misal: 'Mon', 'Tue').
        start: Jam mulai dalam format 24 jam (misal: 9 untuk jam 09.00).
        end: Jam selesai dalam format 24 jam (misal: 11 untuk jam 11.00).
    """

    day: str
    start: int
    end: int

    def overlaps(self, other: "TimeSlot") -> bool:
        """Mengecek apakah dua jadwal saling bertumpukan.

        Args:
            other: Objek :class:`TimeSlot` lain yang akan dibandingkan.

        Returns:
            bool: ``True`` jika kedua slot bertumpukan di hari dan jam yang sama,
            ``False`` jika tidak.
        """
        return self.day == other.day and self.start < other.end and other.start < self.end


@dataclass
class Course:
    """Representasi mata kuliah yang dapat diregistrasikan.

    Attributes:
        code: Kode mata kuliah (misal: 'IF201').
        sks: Beban studi dalam SKS.
        prerequisites: Daftar kode mata kuliah prasyarat.
        slots: Daftar jadwal perkuliahan untuk mata kuliah ini.
    """

    code: str
    sks: int
    prerequisites: List[str]
    slots: List[TimeSlot]


@dataclass
class RegistrationData:
    """Data yang dibutuhkan untuk proses registrasi mata kuliah.

    Attributes:
        student_name: Nama mahasiswa yang melakukan registrasi.
        completed_courses: Set kode mata kuliah yang sudah pernah diambil/lulus.
        requested_courses: Daftar objek :class:`Course` yang ingin diregistrasikan.
    """

    student_name: str
    completed_courses: Set[str]
    requested_courses: List[Course]


class ValidatorManager:
    """Contoh kelas dengan desain buruk (melanggar SRP, OCP, DIP).

    Kelas ini dibiarkan apa adanya sebagai pembanding terhadap desain yang
    sudah direfaktor pada :class:`RegistrationService`.
    """

    def process_validation(self, data: RegistrationData) -> bool:
        """Menjalankan validasi registrasi dengan cara yang belum SOLID.

        Args:
            data: Data registrasi yang akan divalidasi.

        Returns:
            bool: ``True`` jika registrasi dinyatakan valid, ``False`` jika tidak.
        """
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

# LANGKAH 2: REFACTORING SRP & DIP + LOGGING
class IValidationRule(ABC):
    """Kontrak umum untuk semua rule validasi registrasi."""

    @abstractmethod
    def validate(self, data: RegistrationData) -> bool:
        """Menjalankan validasi terhadap data registrasi.

        Args:
            data: Data registrasi yang akan divalidasi.

        Returns:
            bool: ``True`` jika data lolos rule ini, ``False`` jika gagal.
        """
        ...

    @property
    @abstractmethod
    def error_message(self) -> str:
        """Pesan error yang dihasilkan bila validasi gagal."""
        ...


class SksLimitRule(IValidationRule):
    """Rule untuk membatasi total SKS yang dapat diregistrasikan."""

    def __init__(self, max_sks: int):
        """Inisialisasi rule batas SKS.

        Args:
            max_sks: Batas maksimum total SKS yang diizinkan.
        """
        self.max_sks = max_sks
        self._error_message = ""

    @property
    def error_message(self) -> str:
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        """Memvalidasi apakah total SKS tidak melebihi batas."""
        total = sum(c.sks for c in data.requested_courses)
        if total > self.max_sks:
            self._error_message = f"Total SKS {total} melebihi batas {self.max_sks}."
            return False
        return True


class PrerequisiteRule(IValidationRule):
    """Rule untuk mengecek pemenuhan prasyarat mata kuliah."""

    def __init__(self):
        self._error_message = ""

    @property
    def error_message(self) -> str:
        return self._error_message

    def validate(self, data: RegistrationData) -> bool:
        """Memvalidasi apakah seluruh prasyarat sudah pernah diambil."""
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
        """Memvalidasi apakah tidak ada jadwal perkuliahan yang bertumpukan."""
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
    """Kelas high-level untuk mengkoordinasi proses registrasi mata kuliah.

    Kelas ini menerapkan prinsip SRP dan DIP dengan cara menerima daftar
    objek :class:`IValidationRule` melalui dependency injection.
    """

    def __init__(self, rules: list[IValidationRule]):
        """Menginisialisasi :class:`RegistrationService`.

        Args:
            rules: Daftar rule validasi yang akan dijalankan pada proses
                registrasi. Setiap elemen harus mengimplementasikan
                :class:`IValidationRule`.
        """
        self.rules = rules

    def run_registration(self, data: RegistrationData) -> bool:
        """Menjalankan proses registrasi dan semua validasi yang dibutuhkan.

        Args:
            data: Data registrasi yang akan diproses.

        Returns:
            bool: ``True`` jika seluruh rule validasi lolos dan registrasi sukses,
            ``False`` jika ada minimal satu rule yang gagal.
        """
        LOGGER.info("Memulai proses registrasi untuk mahasiswa '%s'.", data.student_name)

        all_ok = True
        for rule in self.rules:
            if not rule.validate(data):
                all_ok = False
                LOGGER.error("[GAGAL] %s", rule.error_message)

        if all_ok:
            LOGGER.info("[SUKSES] Registrasi berhasil untuk '%s'.", data.student_name)
        else:
            LOGGER.info("[INFO] Registrasi gagal untuk '%s'.", data.student_name)

        return all_ok

# LANGKAH 3: EKSEKUSI & PEMBUKTIAN OCP
if __name__ == "__main__":
    print("=== Skenario 1: Validasi SKS + Prasyarat ===")
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
    service_andi.run_registration(data_andi)

    print("\n=== Skenario 2: Pembuktian OCP (Tambah JadwalBentrokRule) ===")
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
    service_budi.run_registration(data_budi)