from xml.dom import minidom


class ECGData:
    _SAMPLE_RATE = 0
    _DATA = []
    _LEAD = []

    def __init__(self, file):
        with open(file, 'r', encoding='utf8') as f:
            self.dom = minidom.parse(f)
            self.root = self.dom.documentElement

    @property
    def Data(self):
        assert len(self.root.getElementsByTagName('increment')) == 1

        self._SAMPLE_RATE = 1 / float(self.root.getElementsByTagName('increment')[0].attributes['value'].value)
        self._DATA = [[int(d) for d in i.firstChild.data.split(' ')[:-1]] for i in
                      self.root.getElementsByTagName('digits')]
        self._LEAD = [i.parentNode.parentNode.getElementsByTagName('code')[0].attributes['code'].value for i in
                      self.root.getElementsByTagName('digits')]
        self._DATA = dict(zip(self._LEAD, self._DATA))
        self._DATA['SAMPLE_RATE'] = self._SAMPLE_RATE
        return self._DATA



