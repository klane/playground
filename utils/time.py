from datetime import datetime, timedelta
from numbers import Number


class Timer(object):
    ZERO = timedelta(0)

    def __init__(self):
        self._start = None
        self._stop = None
        self._split = None
        self._elapsed = Timer.ZERO

    def __str__(self):
        return f'{self:%e}'

    def __repr__(self):
        name = self.__class__.__name__
        return f'{name}(elapsed={self:%e}, split={self:%s}, total={self:%t})'

    def __format__(self, format_spec):
        if format_spec == '%e':
            return Timer.format(self.elapsed)
        elif format_spec == '%s':
            return Timer.format(self.split_elapsed)
        elif format_spec == '%t':
            return Timer.format(self.total_elapsed)
        else:
            return super(Timer, self).__format__(format_spec)

    @property
    def elapsed(self):
        if self.running:
            return datetime.now() - self._start
        elif self._stop is not None:
            return self._stop - self._start
        else:
            return Timer.ZERO

    @staticmethod
    def format(duration):
        if isinstance(duration, timedelta):
            seconds = duration.seconds
        elif isinstance(duration, Number):
            seconds = int(duration)
        else:
            raise TypeError('Duration should be a numeric value or timedelta object')

        days, seconds = divmod(seconds, 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        if days > 0:
            return f'{days:02d}:{hours:02d}:{minutes:02d}:{seconds:02d}'
        else:
            return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

    @property
    def running(self):
        return self._start is not None and self._stop is None

    def reset(self):
        self._start = None
        self._stop = None
        self._split = None
        self._elapsed = Timer.ZERO

    def split(self):
        if not self.running:
            raise RuntimeError('Timer not running')

        now = datetime.now()
        duration = now - self._split
        self._split = now
        return duration

    @property
    def split_elapsed(self):
        if self.running:
            return datetime.now() - self._split
        else:
            return Timer.ZERO

    def start(self):
        if self.running:
            raise RuntimeError('Timer already running')

        self._start = self._split = datetime.now()
        self._stop = None
        return self._start

    def stop(self):
        if not self.running:
            raise RuntimeError('Timer not running')

        self._stop = datetime.now()
        duration = self._stop - self._start
        self._elapsed += duration
        return duration

    @property
    def total_elapsed(self):
        if self.running:
            return self.elapsed + self._elapsed
        else:
            return self._elapsed
