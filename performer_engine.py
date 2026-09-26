class PerformerVariableEngine:
    def __init__(self, genre="funk", bpm=72, intensity=1.0):
        self.genre = genre
        self.bpm = bpm
        self.intensity = intensity

    def compute_animation_triggers(self):
        """Maps musical parameters to animation cue intensity and motion vectors."""
        if self.genre == "funk" and (69 <= self.bpm <= 72):
            return {
                "motion_vector": "high-energy",
                "head_nodding": "rhythmic",
                "brass_cue": True,
                "console_operation": "active"
            }
        elif self.genre == "quiet_storm" and self.bpm == 86:
            return {
                "motion_vector": "smooth-controlled",
                "facial_expression": "subtle-micro",
                "posture_weighting": "relaxed",
                "brass_cue": False
            }
        return {"motion_vector": "default", "intensity": self.intensity}
