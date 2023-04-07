class PasswordGenerator:
    password = 0
    preferredPassword = 0

    def generatePreferredPassword(self):
        newpass = self.preferredPassword + 1
        self.preferredPassword = newpass
        return newpass

    def generateNormalPassword(self):
        newpass = self.password + 1
        self.password = newpass
        return newpass