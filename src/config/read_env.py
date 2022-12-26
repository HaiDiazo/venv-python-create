from dotenv import dotenv_values

config = dotenv_values('.env')

my_config: str = config.get('MY_CONFIG')
coba_aja: bool = config.get('COBA_AJA')