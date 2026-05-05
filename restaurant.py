from pywebio.input import input as input_pw, NUMBER, slider, checkbox
from pywebio.output import put_markdown, put_success, put_error, put_image, put_warning, put_text, put_row, put_column
import messages_rest
import images
import prices

guest_name = input_pw(messages_rest.MSG_WELCOME_GUEST, required=True)
put_success(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))
# put_error(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))
# put_warning(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))

put_markdown("## Меню")

put_row(
    [
        put_column([put_image(images.PIZZA_IMAGE, width='300px', height='200px'), put_text(f'Піцца {prices.PIZZA_PRICE}')]),
        put_column([put_image(images.BURGER_IMAGE, width='300px', height='200px'), put_text(f'Бургер {prices.BURGER_PRICE}')]),
    ]
)
put_row(
    [
        put_column([put_image(images.COLA_IMAGE, width='180px', height='120px'), put_text(f'Кола {prices.COLA_PRICE}')]),
        put_column([put_image(images.CAUSE_IMAGE, width='180px', height='120px'), put_text(f'Соуси {prices.CAUSE_PRICE}')]),
    ]
)
pizza_quantity = input_pw(label='Pizza', type=NUMBER, value=1)
burger_quantity = slider(label='Burger', min_value=0, max_value=10, value=2)
causes = checkbox(label='Causes', options=['майонез', 'кетчуп', 'гірчиця'])
print(causes)
causes_quantity = len(causes)