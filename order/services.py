from django.conf import settings
from django.core.mail import send_mail

from boat.models import Boat
from order.models import Order


def send_order_email(order_item: Order):
    send_mail(
        'заявка на покупку лодки',
        f'{order_item} ({order_item.email}) хочет купить вашу лодку {order_item.boat.name}.'
        f'Сообщение {order_item.message}',
        settings.EMAIL_HOST_USER,
        [order_item.boat.owner.email]
    )