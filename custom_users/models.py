from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (VIPClient, 'VIPClient'),
    (CLIENT, 'CLIENT')
)

MALE = 1
FEMALE = 2
OTHER = 3

GENDER_TYPE = (
    (MALE, 'MALE'),
    (FEMALE, 'FEMALE'),
    (OTHER, 'OTHER')
)


BATKEN = 1
CHUY = 2
OSH = 3
TALAS = 4
NARYN = 5
DJALAL_ABAD = 6
ISSYK_KOL = 7

REGION_TYPE = (
    (BATKEN, 'BATKEN'),
    (CHUY, 'CHUY'),
    (OSH, 'OSH'),
    (TALAS, 'TALAS'),
    (NARYN, 'NARYN'),
    (DJALAL_ABAD, 'DJALAL-ABAD'),
    (ISSYK_KOL, 'ISSYK-KOL')
)


class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя',
                                    default=CLIENT)
    phone_number = models.CharField('phone_number', max_length=100)
    age = models.IntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Пол')
    region = models.IntegerField(choices=REGION_TYPE, verbose_name='Область')
