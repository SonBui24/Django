class HistoryType:
    ADD_QUANTITY = 0
    EXPIRED_QUANTITY = 1
    INVENTORY_QUANTITY = 2

    HISTORY_CHOICES = (
        (ADD_QUANTITY, 'Add quantity'),
        (EXPIRED_QUANTITY, 'Expired quantity'),
        (INVENTORY_QUANTITY, 'Inventory quantity')
    )

    HISTORY_CHOICES_DICT = dict(HISTORY_CHOICES)

