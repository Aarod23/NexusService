class APIError(Exception):
    ERROR_MESSAGES = {
        0: "An unknown error has occurred",
        1: "Not Found",
        2: "Invalid state",
        3: "Invalid payload",
        4: "Bad body",
        5: "Payload expired",
        6: "Bad code",
        7: "Missing scopes",
        8: "Unsupported sub type",
        9: "Method not allowed",
        10: "Bad query",
        11: "Missing authorization",
        12: "Missing access",
        13: "Datastore unavailable",
        14: "Account already exists",
        15: "Roblox account linked limit reached",
        16: "Roblox account already linked",
        17: "Too many accounts queried",
        18: "Invalid session",
        19: "Session not found",
        20: "Access expired"
    }

    def __init__(self, status_code: int, code: int):
        self.status_code = status_code
        self.code = code
        self.message = self.ERROR_MESSAGES.get(code, "Unknown error code")
        super().__init__(f"APIError {status_code}: {self.message}")


