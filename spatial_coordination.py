class SpatialCoordinationEngine:
    def __init__(self):
        self.horn_section = {
            "George": {"instrument": "Alto Saxophone", "position": [-1.5, 2.0, 0.0]},
            "Marcus": {"instrument": "Tenor Saxophone", "position": [-0.5, 2.0, 0.0]},
            "Bari Duke": {"instrument": "Baritone Saxophone", "position": [0.5, 2.0, 0.0]},
            "Barry": {"instrument": "Trombone", "position": [1.5, 2.0, 0.0]},
            "Gene": {"instrument": "Trumpet 1", "position": [-1.0, 2.5, -0.5]},
            "Herb": {"instrument": "Trumpet 2", "position": [1.0, 2.5, -0.5]}
        }
        self.keyboard_cockpits = {
            "Brock": {"rig": "Arturia PolyBrute 5-Keyboard Cockpit", "position": [-3.0, 0.0, 1.0]},
            "Clav Smoove": {"rig": "Clavinet 5-Keyboard Cockpit", "position": [3.0, 0.0, 1.0]}
        }

    def get_performer_coordinates(self, name):
        if name in self.horn_section:
            return self.horn_section[name]
        elif name in self.keyboard_cockpits:
            return self.keyboard_cockpits[name]
        return None
