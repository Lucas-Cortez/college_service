class Logger:
    def __init__(self):
        self.log_file = "log.txt"
        with open(self.log_file, "w") as file:
            file.write(f"INICIO DO LOG {40 * '='}\n")

    def log(self, message):
        with open(self.log_file, "a") as file:
            file.write(f"{message}\n")
        print(message)