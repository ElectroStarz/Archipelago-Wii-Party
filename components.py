from worlds.LauncherComponents import Component, Type, components, launch, icon_paths


def run_client(*args: str) -> None:
    from .wii_party_client.main_client import launch_wii_party_client as launch_wp_client


    launch(launch_wp_client, name="Wii Party Client", args=args)


components.append(
    Component(
        "Wii Party Client",
        func=run_client,
        game_name="Wii Party",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)