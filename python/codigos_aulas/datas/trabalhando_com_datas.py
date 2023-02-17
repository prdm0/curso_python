import datetime
import pytz
import pandas as pd

funcoes_datetime = [pkg for pkg in dir(datetime) if not pkg.startswith("_")]
funcoes_pytz = [pkg for pkg in dir(pytz) if not pkg.startswith("_")]


tabela = pd.DataFrame(pytz.all_timezones)
tabela_html = tabela.to_html()

import IPython

IPython.