import os
import logger
import tomllib

config_path = "conf.toml"


def load_config() -> dict[str]:
    """
    this handles the reading of the config files, usually returning data as follows :\n
    ->  **{"version":TheVersion, "path":PathOftheGames, "mirrors":ListOfUrlstoJson}**
    """
    logger_inst = logger.create_instance_logger("CONFIG", 40)
    try:
        with open(config_path, "r") as f:
            return tomllib.load(f)
    except tomllib.TOMLDecodeError:
        logger_inst.error("Couldn't decode the config file")
    except (IOError, OSError) as e:
        logger_inst.error("Error while trying to open config file, due to %s", e)


def default_path() -> str:
    return os.path.join(
        os.getenv("APPDATA") if os.name == "nt" else os.path.abspath(""),
        "CrackLauncher",
    )
