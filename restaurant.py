from pywebio.input import input as input_pw
from pywebio.output import put_markdown, put_success, put_error, put_warning
import messages_rest

guest_name = input_pw(messages_rest.MSG_WELCOME_GUEST, required=True)
put_success(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))
# put_error(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))
# put_warning(messages_rest.MSG_WELCOME_GUEST_WITH_NAME.format(name=guest_name))

put_markdown("## Меню")

print(guest_name)

