class ManageTempFile:
    def __init__(self, filename):
        self.file_name = filename
        return None

    def __enter__(self):
        print(f"Creating temp file: {self.file_name}")
        return self.file_name
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Safely removing temp file: {self.file_name}")

        if exc_type:
            print(f"-> Logged error: {exc_val}")
        return False

try:
    with ManageTempFile("testing_file.csv") as temp_file:
        print(f"Reading data from the {temp_file} file...")
        raise ValueError("Database connection lost during file processing!")
except ValueError as e:
    print(f"Main script caught the error: {e}")
