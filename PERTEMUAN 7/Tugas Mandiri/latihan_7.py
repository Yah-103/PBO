import os
from datetime import datetime


class FileAnalyzer:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_ada = os.path.exists(file_path)
        
        if self.file_ada:
            self.__path = os.path.getsize(file_path)
        else:
            self.__path = None
    
    def get_file_bytes(self):
        if not self.file_ada:
            return "File tidak ditemukan"
        
        return os.path.getsize(self.file_path)
    
    def get_file_kilobytes(self):
        if not self.file_ada:
            return "File tidak ditemukan"
        
        size_bytes = os.path.getsize(self.file_path)
        size_kb = size_bytes / 1024
        return round(size_kb, 2)
    
    def get_modification_time(self):
        if not self.file_ada:
            return "File tidak ditemukan"
        
        timestamp = os.path.getmtime(self.file_path)
        
        mod_time = datetime.fromtimestamp(timestamp)
        
        formatted_time = mod_time.strftime("%d %B %Y, %H:%M:%S")
        
        return formatted_time
    
    def analyze(self):
        print("=" * 60)
        print("LAPORAN ANALISIS FILE")
        print("=" * 60)
        print(f"Nama File    : {os.path.basename(self.file_path)}")
        print(f"Path File    : {self.file_path}")
        print(f"File Ada     : {'Ya' if self.file_ada else 'Tidak'}")
        print("-" * 60)
        
        if self.file_ada:
            size_bytes = self.get_file_bytes()
            size_kb = self.get_file_kilobytes()
            
            print(f"Ukuran (Bytes) : {size_bytes} Bytes")
            print(f"Ukuran (KB)    : {size_kb} KB")
            
            mod_time = self.get_modification_time()
            print(f"Modifikasi Terakhir : {mod_time}")
        else:
            print("File tidak ditemukan. Tidak dapat dianalisis.")
        
        print("=" * 60)


if __name__ == "__main__":
    print("\n>>> PROGRAM FILE ANALYZER <<<\n")
    
    analyzer = FileAnalyzer(r"C:\Users\neko7\Kuliah\Semester 3\PBO_Praktikum\P7\Tugas Mandiri\dokumen.txt")

    analyzer.analyze()
    
    
    analyzer_error = FileAnalyzer("file_khayalan.txt")
    analyzer_error.analyze()