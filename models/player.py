class Player:
    def __init__(self, player_id, name, city, rating=1000):
        self.id = player_id
        self.name = name
        self.city = city
        self.rating = rating

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "city": self.city,
            "rating": self.rating
        }

    @classmethod
    def from_dict(cls, data):
        return cls(data["id"], data["name"], data["city"], data["rating"])
