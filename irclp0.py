import irc.client
from datetime import datetime
from unidecode import unidecode


class IRCClient(irc.client.SimpleIRCClient):
    def on_welcome(self, connection, event):
        connection.join("#guestbook")

    def on_pubmsg(self, connection, event):
        now = datetime.now()
        message = f"[{now.strftime('%H:%M:%S')}] <{event.source.nick}> {unidecode(event.arguments[0], errors='replace')}\n"
        with open('/dev/usb/lp0', 'w') as printer:
            printer.write(message)
            print(message)


def main():
    client = IRCClient()
    client.connect("zelazny.as21903.net", 6667, "irclp0")
    client.start()


if __name__ == "__main__":
    main()
