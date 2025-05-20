from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Hotel(models.Model):
    name = models.CharField(max_length=30, default="qazzy")
    owner = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    state = models.CharField(max_length=50, default="ca")
    country = models.CharField(max_length=50, default="us")

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=50, default="Lab company")
    description = models.TextField(default="This is a company")

    def __str__(self):
        return self.name

class Room(models.Model):
    ROOM_STATUS = (("1", "available"), ("2", "not available"))
    ROOM_TYPE = (("1", "premium"), ("2", "deluxe"), ("3", "basic"))

    room_type = models.CharField(max_length=50, choices=ROOM_TYPE)
    capacity = models.IntegerField()
    price = models.IntegerField()
    size = models.IntegerField()
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    status = models.CharField(max_length=15, choices=ROOM_STATUS)
    room_number = models.IntegerField()

    def __str__(self):
        return self.hotel.name

class Reservation(models.Model):
    check_in = models.DateField()
    check_out = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    has_child = models.BooleanField(default=False)
    booking_id = models.CharField(max_length=100, default="null")

    def __str__(self):
        return self.guest.username

class PromoCode(models.Model):
    code = models.CharField(max_length=255, unique=True)
    discount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    expiration_date = models.DateField()
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "promocode"
        verbose_name_plural = "promocodes"

    def __str__(self):
        return f"PromoCode: {self.code}"

class Review(models.Model):
    RATINGS = [(i, f"{i} star{'s' if i > 1 else ''}") for i in range(1, 6)]

    name = models.CharField(max_length=50)
    rating = models.IntegerField(choices=RATINGS)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.name}"

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question

class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Vacancy(models.Model):
    title = models.CharField(max_length=200, default="Vacancy")
    text = models.TextField(default="We are hiring!")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # Newest first

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="This is a contact")
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]
    )
    email = models.EmailField(default="default@gmail.com")
    image = models.ImageField(upload_to="contacts", blank=True, null=True)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    feedback_text = models.TextField()
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        default=1
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "feedback"
        verbose_name_plural = "feedbacks"

    def __str__(self):
        return f"Feedback by {self.user.username}"

class News(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "news article"
        verbose_name_plural = "news articles"
        ordering = ['-published_at']

    def __str__(self):
        return self.title