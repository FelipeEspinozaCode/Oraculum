from datetime import datetime, timedelta, timezone

class UserRateLimit:
    """
    Estado de uso de un usuario. 
    Incluye 'last_request' para permitir la auto-limpieza de RAM en el RateLimiter.
    """

    def __init__(self, max_requests: int, window_seconds: int) -> None:
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.request_count = 0
        self.window_start = datetime.now(timezone.utc)
        # Sensor de actividad para el recolector de basura (RateLimiter)
        self.last_request = datetime.now(timezone.utc)

    def reset_if_needed(self) -> None:
        now = datetime.now(timezone.utc)
        if now - self.window_start > timedelta(seconds=self.window_seconds):
            self.request_count = 0
            self.window_start = now

    def allow_request(self) -> bool:
        # Actualizamos actividad siempre, permitiendo saber si el objeto es 'viejo'
        self.last_request = datetime.now(timezone.utc)
        self.reset_if_needed()

        if self.request_count < self.max_requests:
            self.request_count += 1
            return True

        return False