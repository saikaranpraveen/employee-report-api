from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

class PerformanceReport(models.Model):
    Months = (
    ("JANUARY", "January"),
    ("FEBRUARY", "February"),
    ("MARCH", "March"),
    ("APRIL","April"),
    ("MAY", 'May'),
    ("JUNE", 'June'),
    ("JULY", 'July'),
    ("AUGUST", 'August'),
    ("SEPTEMBER", 'September'),
    ("OCTOBER", 'October'),
    ("NOVEMBER", 'November'),
    ("DECEMBER", "December"),
    )

    month = models.CharField(max_length=100, choices= Months)    
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    punctuality_and_discipline = models.PositiveIntegerField(default=0, null ='False', blank = 'False', validators=[MinValueValidator(0), MaxValueValidator(10)])
    execution_of_duties = models.PositiveIntegerField(default=0, null ='False', blank = 'False', validators=[MinValueValidator(0), MaxValueValidator(10)])
    learning_and_development = models.PositiveIntegerField(default=0, null ='False', blank = 'False',validators=[MinValueValidator(0), MaxValueValidator(10)]) 
    team_cooperation = models.PositiveIntegerField(default=0, null ='False', blank = 'False',validators=[MinValueValidator(0), MaxValueValidator(10)])
    responsibility_taken = models.PositiveIntegerField(default=0, null ='False', blank = 'False',validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
         return f"{self.employee} {self.month}"

    def employeename(self):
        return f"{self.employee}"