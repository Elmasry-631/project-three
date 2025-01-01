from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
class Test(models.Model):
    test1 = models.TextField()
    test2 = models.IntegerField()
    # test3 = models.TextChoices()
    test4 = models.CharField(max_length=20)
    test5 = models.DecimalField(max_digits=3, decimal_places=2)
    test6 = models.DateField()
    test7 = models.TimeField()
    test8 = models.DateTimeField()
    test9 = models.BinaryField()
    test10= models.BooleanField()
    # test11= models.URLField()
    # test12= models.ChoicesField()
    test13= models.EmailField()
    # test14= models.AutoField()
    def __str__(self):
        return self.test1
    
    # واحد لواحد
    
class Testrelation1(models.Model):
    testrelation1 = models.CharField(max_length=20)
    def __str__(self):
        return self.testrelation1
class Testrelation2(models.Model):
    testrelation2 = models.CharField(max_length=20)
    testrelation3 = models.OneToOneField(Testrelation1, on_delete=models.CASCADE)
    def __str__(self):
        return self.testrelation2
    
    # واحد لكثير
    
class Testrelation3(models.Model):
    testrelation4 = models.CharField(max_length=20)
    def __str__(self):
        return self.testrelation4
    
class Testrelation4(models.Model):
    testrelation5 = models.CharField(max_length=20)
    testrelation6 = models.ForeignKey(Testrelation3,related_name='test', on_delete=models.PROTECT)
    def __str__(self):
        return self.testrelation5
    
    # كثير لكثير
    
class Testrelation5(models.Model):
    testrelation7 = models.CharField(max_length=20)
    def __str__(self):
        return self.testrelation7
        
class Testrelation6(models.Model):
    testrelation8 = models.CharField(max_length=20)
    testrelation9 = models.ManyToManyField(Testrelation5, related_name='test')
    def __str__(self):
        return self.testrelation8
    
    
class Testmedia(models.Model):
    name = models.CharField(max_length=20)
    testmedia1 = models.ImageField(upload_to='photos/%y/%m/%d')