from database import Database
import config as cfg

db = Database(host=cfg.DB_HOST, user=cgf.user, password=cgf.password)

db.print_host()