import sublime
import sublime_plugin
import os


class SaveAllExistingFilesCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        for w in sublime.windows():
            self._save_files_in_window(w)

    def _save_files_in_window(self, w):
        for v in w.views():
            self._save_exiting_file_in_view(v)

    def _save_exiting_file_in_view(self, v):
        if v.file_name() and os.path.isfile(v.file_name()):
            if v.is_dirty():
                v.run_command("save")


class CloseAllNonExistingFilesCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        for w in sublime.windows():
            self._close_files_in_window(w)

    def _close_files_in_window(self, w):
        for v in w.views():
            self._save_exiting_file_in_view(v)

    def _save_exiting_file_in_view(self, v):
        if not v.file_name() or not os.path.isfile(v.file_name()):
            print('closing: ' + v.name())
            v.set_scratch(True)
            v.close()
