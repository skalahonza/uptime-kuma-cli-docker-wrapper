import os
import click
from uptime_kuma_api import UptimeKumaApi, MonitorType

def create_if_not_exists(api, name):
    monitors = api.get_monitors()
    print(api.get_monitor(93))
    for monitor in monitors:
        if monitor['name'] == name:
            print(f"Monitor {name} already exists")
            return

    api.add_monitor(
        type=MonitorType.HTTP,
        url=f"https://{name}.slp.blue/healthz",
        name=name,
        expiryNotification=True,
        maxretries=5,
    )
    print(f'Added monitor: {name}')

@click.group()
def cli():
    """Uptime Kume CLI"""
    pass

@cli.command()
@click.argument('name')
def add_monitor(name):
    """
    Add a monitor with the specified NAME.
    """

    click.echo("Connecting to Uptime Kuma...")
    api = UptimeKumaApi(os.getenv('KUMA__URL'))
    api.login(os.getenv('KUMA__USERNAME'), os.getenv('KUMA__PASSWORD'))

    click.echo("Getting monitors...")
    monitors = api.get_monitors()

    for monitor in monitors:
        if monitor['name'] == name:
            click.echo(f"Monitor {name} already exists")
            api.disconnect()
            return

    api.add_monitor(
        type=MonitorType.KEYWORD,
        url=f"https://{name}/healthz",
        keyword='Healthy',
        name=name,
        expiryNotification=True,
        maxretries=5,
    )
    click.echo(f'Added monitor: {name}')
    click.echo(f"Monitor '{name}' has been added!")
    api.disconnect()

if __name__ == '__main__':
    cli()
