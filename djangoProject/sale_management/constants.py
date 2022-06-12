class OrderStatus:
    STATUS_NEW = 0
    STATUS_ACCEPTED = 1

    STATUS_CHOICES = (
        (STATUS_NEW, 'New'),
        (STATUS_ACCEPTED, 'Accepted'),
    )

    STATUS_CHOICES_DICT = dict(STATUS_CHOICES)


class Gender:
    FEMALE = 0
    MALE = 1
    UNKNOWN = 2

    GENDER_CHOICES = (
        (FEMALE, 'FEMALE'),
        (MALE, 'MALE'),
        (UNKNOWN, 'UNKNOWN'),
    )
