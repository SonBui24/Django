class CategoryChoices:
    EXPENSE = 0
    REVENUE = 1

    CATEGORY_CHOICES = (
        (EXPENSE, 'Expense'),
        (REVENUE, 'Revenue'),
    )

    CATEGORY_CHOICES_DICT = dict(CATEGORY_CHOICES)
