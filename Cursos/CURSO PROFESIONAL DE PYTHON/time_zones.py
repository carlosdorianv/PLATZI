from datetime import datetime
import pytz

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

