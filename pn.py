import io

import os

from .. import loader 

from PIL import Image

from pn.poshel_naxyi import PoshelNaxyi

def register(cb):

    cb(PNMod()) 

class PNMod(loader.Module):

    """Пошел нахуй.\n©Пятёрка"""

    strings = {'name': 'Poshel-naxyi'} 

    

    async def pncmd(self, event):

        """Используй .pn <реплай на картинку/стикер>."""

        try:

            reply = await event.get_reply_message()

            if not reply:

                return await event.edit("Это не реплай.")

            await event.edit("Подождите немного.")

            im = io.BytesIO()

            await event.edit("Качаю.")

            await event.client.download_file(reply, im)

            await event.edit("Делаю.")

            im = Image.open(im)

            pn = PoshelNaxyi(im)

            sb.save_video("pm.mp4")

            await event.edit("Отправляю...")

            await event.client.send_file(event.to_id, open("pm.mp4", "rb"), reply_to=reply)

            os.remove("pm.mp4")

            await event.delete()

        except:

            return await event.edit("Это не подходит для применения модуля.")
