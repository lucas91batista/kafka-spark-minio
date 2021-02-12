# Traitlet configuration file for jupyter-notebook.

c.ServerProxy.servers = {
    'openrefine': {
        'command': ['airflow webserver', '--port', '{port}'],
        'port': 8080,
        'timeout': 120,
        'launcher_entry': {
            'enabled': True,
            'icon_path': '/home/jovyan/.jupyter/airflow-logo.png',
            'title': 'Airflow',
        },
    },
}
