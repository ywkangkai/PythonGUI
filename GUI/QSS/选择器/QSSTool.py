class QSSTool:
    @staticmethod
    def setQssToObj(qssFile, obj):
        with open(qssFile, 'r') as f:
            obj.setStyleSheet(f.read())