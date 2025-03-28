class PersonService:
    @staticmethod
    def calculate_ideal_weight(person):
        try:
            height = float(person.height)
            if person.sex == 'm':
                return (72.7 * height) - 58
            elif person.sex == 'f':
                return (62.1 * height) - 44.7
            return None
        except (ValueError, TypeError):
            return None