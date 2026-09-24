class Student:
    """Represents a single student and their four subject scores."""

    def __init__(self, full_name, section, spanish_score, english_score,
                 social_studies_score, science_score):
        self.full_name = full_name
        self.section = section
        self.spanish_score = spanish_score
        self.english_score = english_score
        self.social_studies_score = social_studies_score
        self.science_score = science_score

    def get_average(self):
        """Returns the average of the four subject scores."""
        total = (self.spanish_score + self.english_score +
                 self.social_studies_score + self.science_score)
        return total / 4

    def get_failed_subjects(self):
        """Returns a list of (subject_name, score) for subjects below 60."""
        subjects = [
            ("Spanish", self.spanish_score),
            ("English", self.english_score),
            ("Social Studies", self.social_studies_score),
            ("Science", self.science_score),
        ]
        return [(name, score) for name, score in subjects if score < 60]

    def to_dict(self):
        """Converts this Student object into a dictionary (used for CSV export)."""
        return {
            "full_name": self.full_name,
            "section": self.section,
            "spanish_score": self.spanish_score,
            "english_score": self.english_score,
            "social_studies_score": self.social_studies_score,
            "science_score": self.science_score,
        }

    @staticmethod
    def from_dict(data):
        """Builds a Student object from a dictionary (used for CSV import)."""
        return Student(
            full_name=data["full_name"],
            section=data["section"],
            spanish_score=float(data["spanish_score"]),
            english_score=float(data["english_score"]),
            social_studies_score=float(data["social_studies_score"]),
            science_score=float(data["science_score"]),
        )

    def __str__(self):
        return (f"{self.full_name} ({self.section}) - "
                f"Spanish: {self.spanish_score}, English: {self.english_score}, "
                f"Social Studies: {self.social_studies_score}, "
                f"Science: {self.science_score}, "
                f"Average: {self.get_average():.2f}")
