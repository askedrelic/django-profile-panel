import tempfile
import hotshot
import hotshot.stats
from cStringIO import StringIO

from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from debug_toolbar.panels import DebugPanel

def f8(x):
    """Helper function for time formatting"""
    return "%8.3f" % x


class ProfileDebugPanel(DebugPanel):
    """
    A panel to display Profiling info.
    """
    name = 'Profiling'
    has_content = True

    def __init__(self, context):
        self.stats = None
        self.list = []
        super(ProfileDebugPanel, self).__init__(context)

    def nav_title(self):
        return _('Profile')

    def nav_subtitle(self):
        if self.stats:
            return '%s function calls' % self.stats.total_calls
        else:
            return 'Profile not run'

    def title(self):
        return _('Profile')

    def url(self):
        return ''

    def content(self):
        context = self.context.copy()
        context.update({
            'stats': self.stats,
            'list': self.list,
            })

        return render_to_string('profile_panel/profile.html', context)

    def process_request(self, request):
        self.tmpfile = tempfile.NamedTemporaryFile()
        self.prof = hotshot.Profile(self.tmpfile.name)

    def process_view(self, request, callback, callback_args, callback_kwargs):
        return self.prof.runcall(callback, request, *callback_args, **callback_kwargs)

    def process_response(self, request, response):
        self.prof.close()
        if 'prof' in request.GET:
            print 'profiling'
            stats = hotshot.stats.load(self.tmpfile.name)

            #hide stdout output
            stats.stream = StringIO()
            stats.sort_stats('cumulative')

            self.stats = stats

            for func in self.stats.get_print_list({})[1]:
                cc, nc, tt, ct, _ = self.stats.stats[func]
                self.list.append(
                    (cc, nc, f8(tt), f8(ct), func[2], func[0], func[1]))
        else:
            print 'not profiling'

        return response
