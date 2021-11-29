from email.message import EmailMessage
import aiosmtplib
import aiosqlite
import asyncio
import sys


async def get_recipients():
    recipients = []
    async with aiosqlite.connect('contacts.db') as db:
        async with db.execute("SELECT email FROM contacts") as cursor:
            async for row in cursor:
                recipients.append(row[0])

    return recipients


async def send_email(smtp_server, smtp_port, recipient):
    message = EmailMessage()
    message["From"] = recipient
    message["To"] = recipient
    message["Subject"] = f'Уважаемый {recipient.replace("@none_exists_test.ru", "")}! ' \
                         f'Спасибо, что пользуетесь нашим сервисом объявлений.'
    message.set_type('text/html', header='Content-Type')
    await aiosmtplib.send(
        message,
        hostname=smtp_server,
        port=smtp_port
    )


async def main():
    if len(sys.argv) != 3:
        print('Please provide 2 arguments: SMTP server address and port')
        exit(1)

    try:
        smtp_server_port = int(sys.argv[2])
    except ValueError:
        print('Port must be an integer')
        exit(1)

    smtp_server = sys.argv[1]

    recipients = await get_recipients()
    tasks = []

    for recipient in recipients:
        task = asyncio.create_task(send_email(smtp_server, smtp_server_port, recipient))
        tasks.append(task)

    await asyncio.gather(*tasks)
    print(f'All {len(recipients)} emails have been sent')


if __name__ == '__main__':
    asyncio.run(main())
