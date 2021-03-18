from bison import Bison, DictOption, Option, Scheme  # type: ignore

# Set configuration scheme.
config_scheme = Scheme(
    Option(
        "logging", default="info", choices=["debug", "info", "warn", "error"]
    ),  # noqa
)

# Create a new Bison instance to store and manage configuration data.
options = Bison(scheme=config_scheme)

# Set the environment variable prefix and enable auto-env.
options.env_prefix = "{{cookiecutter.name}}".upper()
options.auto_env = True
