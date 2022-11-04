import os
import sys
from os.path import dirname, abspath
import importlib.util
import pkgutil


def find_plugins():
    plugins_dir = os.path.join(dirname(abspath(__file__)), 'plugins')
    plugins = []
    for plugin_dir in os.listdir(plugins_dir):
        module_name = plugin_dir.removesuffix('.py')
        spec = importlib.util.spec_from_file_location(module_name,
                                                      os.path.join(plugins_dir, plugin_dir, "entrypoint.py"))
        plugin = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = plugin
        spec.loader.exec_module(plugin)
        plugins.append(plugin)

    for finder, name, ispkg in pkgutil.iter_modules():
        if name.startswith('platzky_'):
            plugins.append(importlib.import_module(name))

    return plugins


def plugify(app):
    for plugin in find_plugins():
        plugin.process(app)
    return app
