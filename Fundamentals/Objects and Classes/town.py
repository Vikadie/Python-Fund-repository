class Town:

    def __init__(self, name_):
        self.name = name_
        self.latitude = 0
        self.longitude = 0

    def set_latitude(self, latitude_):
        self.latitude = latitude_

    def set_longitude(self, longitude_):
        self.longitude = longitude_

    def __repr__(self):
        return f"Town: {self.name} | Latitude: {self.latitude} | Longitude: {self.longitude}"


town = Town("Sofia")
town.set_latitude("42° 41\' 51.04\" N")
town.set_longitude("23° 19\' 26.94\" E")
print(town)