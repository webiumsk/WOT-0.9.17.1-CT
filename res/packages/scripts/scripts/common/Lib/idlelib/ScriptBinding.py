# 2017.02.03 21:59:01 St�edn� Evropa (b�n� �as)
# Embedded file name: scripts/common/Lib/idlelib/ScriptBinding.py
"""Extension to execute code outside the Python shell window.

This adds the following commands:

- Check module does a full syntax check of the current module.
  It also runs the tabnanny to catch any inconsistent tabs.

- Run module executes the module's code in the __main__ namespace.  The window
  must have been saved previously. The module is added to sys.modules, and is
  also added to the __main__ namespace.

XXX GvR Redesign this interface (yet again) as follows:

- Present a dialog box for ``Run Module''

- Allow specify command line arguments in the dialog box

"""
import os
import re
import string
import tabnanny
import tokenize
import tkMessageBox
from idlelib import PyShell
from idlelib.configHandler import idleConf
from idlelib import macosxSupport
IDENTCHARS = string.ascii_letters + string.digits + '_'
indent_message = 'Error: Inconsistent indentation detected!\n\n1) Your indentation is outright incorrect (easy to fix), OR\n\n2) Your indentation mixes tabs and spaces.\n\nTo fix case 2, change all tabs to spaces by using Edit->Select All followed by Format->Untabify Region and specify the number of columns used by each tab.\n'

class ScriptBinding:
    menudefs = [('run', [None, ('Check Module', '<<check-module>>'), ('Run Module', '<<run-module>>')])]

    def __init__(self, editwin):
        self.editwin = editwin
        self.flist = self.editwin.flist
        self.root = self.editwin.root
        if macosxSupport.isCocoaTk():
            self.editwin.text_frame.bind('<<run-module-event-2>>', self._run_module_event)

    def check_module_event(self, event):
        filename = self.getfilename()
        if not filename:
            return 'break'
        if not self.checksyntax(filename):
            return 'break'
        if not self.tabnanny(filename):
            return 'break'

    def tabnanny(self, filename):
        f = open(filename, 'r')
        try:
            tabnanny.process_tokens(tokenize.generate_tokens(f.readline))
        except tokenize.TokenError as msg:
            msgtxt, (lineno, start) = msg
            self.editwin.gotoline(lineno)
            self.errorbox('Tabnanny Tokenizing Error', 'Token Error: %s' % msgtxt)
            return False
        except tabnanny.NannyNag as nag:
            self.editwin.gotoline(nag.get_lineno())
            self.errorbox('Tab/space error', indent_message)
            return False

        return True

    def checksyntax(self, filename):
        self.shell = shell = self.flist.open_shell()
        saved_stream = shell.get_warning_stream()
        shell.set_warning_stream(shell.stderr)
        with open(filename, 'r') as f:
            source = f.read()
        if '\r' in source:
            source = re.sub('\\r\\n', '\n', source)
            source = re.sub('\\r', '\n', source)
        if source and source[-1] != '\n':
            source = source + '\n'
        text = self.editwin.text
        text.tag_remove('ERROR', '1.0', 'end')
        try:
            return compile(source, filename, 'exec')
        except (SyntaxError, OverflowError, ValueError) as err:
            try:
                msg, (errorfilename, lineno, offset, line) = err
                if not errorfilename:
                    err.args = (msg, (filename,
                      lineno,
                      offset,
                      line))
                    err.filename = filename
                self.colorize_syntax_error(msg, lineno, offset)
            except:
                msg = '*** ' + str(err)

            self.errorbox('Syntax error', "There's an error in your program:\n" + msg)
            return False
        finally:
            shell.set_warning_stream(saved_stream)

    def colorize_syntax_error(self, msg, lineno, offset):
        text = self.editwin.text
        pos = '0.0 + %d lines + %d chars' % (lineno - 1, offset - 1)
        text.tag_add('ERROR', pos)
        char = text.get(pos)
        if char and char in IDENTCHARS:
            text.tag_add('ERROR', pos + ' wordstart', pos)
        if '\n' == text.get(pos):
            text.mark_set('insert', pos)
        else:
            text.mark_set('insert', pos + '+1c')
        text.see(pos)

    def run_module_event(self, event):
        """Run the module after setting up the environment.
        
        First check the syntax.  If OK, make sure the shell is active and
        then transfer the arguments, set the run environment's working
        directory to the directory of the module being executed and also
        add that directory to its sys.path if not already included.
        
        """
        filename = self.getfilename()
        if not filename:
            return 'break'
        code = self.checksyntax(filename)
        if not code:
            return 'break'
        if not self.tabnanny(filename):
            return 'break'
        interp = self.shell.interp
        if PyShell.use_subprocess:
            interp.restart_subprocess(with_cwd=False)
        dirname = os.path.dirname(filename)
        interp.runcommand('if 1:\n            __file__ = {filename!r}\n            import sys as _sys\n            from os.path import basename as _basename\n            if (not _sys.argv or\n                _basename(_sys.argv[0]) != _basename(__file__)):\n                _sys.argv = [__file__]\n            import os as _os\n            _os.chdir({dirname!r})\n            del _sys, _basename, _os\n            \n'.format(filename=filename, dirname=dirname))
        interp.prepend_syspath(filename)
        interp.runcode(code)
        return 'break'

    if macosxSupport.isCocoaTk():
        _run_module_event = run_module_event

        def run_module_event(self, event):
            self.editwin.text_frame.after(200, lambda : self.editwin.text_frame.event_generate('<<run-module-event-2>>'))
            return 'break'

    def getfilename(self):
        """Get source filename.  If not saved, offer to save (or create) file
        
        The debugger requires a source file.  Make sure there is one, and that
        the current version of the source buffer has been saved.  If the user
        declines to save or cancels the Save As dialog, return None.
        
        If the user has configured IDLE for Autosave, the file will be
        silently saved if it already exists and is dirty.
        
        """
        filename = self.editwin.io.filename
        if not self.editwin.get_saved():
            autosave = idleConf.GetOption('main', 'General', 'autosave', type='bool')
            if autosave and filename:
                self.editwin.io.save(None)
            else:
                confirm = self.ask_save_dialog()
                self.editwin.text.focus_set()
                if confirm:
                    self.editwin.io.save(None)
                    filename = self.editwin.io.filename
                else:
                    filename = None
        return filename

    def ask_save_dialog(self):
        msg = 'Source Must Be Saved\n' + '     ' + 'OK to Save?'
        confirm = tkMessageBox.askokcancel(title='Save Before Run or Check', message=msg, default=tkMessageBox.OK, master=self.editwin.text)
        return confirm

    def errorbox(self, title, message):
        tkMessageBox.showerror(title, message, master=self.editwin.text)
        self.editwin.text.focus_set()
# okay decompyling c:\Users\PC\wotsources\files\originals\res\packages\scripts\scripts\common\Lib\idlelib\ScriptBinding.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.02.03 21:59:02 St�edn� Evropa (b�n� �as)
