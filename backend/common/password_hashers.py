from django.contrib.auth.hashers import Argon2PasswordHasher


class Argon2OwaspPasswordHasher(Argon2PasswordHasher):
    """Argon2 password hasher with recommended settings from OWASP top 10.

    More information here: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id
    """

    time_cost = 3
    memory_cost = 12288
    parallelism = 1
