from django.db import models


class Moneybox(models.Model):
    name = models.CharField(max_length=150)
    balance = models.PositiveIntegerField(default=0)
    goal = models.PositiveIntegerField(default=0)


    def residue(self):
        return self.goal - self.balance

    def push(self, value):
        if value and value > 0:
            self.balance += value

    def is_complete(self):
        return self.balance  == self.goal

