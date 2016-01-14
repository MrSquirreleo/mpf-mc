"""Base class used for things that "play" from the config files, such as
WidgetPlayer, ScreenPlayer, etc."""


class EventPlayer(object):
    config_file_section = None

    def __init__(self, mc):
        self.mc = mc

        self.mc.mode_controller.register_start_method(self.process_config,
                                                      self.config_file_section)

    def process_config(self, config, mode=None, priority=0):
        key_list = list()

        for event, settings in config.items():
            key_list.append(self.mc.events.add_handler(
                    event,
                    self.play,
                    mode=mode,
                    settings=settings))

        return self.unload_player_events, key_list

    def unload_player_events(self, key_list):
        self.mc.events.remove_handlers_by_keys(key_list)

    def play(self, settings, mode=None):
        raise NotImplementedError