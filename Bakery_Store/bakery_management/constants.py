class HistoryType:
    ADD_QUANTITY = 0
    EXPIRED_QUANTITY = 1
    SOLD_QUANTITY = 2

    HISTORY_CHOICES = (
        (ADD_QUANTITY, 'Add quantity'),
        (EXPIRED_QUANTITY, 'Expired quantity'),
        (SOLD_QUANTITY, 'Sold quantity')
    )

    HISTORY_CHOICES_DICT = dict(HISTORY_CHOICES)

